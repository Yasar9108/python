import openai


openai.api_key="Enter Youe api key"

def chat_bot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    print("Chatbot is running! Type 'exit', 'bye', or 'quit' to end the chat.")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Bot: Goodbye!")
            break
        response = chat_bot(user_input)
        print('Bot:', response)
