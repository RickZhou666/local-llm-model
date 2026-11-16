
from ollama import chat

response = chat(
    model="qwen3:14b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Explain how AI agent tool calling works."
        },
    ],
)

print(response.message.content)
