import smtplib
from email.mime.text import MIMEText
from flask import current_app

def send_email(recipient, subject, content):
    smtp_server = current_app.config['SMTP_SERVER']
    smtp_port = current_app.config['SMTP_PORT']
    sender_email = current_app.config['EMAIL_ADDRESS']
    password = current_app.config['EMAIL_PASSWORD']
    
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())
