import os
from llama_index.core.tools import FunctionTool

def code_reader_function(file_name):
  path = os.path.join('data', file_name)
  try:
    with open(path, 'r') as f:
      content = f.read()
      print('Code is read\n')
      return {'file_content': content}
  except Exception as e:
    return {f"Error reading code: {e}"}

code_reader = FunctionTool.from_defaults(
  fn=code_reader_function,
  name="code_reader",
  description=
  """
  This tool can read the contents of code files and returns their results.
  Use this when you need to read the contents of a file
  """
)
