import random

lista_original = []
for _ in range(20):
    numero_aleatorio = random.randint(-100, 100)
    lista_original.append(numero_aleatorio)

lista_ordenada = sorted(lista_original)
print("A lista ordenada:", lista_ordenada)

print("A lista original:", lista_original)

maior_valor = max(lista_original)
indice_maior = lista_original.index(maior_valor)
print(f"O índice do maior valor ({maior_valor}) é:", indice_maior)

menor_valor = min(lista_original)
indice_menor = lista_original.index(menor_valor)
print(f"O índice do menor valor ({menor_valor}) é:", indice_menor)