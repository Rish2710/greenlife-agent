import requests
from dotenv import load_dotenv
import os

load_dotenv()
def get_response(product,user_input):
    api_url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
    "messages": [
		{
			"role": "user",
			"content": f"You are a smart chatbot that helps users with product-related queries, such as finding prices, descriptions, adding items to the cart, removing items, and calculating the total price of the cart. Respond dynamically based on user input\n\nContext:{product}\n\nQuery:{user_input}\n\nAssistant:"
		}
	],
    "max_tokens": 2048,
    "temperature": 0.9,
    "top_p": 0.9,
    "stream": False
}
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        botresult = result['choices'][0]['message']['content']
        return botresult
    return "Error contacting API."