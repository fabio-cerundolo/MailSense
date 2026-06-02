import os
from dotenv import load_dotenv

load_dotenv()

# Configurazione Groq (legge dal file .env)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
SMTP_SERVER = os.getenv('SMTP_SERVER', 'sandbox.smtp.mailtrap.io')
SMTP_PORT = int(os.getenv('SMTP_PORT', 2525))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_USE_TLS = os.getenv('SMTP_USE_TLS', 'True') == 'True'
SMTP_USE_SSL = os.getenv('SMTP_USE_SSL', 'False') == 'True'

