with open("frase.txt", "r", encoding="utf-8") as f_in:
    conteudo = f_in.read()

palavras_limpas = []
for palavra in conteudo.split():
    palavra_filtrada = "".join(letra for letra in palavra if letra.isalpha())
    if palavra_filtrada:
        palavras_limpas.append(palavra_filtrada)

with open("palavras.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(palavras_limpas))

print("Conteúdo do arquivo 'palavras.txt':")
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())