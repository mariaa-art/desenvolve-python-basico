import random
numero_secreto = random.randint(1, 10)

print("Jogo de Adivinhação - Número entre 1 e 10")

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print(f"Correto! O número é {numero_secreto}.")
        break
    elif palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    else:
        print("Muito alto, tente novamente!")