from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from flask import current_app

def initialize_generator():
    # Inizializza tokenizer e model
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")

    # Configura correttamente i token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id

    # Crea il pipeline usando solo max_new_tokens
    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        pad_token_id=tokenizer.pad_token_id
    )

# Inizializza il generatore una volta sola
generator = initialize_generator()

def generate_email_content(context):
    try:
        prompt = f"Scrivi una email formale per il seguente contesto: {context}"
        result = generator(
            prompt,
            max_new_tokens=1500,  # Usiamo solo max_new_tokens
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            no_repeat_ngram_size=2
        )
        return result[0]['generated_text']
    except Exception as e:
        print(f"Errore durante la generazione: {e}")
        return None