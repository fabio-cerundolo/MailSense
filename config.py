import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'sandbox.smtp.mailtrap.io')
SMTP_PORT = int(os.getenv('SMTP_PORT', 2525))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_USE_TLS = os.getenv('SMTP_USE_TLS', 'True') == 'True'
SMTP_USE_SSL = os.getenv('SMTP_USE_SSL', 'False') == 'True'

