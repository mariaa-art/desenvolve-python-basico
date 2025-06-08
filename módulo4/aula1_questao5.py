def calcular_media_idades():
    n = int(input("Quantidade de respondentes: "))
    
    while n <= 0:
        print("O número deve ser positivo!")
        n = int(input("Digite novamente a quantidade de respondentes: "))
    
    soma = 0
    
    for i in range(1, n+1):
        idade = int(input(f"Idade do respondente {i}: "))
        soma += idade
    
    media = soma / n
    print(f"\nMédia de idade: {media:.2f} anos")

calcular_media_idades()