from flask import Blueprint, render_template, request, jsonify
from .ai_email_service import generate_email_content
from .email_sender import send_email

# Crea un Blueprint per le rotte
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    content = generate_email_content(data.get('context'))
    send_email(recipient, subject, content)
    return jsonify({"status": "Email inviata con successo"})
