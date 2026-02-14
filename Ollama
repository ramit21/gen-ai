# 🚀 Ollama -- Run LLMs Locally & Build AI Applications

Ollama is an open-source tool that lets you run Large Language Models
(LLMs) locally on your machine.

## ✅ Features

-   Keep your data private
-   No cloud dependency required
-   Build AI applications with REST APIs
-   Customize and publish your own models

------------------------------------------------------------------------

## 📦 Installation

1.  Visit https://ollama.com/download\
2.  Install the software\
3.  Select **YES** to install the CLI tool during setup

------------------------------------------------------------------------

## ▶️ Running a Model

``` bash
ollama run <model-name>
```

Example:

``` bash
ollama run llama3.2
```

------------------------------------------------------------------------

## 💬 Chat Commands

  Command    Description
  ---------- --------------------
  `/clear`   Clear chat history
  `/bye`     Exit session

------------------------------------------------------------------------

## 🛠 Model Management

``` bash
ollama pull <model>   # Download model only
ollama list           # List downloaded models
ollama ps             # Show running models
ollama stop <model>   # Stop model
ollama rm <model>     # Remove model
```

------------------------------------------------------------------------

## 🌐 REST API

Start server:

``` bash
ollama serve
```

Server runs at:

    http://localhost:11434

------------------------------------------------------------------------

## 📡 Generate API Example

``` bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen:0.5b",
  "prompt": "Who invented computing?"
}'
```

Disable streaming:

``` json
"stream": false
```

------------------------------------------------------------------------

## 💬 Chat API Example

``` bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen:0.5b",
  "messages": [
    {"role": "user", "content": "Who invented computing?"},
    {"role": "assistant", "content": "Charles Babbage"},
    {"role": "user", "content": "When?"}
  ],
  "stream": false
}'
```

------------------------------------------------------------------------

## 🧠 Flask Integration Example

``` python
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

load_dotenv()
app = Flask(__name__)

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL_NAME")

def chat_with_model(messages):
    url = f"{BASE_URL}/chat/completions"
    headers = {"Content-Type": "application/json"}

    if API_KEY and API_KEY.lower() != "none":
        headers["Authorization"] = f"Bearer {API_KEY}"

    payload = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    return data["choices"][0]["message"]["content"]

@app.route("/ask", methods=["GET"])
def ask():
    user_query = request.args.get("q", "")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_query}
    ]
    answer = chat_with_model(messages)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
```

------------------------------------------------------------------------

## ⚙️ Model Customization (Modelfile)

``` dockerfile
FROM llama3

SYSTEM """
You are a precise assistant that answers with clean, factual responses.
"""

PARAMETER temperature 0.3
PARAMETER top_p 0.95
PARAMETER num_ctx 4096
```

Build custom model:

``` bash
ollama create mymodel -f Modelfile
ollama run mymodel
```

------------------------------------------------------------------------

## 🎯 Why Use Ollama?

-   Privacy-first AI development
-   Fully local inference
-   OpenAI-compatible APIs
-   Easy dev-to-prod switching
-   Model customization support

------------------------------------------------------------------------

## 📌 Ideal For

-   AI Developers
-   ML Engineers
-   Privacy-focused startups
-   Researchers
-   Edge AI deployments
