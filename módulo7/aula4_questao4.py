import random
import os

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().upper() for linha in f]

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios_forca = list(filter(None, [e.strip() for e in f.read().split("=========")]))

palavra_secreta = random.choice(palavras)
letras_acertadas = ['_'] * len(palavra_secreta)
letras_tentadas = []
erros = 0

while erros < 6 and '_' in letras_acertadas:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- JOGO DA FORCA ---")
    imprime_enforcado(erros, estagios_forca)
    print("\nPalavra: " + " ".join(letras_acertadas))
    print("\nLetras tentadas: " + ", ".join(sorted(letras_tentadas)))

    tentativa = input("Digite uma letra: ").upper()

    if not tentativa.isalpha() or len(tentativa) != 1:
        continue
    if tentativa in letras_tentadas:
        continue
    
    letras_tentadas.append(tentativa)

    if tentativa in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                letras_acertadas[i] = tentativa
    else:
        erros += 1

os.system('cls' if os.name == 'nt' else 'clear')
imprime_enforcado(erros, estagios_forca)

if '_' not in letras_acertadas:
    print(f"\nPARABÉNS! Você venceu! A palavra era: {palavra_secreta}")
else:
    print(f"\nVOCÊ PERDEU! A palavra secreta era: {palavra_secreta}")