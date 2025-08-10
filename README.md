# TasksCS

This repository contains four main files, each demonstrating different programming concepts and integrations in Python. The focus is on API consumption, language model integration, and practical scripting. All sensitive information (such as API keys) has been removed for security.

---

## Repository Structure

```
TasksCS/
│
├── consumeApi.py
├── langgraph.py
├── <file3>.py
├── <file4>.py
└── README.md
```

---

## File Explanations

### 1. `consumeApi.py`

**Purpose:**  
This script demonstrates how to consume a REST API using Python. It shows how to make HTTP requests, handle responses, and process data from an external service.

**Key Features:**
- Uses the `requests` library to send HTTP requests.
- Handles authentication using environment variables for API keys.
- Parses JSON responses and displays relevant information.
- Includes error handling for failed requests.

**Usage Example:**
```python
import requests
import os

API_KEY = os.getenv("AZURE_OPENAI_KEY")
response = requests.get("https://api.example.com/data", headers={"Authorization": f"Bearer {API_KEY}"})
print(response.json())
```

---

### 2. `langgraph.py`

**Purpose:**  
This script integrates with Azure OpenAI services to demonstrate how to use large language models (LLMs) in Python. It shows how to set up the client, send prompts, and handle responses.

**Key Features:**
- Connects to Azure OpenAI using environment variables for secure API key management.
- Sends prompts to a language model and receives generated text.
- Configurable model parameters such as deployment name, model name, and temperature.
- Demonstrates best practices for working with cloud-based AI services.

**Usage Example:**
```python
from openai import AzureChatOpenAI
import os

llm = AzureChatOpenAI(
    deployment_name="AopenAI",
    model_name="gpt-35-turbo",
    temperature=0,
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_base="https://firsttaskoai.openai.azure.com/",
    openai_api_version="2023-05-15"
)
response = llm.generate("Hello, world!")
print(response)
```

---

### 3. `<file3>.py`

**Purpose:**  
_Replace this section with the actual filename and description._  
This file demonstrates [describe the main functionality, e.g., data processing, automation, etc.].

**Key Features:**
- [List key features or modules used]
- [Describe any unique logic or integrations]

**Usage Example:**
```python
# Example code snippet from file3.py
```

---

### 4. `<file4>.py`

**Purpose:**  
_Replace this section with the actual filename and description._  
This file is focused on [describe the main functionality, e.g., utility functions, data analysis, etc.].

**Key Features:**
- [List key features or modules used]
- [Describe any unique logic or integrations]

**Usage Example:**
```python
# Example code snippet from file4.py
```

---

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Sopanpatil22/TasksCS.git
   cd TasksCS
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**  
   Create a `.env` file or set environment variables in your system for any required API keys.

4. **Run the scripts:**  
   ```sh
   python consumeApi.py
   python langgraph.py
   # etc.
   ```

---

## Security

- **Never commit secrets or API keys.** Always use environment variables.
- If a secret is accidentally committed, follow [GitHub’s guide to removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or suggestions, please open an issue or contact the repository owner.
