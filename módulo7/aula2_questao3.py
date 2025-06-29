while True:
    frase_original = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase_original.lower().strip() == "fim":
        break

    frase_limpa = "".join(char for char in frase_original if char.isalnum()).lower()
    
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase_original}" é palíndromo\n')
    else:
        print(f'"{frase_original}" não é palíndromo\n')