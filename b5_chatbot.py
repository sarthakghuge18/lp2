import random

# Define the chatbot function
def chatbot():
    print("Welcome to ShopEasy Bot!")  # Greeting message
    print("Type 'exit' to end the chat.")  # Instruction to end the chat
    
    # Predefined responses for different queries
    greetings = ["Hello!", "Hi there!", "Hey! How can I help you?"]
    delivery_info = ["Deliveries take 3-5 business days.", "Standard delivery time is 3-5 days."]
    return_info = ["You can return a product within 7 days of delivery.", "Returns are accepted within 7 days."]
    refund_info = ["Refunds are processed within 5-7 business days after pickup.", "Refunds take about 5-7 working days."]
    unknown_response = ["I'm not sure I understand. Could you rephrase?", "Sorry, I didn't get that."]

    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase

        # Exit condition
        if user_input == 'exit':
            print("Bot: Thank you for visiting! Have a nice day 😊")
            break  # Exit the loop and end the chat

        # Handle greeting responses
        elif any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            print(f"Bot: {random.choice(greetings)}")
        
        # Handle delivery-related queries
        elif 'delivery' in user_input or 'shipping' in user_input:
            print(f"Bot: {random.choice(delivery_info)}")

        # Handle return or exchange queries
        elif 'return' in user_input or 'exchange' in user_input:
            print(f"Bot: {random.choice(return_info)}")

        # Handle refund-related queries
        elif 'refund' in user_input:
            print(f"Bot: {random.choice(refund_info)}")

        # Handle 'thank you' message
        elif 'thank' in user_input:
            print("Bot: You're welcome! 😊")

        # Handle unknown input (Fallback response)
        else:
            print(f"Bot: {random.choice(unknown_response)}")

# Run the chatbot
chatbot()
