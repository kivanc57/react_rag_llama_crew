# React&RAG LLama Crew

## 🚀 Overview
This project introduces an **AI Agent Crew** powered by **LlamaIndex** to analyze, generate, and process code efficiently. The system consists of **multiple specialized LLMs and a ReActAgent**, forming a collaborative AI team that enhances Retrieval-Augmented Generation (RAG), structured output parsing, and vector-based search.

## 🔥 Key Features

### 🏆 Multi-Agent AI Crew
- **Llama3.2**: Handles natural language understanding and analysis.
- **CodeLlama**: Specialized in code generation and improvement.
- **Ollama**: Supports enhanced query response and knowledge retrieval.
- **ReActAgent**: Coordinates tools, interacts with the user, and ensures logical reasoning.

### 🧠 Intelligent Code Analysis & Generation
- Generates, refines, and explains code based on user prompts.
- Understands complex queries and adapts responses accordingly.

### 📄 API Documentation Querying
- **Vector-based search** on API documentation for instant lookups.
- **Automatic document processing** for `.pdf` files.
- **LlamaParse integration** to extract meaningful text from documents.

### 🔎 Retrieval-Augmented Generation (RAG)
- **Combines LLMs with real-time document retrieval** to enhance code generation accuracy.
- **Ensures responses are grounded in relevant documentation**.
- Reduces hallucinations and improves factual correctness.

### 📂 Code Reader Functionality
- Reads and retrieves code files using the **code_reader** tool.
- Helps in debugging, refactoring, and understanding existing code.

### 🔗 LlamaIndex-Powered Query Pipeline
- **VectorStoreIndex** for efficient document retrieval.
- **QueryEngineTool** for answering API documentation queries.
- **SimpleDirectoryReader** to load and process data.

### ⚙️ Advanced Code Parsing & Output Structuring
- Uses **PydanticOutputParser** to structure output in JSON format.
- Generates **clean, structured** code with meaningful descriptions and filenames.

### 🎯 Robust & Reliable Execution
- **Error handling & retry mechanism** for resilient processing.
- Saves generated code **automatically** to the output directory.

## 🛠 How It Works
1. **User Input**: Enter a prompt to generate or analyze code.
2. **Processing**: The agent crew retrieves relevant documentation, reads code, and formulates responses.
3. **Generation**: The AI produces well-structured code and descriptions.
4. **Output**: The code is saved with an appropriate filename.

## 🏗 Technologies Used
- **LlamaIndex**: Efficient document indexing and retrieval.
- **Ollama**: Llama3.2 & CodeLlama models for text & code processing.
- **Pydantic**: Structured output parsing.
- **HuggingFace Optimum**: High-performance vector embeddings.
- **Retrieval-Augmented Generation (RAG)**: Enhances AI responses with real-time document retrieval.
- **Ast & Dotenv**: Code execution & environment configuration.

## 📌 Usage
1. Place code and documentation files in the `data/` folder.
2. Run the script:  
   ```bash
   python main.py
   ```
3. Follow the prompt to analyze or generate code.
4. Output files are saved in the `output/` folder.

## 📩 Contact
For improvements or issues, feel free to contribute or reach out!
