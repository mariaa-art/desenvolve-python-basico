import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista Original:", lista)

max_len = 0
max_start_index = -1

current_len = 0
for i, num in enumerate(lista):
    if num < 0:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
            max_start_index = i - current_len
        current_len = 0

if current_len > max_len:
    max_len = current_len
    max_start_index = len(lista) - current_len

if max_start_index != -1:
    start = max_start_index
    end = start + max_len
    del lista[start:end]

print("Lista Editada: ", lista)