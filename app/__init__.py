from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Carica le variabili dal file .env
    load_dotenv()

    # Aggiungi una stampa per verificare che l’ambiente sia caricato correttamente
    print("HUGGINGFACE_API_KEY:", os.getenv("HUGGINGFACE_API_KEY"))

    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('../config.py')  # Carica il file config.py
    
    with app.app_context():
        from .routes import routes
        app.register_blueprint(routes)

    return app
