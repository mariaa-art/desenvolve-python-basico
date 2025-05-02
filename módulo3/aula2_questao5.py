genero = input("Digite seu gênero (M/F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

a = (genero == "F" and idade >= 60) or (genero == "M" and idade >= 65)
b = tempo_servico >= 30
c = idade >= 60 and tempo_servico >= 25

pode_aposentar = a or b or c
print(pode_aposentar)