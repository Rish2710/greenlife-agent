import streamlit as st
import json
from api_integration import get_response

# Load the products JSON
def load_products(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Load products from JSON
products = load_products("/Users/rishabh/Desktop/greenlife-agent/data/products.json")

# Streamlit app title
st.title("GreenLife Foods Chatbot")

# Function to get user input
def get_user_input():
    return st.text_input("Ask me about GreenLife Foods products:", key="input_box")

# Function to display the conversation history
def display_conversation(conversation_history):
    if conversation_history:
        st.markdown("---")  # Separator line
        for user_query, bot_reply in reversed(conversation_history):
            st.markdown(f"**You:** {user_query}")
            st.markdown(f"**Chatbot:** {bot_reply}")

# Main function
def main():
    st.write("Welcome to GreenLife Foods Chatbot! Ask about our products.")
    conversation_history = st.session_state.get("conversation_history", [])  # Retrieve or initialize history

    user_input = get_user_input()

    if user_input:
        bot_response = get_response(products, user_input)
        
        conversation_history.append((user_input, bot_response))  # Store the conversation
        st.session_state["conversation_history"] = conversation_history  # Save history to session
        display_conversation(conversation_history)  # Display the conversation history

if __name__ == "__main__":
    main()
