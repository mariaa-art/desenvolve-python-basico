import random

def encrypt(lista_strings):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in lista_strings:
        nome_cripto = ""
        for char in nome:
            valor_novo = ord(char) + chave
            nome_cripto += chr(valor_novo)
        nomes_criptografados.append(nome_cripto)
        
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_usada = encrypt(nomes)

print(f"Nomes originais: {nomes}")
print(f"Chave de criptografia: {chave_usada}")
print(f"Nomes criptografados: {nomes_cript}")