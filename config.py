import os

import os
from transformers import pipeline
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
SMTP_SERVER='sandbox.smtp.mailtrap.io'
SMTP_PORT= 2525
EMAIL_ADDRESS= 'f79408623a0293'
EMAIL_PASSWORD= '7ee32aa22e6ae9'
SMTP_USE_TLS= True
SMTP_USE_SSL= False
def generate_email_content(context):
    api_key = os.getenv('HUGGINGFACE_API_KEY')  # Assicurati che la chiave sia impostata come variabile d'ambiente
    generator = pipeline("text-generation", model="distilgpt2", use_auth_token=api_key)
    prompt = f"Write a formal email for the following context: {context}"
    result = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)
    return result[0]['generated_text']

# Looking to send emails in production? Check out our Email API/SMTP product!

