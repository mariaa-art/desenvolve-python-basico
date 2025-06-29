data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
partes = data_nascimento.split('/')
dia, mes_numero, ano = partes[0], int(partes[1]), partes[2]

meses_por_extenso = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
nome_mes = meses_por_extenso[mes_numero - 1]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")