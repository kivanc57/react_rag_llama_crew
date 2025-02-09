import os
import ast
from pydantic import BaseModel
from dotenv import load_dotenv

from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate, Settings
from llama_index.embeddings.huggingface_optimum import OptimumEmbedding
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.query_pipeline import QueryPipeline

from code_reader import code_reader
from prompts import context, code_parser_template

# Get env variables
load_dotenv()

# Configure vector embeddings
OptimumEmbedding.create_and_save_optimum_model("BAAI/bge-small-en-v1.5", "./bge_onnx")
embed_model = OptimumEmbedding(folder_name="./bge_onnx")
Settings.embed_model = embed_model

# Get reader LLM
reader_llm = Ollama(model='llama3.2', request_timeout=300.0)

# Configure parser
parser = LlamaParse(result_type='markdown')
file_extractor = {'.pdf': parser}
documents = SimpleDirectoryReader('data', file_extractor=file_extractor).load_data()

# Parse input
vector_index = VectorStoreIndex.from_documents(documents)
query_engine = vector_index.as_query_engine(llm=reader_llm)

# Configure tools
tools = [
  QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
      name="api_documentation",
      description="This gives documentation about code for an API. Use this for reading docs for the API."
    )
  ),
  code_reader,
]

# Get coder LLM and deploy it as an agent
coder_llm = Ollama(model="codellama", request_timeout=300.0)
agent = ReActAgent.from_tools(tools, llm=coder_llm, verbose=True, context=context)

# Create output format
class CodeOutput(BaseModel):
  code: str
  description: str
  filename: str

# Configure parser to get output as JSON file
parser = PydanticOutputParser(CodeOutput)
json_prompt_str = parser.format(code_parser_template)
json_prompt_template = PromptTemplate(json_prompt_str)
output_pipeline = QueryPipeline(chain=[json_prompt_template, reader_llm])



def main():
  retries = 0

  while retries < 3:
    try:
      prompt = input("Enter a prompt (q to quit): ").lower()
      if prompt == 'q':
        break
      result = agent.query(prompt)
      next_result = output_pipeline.run(response=result)
      cleaned_json = ast.literal_eval(str(next_result).replace("assistant:", ""))
    except Exception as e:
      retries += 1
      print(f"Error occurred, retry {retries}", e)
    
    if retries >= 3:
      print("Unable to process request, try again...")
      continue

    print("Code Generated")
    print(cleaned_json["code"])

    print("\n\nDescription:", cleaned_json["description"])

    filename = cleaned_json["filename"]

    try:
      with open(os.path.join("output", filename), "w") as f:
        f.write(cleaned_json["code"])
      print("Saved file", filename)
    except Exception as e:
      print(f"Error saving file: {e}")

if __name__ == '__main__':
  main()
