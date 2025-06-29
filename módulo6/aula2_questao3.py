import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

set1 = set(lista1)
set2 = set(lista2)

interseccao_set = set1 & set2
interseccao = list(interseccao_set)
interseccao.sort()

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print("Interseccao:", interseccao)

print("Contagem")
for elemento in interseccao:
    contagem_lista1 = lista1.count(elemento)
    contagem_lista2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={contagem_lista1}, lista2={contagem_lista2})")