import re

with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print("--- Primeiras 25 linhas ---")
for linha in linhas[:25]:
    print(linha.strip())
print("-" * 30)

print(f"Número de linhas do arquivo: {len(linhas)}")
print("-" * 30)

linha_mais_longa = max(linhas, key=len)
print("Linha com maior número de caracteres:")
print(linha_mais_longa.strip())
print("-" * 30)

texto_completo = "".join(linhas)
mencoes_nonato = len(re.findall(r'\bNonato\b', texto_completo, re.IGNORECASE))
mencoes_iria = len(re.findall(r'\bÍria\b', texto_completo, re.IGNORECASE))

print(f"Número de menções a 'Nonato': {mencoes_nonato}")
print(f"Número de menções a 'Íria': {mencoes_iria}")