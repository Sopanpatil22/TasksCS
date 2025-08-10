import os
import openai

AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") or "https://firsttaskoai.openai.azure.com/"
#AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY") or "6I1m3qrSuwN0hFCavPrmZarUXy5wkwCEQp9gcTt07bz5YaBpBbFuJQQJ99BHACqBBLyXJ3w3AAABACOG8MHB"
API_VERSION = "2023-05-15"
DEPLOYMENT = "gpt-35-turbo"

openai.api_type = "azure"
openai.api_key = AZURE_API_KEY
openai.api_base = AZURE_ENDPOINT
openai.api_version = API_VERSION

def have_a_chat(history):
    try:
        response = openai.ChatCompletion.create(
            engine=DEPLOYMENT,
            messages=history,
            temperature=0.7,
            max_tokens=500,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as err:
        return f"Oops, something went wrong: {err}"

if __name__ == "__main__":
    intro = {"role": "system", "content": "You’re a warm and helpful assistant."}
    question = {"role": "user", "content": "Tell me something cool about space."}
    conversation_history = [intro, question]
    print("User:", question["content"])
    reply = have_a_chat(conversation_history)
    print("Assistant:", reply)
