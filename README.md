# GreenLife Foods Chatbot

## Overview
This chatbot provides an AI-driven solution for GreenLife Foods to streamline the order capture process for distributors and retailers. The chatbot answers product-related inquiries using Qwen2.5-72B-Instruct, integrated via the Huggingface Qwen2.5-72B-Instruct Inference API.

## Requirements
- Python 3.x
- Huggingface API Key

## Setup Instructions
1. Clone the repository using `git clone <repository url>` command.
2. Create the virtual environment.
   `python3 -m venv venv`
3. Activate your virtual environment.
4. Install required packages by running the requirements.txt file using the below command.
   `pip3 install -r requirements.txt`
5. Once all the dependencies are installed.
6. Create a `.env` file and add the huggingface API key to access the Inference endpoints.
   ```
   HUGGINGFACE_API_KEY=hf_JHMhpwGRamZVqQnZOpXnGiP
   ```
   Add this above line with your API key in the `.env` file.
7. Once above steps are done go to the folder location in your terminal where we have the `app.py` file, so here we have it in `/src` folder.
8. Once we have reached the folder location, now we are ready to run our streamlit app and interact with the chatbot.
9. Run this below command.
    `streamlit run app.py`
10. It will open the browser with UI interface to interact.
