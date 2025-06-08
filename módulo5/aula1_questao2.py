import random
import math

n = int(input("Digite a quantidade de valores (n): "))

soma = 0
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz = math.sqrt(soma)

print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz:.2f}")