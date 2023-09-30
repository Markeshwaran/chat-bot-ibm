
import openai

# Define your OpenAI API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to generate a response from the chatbot
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can also use "curie" or other engines if available.
        prompt=prompt,
        max_tokens=50  # Adjust the max_tokens as needed for the desired response length.
    )
    return response.choices[0].text

# Main chat loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    prompt = f"You: {user_input}\nChatbot:"
    response = generate_response(prompt)
    print(response)