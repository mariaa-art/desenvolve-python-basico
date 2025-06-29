import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista elementos:", elementos)

soma_valores = sum(elementos)
print("A soma dos valores da lista é:", soma_valores)

media_valores = soma_valores / len(elementos)
print(f"A média dos valores da lista é: {media_valores:.2f}")