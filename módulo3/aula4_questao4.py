distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

if distancia <= 100:
    frete = peso * 1
elif distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

if peso > 10:
    frete += 10

print(f"O valor do frete é: R${frete:.2f}")