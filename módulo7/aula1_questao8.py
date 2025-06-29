cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

cpf_numeros = cpf_usuario.replace('.', '').replace('-', '')

if len(cpf_numeros) != 11 or len(set(cpf_numeros)) == 1:
    print("Inválido")
else:
    nove_digitos = cpf_numeros[:9]
    soma1 = sum(int(digito) * (10 - i) for i, digito in enumerate(nove_digitos))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    dez_digitos = nove_digitos + str(digito1)
    soma2 = sum(int(digito) * (11 - i) for i, digito in enumerate(dez_digitos))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    
    if cpf_numeros[9:] == f"{digito1}{digito2}":
        print("Válido")
    else:
        print("Inválido")