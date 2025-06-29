frase = input("Digite uma frase: ")

vogais_str = "aeiou"
vogais = sorted([letra for letra in frase if letra.lower() in vogais_str])
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in vogais_str]

print("Vogais:", vogais)
print("Consoantes:", consoantes)