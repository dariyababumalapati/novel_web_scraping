from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Example usage:
text_to_translate = input("text: ")
translated_text = translate_text(text_to_translate, target_language='en')  # Translate to Spanish
print("Translated text:", translated_text)
