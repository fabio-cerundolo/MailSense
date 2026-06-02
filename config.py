import os

import os
from transformers import pipeline
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 2525))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
SMTP_USE_TLS= True
SMTP_USE_SSL= False
def generate_email_content(context):
    api_key = os.getenv('HUGGINGFACE_API_KEY')  # Assicurati che la chiave sia impostata come variabile d'ambiente
    generator = pipeline("text-generation", model="distilgpt2", use_auth_token=api_key)
    prompt = f"Write a formal email for the following context: {context}"
    result = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)
    return result[0]['generated_text']

# Looking to send emails in production? Check out our Email API/SMTP product!

