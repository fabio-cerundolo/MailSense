import requests
import os
from config import GROQ_API_KEY, GROQ_URL, GROQ_MODEL


def generate_email_content(context: str):
    """
    Genera il corpo dell'email usando Groq (Llama 3.3 70B).
    Ritorna: (successo: bool, contenuto: str | None, errore: str | None)
    """
    if not GROQ_API_KEY:
        return False, None, "API key Groq non configurata. Verifica il file .env"

    prompt = (
        "Agisci come un assistente professionale per la scrittura di email aziendali in italiano. "
        "Il tuo compito è scrivere SOLO il corpo dell'email, senza saluti iniziali o finali generici "
        "e senza aggiungere spiegazioni, premesse o commenti.\n\n"
        f"Contesto fornito dall'utente: {context}"
    )

    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": GROQ_MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 512
            },
            timeout=30  # Groq è velocissimo, 30s sono più che sufficienti
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"].strip()
        
        if not content:
            return False, None, "L'IA ha restituito una risposta vuota."
            
        return True, content, None

    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return False, None, "API key Groq non valida."
        elif response.status_code == 429:
            return False, None, "Limite di richieste raggiunto. Riprova tra qualche secondo."
        return False, None, f"Errore API: {response.status_code}"
    except requests.exceptions.Timeout:
        return False, None, "La generazione ha impiegato troppo tempo."
    except Exception as e:
        return False, None, f"Errore imprevisto: {str(e)}"