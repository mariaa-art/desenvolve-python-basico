qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))

print(f"Digite os {qtd1} elementos da lista 1:")
lista1 = []

for _ in range(qtd1):
    elemento = int(input()) 
    lista1.append(elemento) 

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd2} elementos da lista 2:")
lista2 = []
for _ in range(qtd2):
    elemento = int(input())
    lista2.append(elemento)

lista_intercalada = []

tamanho_menor_lista = min(len(lista1), len(lista2))

for i in range(tamanho_menor_lista):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[tamanho_menor_lista:])
else:
    lista_intercalada.extend(lista2[tamanho_menor_lista:])
print("\nLista intercalada:", *lista_intercalada)