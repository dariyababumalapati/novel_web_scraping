import os 
import openai
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


with open('ch_text.txt', 'r', encoding='utf-8') as f:
   ch_text = f.read()



chat_completion = client.chat.completions.create(
    messages=[f"Translate the following Chinese text to English, {ch_text}"],
    model="gpt-3.5-turbo",
)

# Output the generated text
generated_text = chat_completion.choices[0].message['content'].strip()

with open('en_text.txt', 'w', encoding='utf-8') as f:
   f.write(generated_text)

print(generated_text)
