pares_20_a_50 = [num for num in range(20, 51, 2)]
print("Números pares entre 20 e 50:", pares_20_a_50)

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [num ** 2 for num in lista_original]
print("Quadrados de 1 a 9:", quadrados)

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números de 1 a 100 divisíveis por 7:", divisiveis_por_7)

par_ou_impar = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("Paridade para range(0, 30, 3):", par_ou_impar)