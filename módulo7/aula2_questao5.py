import random

def embaralhar_palavras(frase):
    palavras = frase.split(' ')
    nova_frase_lista = []
    for palavra in palavras:
        if len(palavra) <= 3:
            nova_frase_lista.append(palavra)
        else:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
            nova_frase_lista.append(nova_palavra)
    return " ".join(nova_frase_lista)

# Exemplo de uso:
frase = "Python é uma linguagem de programação poderosa"
resultado = embaralhar_palavras(frase)
print(resultado)