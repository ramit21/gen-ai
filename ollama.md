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
> ollama run <model-name> shows following information about the model:
> 
Model parameters: weights and biases to fine tune.

Context length: How many tokens model can remember and process at once. High conext length => extensive conversations => more computational resources. 

Embedding length: Size of vector representation of each token. Highr value - model can encode more details.

Quantization: Reducing precision of numbers used in model to save memory and speed up processing.

ollama.com/library has all models supported.
eg >ollama run llava -> >> what is there in this image: ./logo.jpg -> gives textual summary of the image provided.
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

Olama REST API: lets you interact with LLMs programmatically.

>ollama serve -> starts ollama server on localhost:11434, to be accessed via REST APIs.
>
Its compatible with OpenAPI API, ie in production, if you want to switch away from local Ollama to OpenApi apis, then just plugin the OpenApi keys and switch to latter's APIs in your application instead of Ollama APIs.
	
API provides different endpoints for deleting a model, pull model etc.

2 more useful APIs are /generate - generates text response, /chat - output is generated based on previous chat history that you need to provide.
------------------------------------------------------------------------

### 📡 Generate API Example

``` bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen:0.5b",
  "prompt": "Who invented computing?"
}'
```

Disable streaming (ie generate all output in one go)

``` json
"stream": false
```

------------------------------------------------------------------------

### 💬 Chat API Example

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
## Programmatic access

Accessing Ollama from application code using OpenApi APIs:

Writing code calling OpenApi specs, makes it easy to switch dev mode pointing to local Ollama server, and prod mode to OpenApi URL. The open_Api_keys is set to any random text for dev mode, and actual OPENApi key for prod mode.

### 🧠 Flask Integration Example

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
        "messages": messages # messages as chat history context input to the model
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

To run above, first setup Python virtual env. A virtual environment isolates your project’s Python packages from system-wide libraries and other projects, giving you clean, reproducible setups.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

```

------------------------------------------------------------------------

## ⚙️ Model Customization (Modelfile)
Ollama supports Model customization and the upload of custom model in the Ollama registry.
Customisation is defined in a **Modelfile**, with instructions similar to a Dockerfile.
``` 
FROM llama3

SYSTEM """
You are a precise assistant who answers with clean, factual responses.
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
Push to ollama registry:
```
ollama login
ollama tag mymodel username/mymodel:v1
ollama push username/mymodel:latest
```

Reusing the model from registry:
```
ollama pull username/mymodel:latest

ollama run username/mymodel
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


Note: Ollama hosts only open‑source, locally runnable models. It supports text LLMs (Llama, Mistral, Gemma, Qwen), vision models (LLaVA, Moondream), and some image generators (Stable Diffusion, Flux). It does not include OpenAI’s proprietary models like Whisper (audio), Sora (video), or GPT‑4. Those remain cloud‑only and accessible exclusively through the OpenAI API. Ollama is ideal for local experimentation, but not for audio/video generation or OpenAI‑specific workflows.
