try:
    from emoji import emojize
except ImportError:
    print("\nERRO: Biblioteca 'emoji' não instalada!")
    print("Execute no terminal/cmd: pip install emoji")
    exit()

emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍", 
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:")
for codigo, simbolo in emojis.items():
    print(f"- {codigo} - {simbolo}")

frase = input("\nDigite uma frase com códigos de emoji (ex: :red_heart:): ")

for codigo, simbolo in emojis.items():
    frase = frase.replace(codigo, simbolo)

print("\nFrase com emojis:")
print(frase)