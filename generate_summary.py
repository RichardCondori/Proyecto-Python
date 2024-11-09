import openai
import sys
import os

# Obtén la clave de API de OpenAI desde la variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(diff_text):
    prompt = f"Summarize the following changes in Python code:\n{diff_text}"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Lee el archivo de diferencias pasado como argumento
    with open(sys.argv[1], 'r') as f:
        diff_text = f.read()
    summary = generate_summary(diff_text)
    print(summary)
