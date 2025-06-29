frase_original = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ""
for letra in frase_original:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra
print(f"Frase modificada: {frase_modificada}")