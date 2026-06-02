<p align="center">
  <img src="assets/mailsense-banner.svg" alt="MailSense Banner" width="550" />
</p>

<br />
# MailSense

MailSense è un'applicazione web per l'automazione intelligente della generazione e dell'invio di email, progettata per semplificare le comunicazioni aziendali. Sfrutta l'elaborazione del linguaggio naturale (NLP) per trasformare brevi contesti in email professionali, pronte per essere inviate in modo sicuro tramite un ambiente di test SMTP.

## Panoramica

Il progetto risolve il problema della scrittura ripetitiva di email aziendali, offrendo:
- Generazione istantanea di contenuti email professionali e contestualizzati tramite IA.
- Anteprima in tempo reale nel browser prima dell'invio.
- Consegna sicura e tracciabile tramite ambiente di test (Mailtrap), ideale per demo e sviluppo.
- Interfaccia utente moderna, reattiva e focalizzata sulla produttività.

## Tech Stack

| Componente | Tecnologia |
|------------|------------|
| **Backend** | Python, Flask (Blueprints) |
| **Intelligenza Artificiale** | Groq API (`llama-3.3-70b-versatile`) |
| **Email Delivery** | Mailtrap (Sandbox SMTP) |
| **Frontend** | HTML5, JavaScript (Fetch API), Tailwind CSS |
| **Configurazione** | `python-dotenv` |

## Prerequisiti

Prima di iniziare, assicurati di avere:
- Python 3.10 o superiore installato.
- Un account gratuito su [Groq Console](https://console.groq.com) per ottenere una API Key.
- Un account gratuito su [Mailtrap](https://mailtrap.io) per le credenziali SMTP di test (sezione "Email Testing").

## Installazione e Configurazione

1. **Clona il repository**
   ```bash
   git clone https://github.com/fabio-cerundolo/MailSense.git
   cd MailSense
   ```

2. **Crea e attiva un ambiente virtuale** (consigliato)
   ```bash
   python -m venv .venv
   # Su Linux/macOS:
   source .venv/bin/activate
   # Su Windows:
   .venv\Scripts\activate
   ```

3. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente**
   Crea un file `.env` nella root del progetto copiando il template fornito:
   ```bash
   cp .env.example .env
   ```
   Apri il file `.env` e inserisci le tue credenziali reali:
   ```env
   # Groq AI Configuration
   GROQ_API_KEY=gsk_your_groq_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile

   # Mailtrap SMTP Configuration
   EMAIL_ADDRESS=your_mailtrap_username
   EMAIL_PASSWORD=your_mailtrap_password
   SMTP_SERVER=sandbox.smtp.mailtrap.io
   SMTP_PORT=2525
   SMTP_USE_TLS=True
   SMTP_USE_SSL=False
   ```

5. **Avvia l'applicazione**
   ```bash
   python app.py
   ```
   L'applicazione sarà disponibile all'indirizzo: [http://localhost:5000](http://localhost:5000)

## Struttura del Progetto

```text
MailSense/
├── app/
│   ├── __init__.py
│   ├── ai_email_service.py   # Logica di integrazione con Groq API
│   ├── email_sender.py       # Logica di invio SMTP (Mailtrap)
│   └── routes.py             # Definizione delle route Flask (Blueprints)
├── templates/
│   └── index.html            # Interfaccia utente frontend
├── config.py                 # Caricamento centralizzato delle variabili d'ambiente
├── .env.example              # Template sicuro per le variabili d'ambiente
├── requirements.txt          # Dipendenze Python
└── README.md
```

## Funzionamento del Flusso

1. L'utente compila i campi "Destinatario", "Oggetto" e "Contesto" nell'interfaccia web.
2. Il frontend invia una richiesta `POST` al backend Flask (`/send-email`).
3. Il backend chiama l'API di Groq per generare il corpo dell'email basato sul contesto fornito.
4. Il testo generato viene restituito al frontend per un'anteprima immediata e chiara.
5. Contemporaneamente, il backend tenta di inviare l'email tramite il server SMTP configurato (Mailtrap).
6. L'utente riceve un feedback visivo di successo o di errore dettagliato, mantenendo sempre la visibilità del testo generato.

## Sicurezza e Best Practices

- Le chiavi API e le credenziali SMTP non sono mai committate nel repository, grazie all'uso di `python-dotenv` e al file `.gitignore`.
- Le richieste all'API di Groq includono un timeout configurato per prevenire blocchi del thread del server.
- La gestione degli errori è strutturata per restituire messaggi chiari al frontend senza esporre dettagli sensibili del backend o stack trace.

## Licenza

Questo progetto è distribuito con licenza MIT. Vedere il file `LICENSE` per i dettagli.

## Autore

**Fabio Cerundolo** — Full-Stack Developer

- Portfolio: [fabio-cerundolo.dev](https://fabio-cerundolo.dev)
- GitHub: [@fabio-cerundolo](https://github.com/fabio-cerundolo)
- LinkedIn: [fabio-cerundolo](https://linkedin.com/in/fabio-cerundolo)