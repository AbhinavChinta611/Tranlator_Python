from translate import Translator
translator = Translator(to_lang = "Hindi") #change language here to translate
s = str(input("Enter string to translate : "))
translation = translator.translate(s)
print()
print(translation)
