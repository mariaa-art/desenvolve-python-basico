# aula3_questao1.py
numeros = []

while len(numeros) < 4:
    numeros = []
    print("\nDigite pelo menos 4 números inteiros. Pressione Enter sem digitar nada para finalizar.")
    
    while True:
        entrada = input(f"Digite o {len(numeros) + 1}º número (ou Enter para parar): ")
        if entrada == "":
            break
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if len(numeros) < 4:
        print(f"Você digitou apenas {len(numeros)} número(s). É necessário no mínimo 4.")

print("\n--- Resultados ---")
print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])