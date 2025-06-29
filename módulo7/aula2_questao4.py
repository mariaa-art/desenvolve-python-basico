def validador_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))