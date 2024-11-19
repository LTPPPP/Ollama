from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="Ollama"
)

conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3.2:latest",
        stream=True,
        messages=conversation_history
    )

    response_message = ""
    for chunk in response:
        response_message += chunk.choices[0].delta.content or ""

    conversation_history.append({"role": "assistant", "content": response_message})

    print("Assistant:", response_message)
