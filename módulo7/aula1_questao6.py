frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

assinatura_objetivo = sorted(palavra_objetivo.lower())
palavras_na_frase = frase.split()
lista_anagramas = []

for palavra in palavras_na_frase:
    if sorted(palavra.lower()) == assinatura_objetivo:
        lista_anagramas.append(palavra)

print(f"Anagramas: {lista_anagramas}")