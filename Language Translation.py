from translate import Translator

translator = Translator(from_lang='en', to_lang='fr')  # from English to japanese


text = 'Hello'

translation = translator.translate(text)

print(f'Text: {text}')
print(f'Translation: {translation}')