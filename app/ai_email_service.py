import requests

def generate_email_content(context):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "mistral",
                "prompt": f"Scrivi una email formale e professionale per il seguente contesto: {context}. Scrivi solo il corpo dell'email, senza aggiungere spiegazioni.",
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json().get('response', '').strip()
    except requests.exceptions.ConnectionError:
        print("Errore: Ollama non è in esecuzione. Avvia con: ollama serve")
        return None
    except Exception as e:
        print(f"Errore durante la generazione: {e}")
        return None