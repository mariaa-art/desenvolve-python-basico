frase = input("Digite uma frase: ")
vogais_str = "aeiou"
indices_vogais = []

for indice, letra in enumerate(frase):
    if letra.lower() in vogais_str:
        indices_vogais.append(indice)

print(f"{len(indices_vogais)} vogais")
print(f"Índices {indices_vogais}")