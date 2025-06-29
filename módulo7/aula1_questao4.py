numero = input("Digite o número: ")

if len(numero) == 8:
    numero_completo = '9' + numero
    numero_formatado = f"{numero_completo[:5]}-{numero_completo[5:]}"
    print(f"Número completo: {numero_formatado}")
elif len(numero) == 9:
    if numero[0] == '9':
        numero_formatado = f"{numero[:5]}-{numero[5:]}"
        print(f"Número completo: {numero_formatado}")
    else:
        print("Número de 9 dígitos inválido (não começa com 9).")
else:
    print("Número com quantidade de dígitos inválida.")