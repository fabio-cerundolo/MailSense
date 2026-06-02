from flask import Blueprint, render_template, request, jsonify
from .ai_email_service import generate_email_content
from .email_sender import send_email as send_email_smtp  # Rinominato per evitare conflitti

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/send-email', methods=['POST'])
def handle_send_email():
    # 1. Ricevi i dati dal frontend
    data = request.get_json()
    if not data:
        return jsonify({"status": "Errore: Nessuna data fornita"}), 400

    recipient = data.get('recipient')
    subject = data.get('subject')
    context = data.get('context')

    if not all([recipient, subject, context]):
        return jsonify({"status": "Errore: Campi obbligatori mancanti"}), 400

    # 2. Genera il contenuto con l'IA
    success, generated_body, error_msg = generate_email_content(context)

    if not success:
        return jsonify({"status": f"Errore IA: {error_msg}"}), 500

    # 3. Invia l'email tramite Mailtrap (se configurato)
    smtp_success = True
    smtp_error = ""
    try:
        # Chiama la funzione di invio che hai già in email_sender.py
        send_email_smtp(recipient, subject, generated_body)
    except Exception as e:
        smtp_success = False
        smtp_error = str(e)

    # 4. Rispondi al frontend
    if smtp_success:
        return jsonify({
            "status": f"Email generata e inviata con successo alla sandbox Mailtrap per {recipient}!",
            "generated_content": generated_body,
            "subject": subject
        }), 200
    else:
        # Restituiamo 200 OK comunque, perché l'IA ha funzionato e il testo è visibile in anteprima nel frontend
        return jsonify({
            "status": f"Email generata con successo, ma errore nell'invio SMTP: {smtp_error}. Il testo è comunque pronto in anteprima.",
            "generated_content": generated_body,
            "subject": subject
        }), 200