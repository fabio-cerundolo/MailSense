# MailSense

> AI-powered email generation and delivery platform — generate, send and monitor personalized email campaigns with a local LLM.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-distilgpt2-FFD21E?logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Indice

1. [Panoramica](#1-panoramica)
2. [Stack Tecnologico](#2-stack-tecnologico)
3. [Architettura](#3-architettura)
4. [Struttura del Repository](#4-struttura-del-repository)
5. [Prerequisiti](#5-prerequisiti)
6. [Installazione e Avvio](#6-installazione-e-avvio)
7. [Configurazione Variabili d'Ambiente](#7-configurazione-variabili-dambiente)
8. [API Reference](#8-api-reference)
9. [Flusso di Generazione Email](#9-flusso-di-generazione-email)
10. [Roadmap](#10-roadmap)
11. [Sicurezza e Note per la Produzione](#11-sicurezza-e-note-per-la-produzione)

---

## 1. Panoramica

**MailSense** è una web application che combina un backend Flask con un modello linguistico locale (distilgpt2 via HuggingFace Transformers) per generare automaticamente contenuti email personalizzati a partire da un contesto testuale fornito dall'utente.

Il sistema permette di:

- **Generare contenuti email** tramite LLM locale (nessuna chiamata a API esterne a pagamento)
- **Inviare email** via SMTP con supporto TLS
- **Testare i flussi email** in locale tramite Mailtrap senza inviare messaggi reali
- **Interfacciarsi** tramite una UI web minimale o direttamente via API REST

---

## 2. Stack Tecnologico

| Layer | Tecnologia | Note |
|---|---|---|
| Backend | Python + Flask | Blueprint per routing modulare |
| AI / LLM | HuggingFace Transformers — distilgpt2 | Inference locale, no API key richiesta |
| Email Testing | Mailtrap SMTP Sandbox | Nessuna email reale inviata in dev |
| Frontend | HTML + Jinja2 | Template Flask |
| Config | python-dotenv | Variabili d'ambiente da file `.env` |

**Linguaggi nel repository:**

- Python — ~90%
- HTML — ~10%

---

## 3. Architettura

```
┌─────────────────┐       ┌──────────────────────┐
│   Browser       │──────▶│   Flask App          │
│  (index.html)   │       │   app.py / routes.py │
└─────────────────┘       └────────┬─────────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  │                │                │
                  ▼                ▼                ▼
     ┌────────────────┐  ┌─────────────────┐  ┌──────────────┐
     │ ai_email_      │  │  email_sender   │  │  config.py   │
     │ service.py     │  │  .py            │  │  (.env)      │
     │                │  │                 │  └──────────────┘
     │ distilgpt2     │  │  SMTP / TLS     │
     │ HuggingFace    │  │  Mailtrap       │
     └────────────────┘  └─────────────────┘
```

**Flusso dati:**

```
Utente → Frontend (form contesto + destinatario)
       → POST /send-email
       → generate_email_content(context)   [distilgpt2 locale]
       → send_email(recipient, subject, content)  [SMTP Mailtrap]
       ← Risposta JSON {"status": "Email inviata con successo"}
```

---

## 4. Struttura del Repository

```
MailSense/
│
├── app/
│   ├── __init__.py           # Factory function create_app()
│   ├── ai_email_service.py   # Generazione contenuto via distilgpt2
│   ├── email_sender.py       # Invio email via SMTP
│   └── routes.py             # Blueprint Flask con gli endpoint
│
├── templates/
│   └── index.html            # UI web principale
│
├── app.py                    # Entry point — avvia Flask
├── config.py                 # Configurazione da variabili d'ambiente
├── requirements.txt          # Dipendenze Python
├── .env.example              # Template variabili d'ambiente
├── .gitignore
└── LICENSE
```

---

## 5. Prerequisiti

- Python >= 3.10
- pip
- Git

> Il modello distilgpt2 viene scaricato automaticamente da HuggingFace al primo avvio (~350MB). Nessuna API key richiesta per l'inference locale.

---

## 6. Installazione e Avvio

```bash
# 1. Clona il repository
git clone https://github.com/fabio-cerundolo/MailSense.git
cd MailSense

# 2. Crea e attiva il virtual environment
python -m venv .venv

# Linux / macOS (bash)
source .venv/bin/activate

# Fish shell
source .venv/bin/activate.fish

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Configura le variabili d'ambiente
cp .env.example .env
# Modifica .env con le tue credenziali SMTP

# 5. Avvia l'applicazione
python app.py
```

L'applicazione sarà disponibile su `http://localhost:5000`.

> **Nota:** Al primo avvio, HuggingFace scaricherà il modello distilgpt2 (~350MB). I successivi avvii saranno immediati grazie alla cache locale.

---

## 7. Configurazione Variabili d'Ambiente

Copia `.env.example` in `.env` e compila i valori:

| Variabile | Default | Descrizione |
|---|---|---|
| `SMTP_SERVER` | `sandbox.smtp.mailtrap.io` | Host SMTP |
| `SMTP_PORT` | `2525` | Porta SMTP |
| `EMAIL_ADDRESS` | — | Username SMTP |
| `EMAIL_PASSWORD` | — | Password SMTP |
| `SMTP_USE_TLS` | `True` | Abilita STARTTLS |
| `SMTP_USE_SSL` | `False` | Abilita SSL diretto |
| `HUGGINGFACE_API_KEY` | — | Opzionale — solo per modelli privati HF |

> Per usare un provider SMTP reale in produzione (Gmail, SendGrid, SES) è sufficiente aggiornare le variabili SMTP nel file `.env`.

---

## 8. API Reference

### `GET /`
Restituisce la UI web principale (`index.html`).

---

### `POST /send-email`

Genera il contenuto dell'email tramite AI e la invia al destinatario.

**Request body (JSON):**

```json
{
  "recipient": "destinatario@esempio.com",
  "subject": "Oggetto dell'email",
  "context": "Scrivi un'email di follow-up per un cliente interessato al nostro prodotto SaaS."
}
```

**Response:**

```json
{
  "status": "Email inviata con successo"
}
```

**Esempio con curl:**

```bash
curl -X POST http://localhost:5000/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "recipient": "test@esempio.com",
    "subject": "Follow-up",
    "context": "Email di follow-up per cliente interessato al prodotto SaaS."
  }'
```

---

## 9. Flusso di Generazione Email

```
1. L'utente invia il contesto via form o API
        │
        ▼
2. Flask (routes.py) riceve la richiesta POST /send-email
        │
        ▼
3. ai_email_service.py genera il contenuto
   - Carica distilgpt2 via HuggingFace Transformers (cache locale)
   - Costruisce il prompt: "Scrivi una email formale per: {context}"
   - Genera il testo con temperature=0.7, max_new_tokens=1500
        │
        ▼
4. email_sender.py invia l'email
   - Connessione SMTP con STARTTLS
   - Login con credenziali da .env
   - Invio tramite Mailtrap (dev) o SMTP reale (prod)
        │
        ▼
5. Risposta JSON al client
```

---

## 10. Roadmap

- [ ] Aggiungere supporto per modelli HuggingFace alternativi (es. GPT-2 medium, Mistral)
- [ ] Implementare A/B testing sui contenuti generati
- [ ] Aggiungere dashboard per monitoraggio metriche (open rate, click rate)
- [ ] Supporto multilingua nella generazione
- [ ] Containerizzazione con Docker Compose
- [ ] Autenticazione utenti con JWT

---

## 11. Sicurezza e Note per la Produzione

> Questo progetto è pensato come ambiente dimostrativo. Prima di un deployment in produzione:

1. **Non committare mai `.env`** — è già in `.gitignore`
2. **Usare un provider SMTP reale** — sostituire Mailtrap con Gmail, SendGrid o AWS SES
3. **Disabilitare `debug=True`** in `app.py`
4. **Aggiungere autenticazione** agli endpoint API
5. **Configurare HTTPS** tramite reverse proxy (Nginx + Let's Encrypt)
6. **Valutare modelli LLM più potenti** per produzione (es. via API OpenAI o modelli locali Mistral/LLaMA)

---

*MailSense — AI-powered email generation · [fabio-cerundolo](https://github.com/fabio-cerundolo)*