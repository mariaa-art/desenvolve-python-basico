n = int(input("Digite a quantidade de números (n): "))  
maior = 0  

while n > 0:  
    x = float(input("Digite um número: "))  
    if x > maior:  
        maior = x 
    n = n - 1  

print("O maior número é:", maior) 