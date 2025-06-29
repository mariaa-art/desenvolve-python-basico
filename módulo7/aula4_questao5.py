livros = [
    ["Título", "Autor", "Ano de publicação", "Número de páginas"],
    ["O Hobbit", "J.R.R. Tolkien", "1937", "310"],
    ["O Guia do Mochileiro das Galáxias", "Douglas Adams", "1979", "208"],
    ["Eu, Robô", "Isaac Asimov", "1950", "320"],
    ["A Guerra dos Tronos", "George R. R. Martin", "1996", "694"],
    ["Duna", "Frank Herbert", "1965", "688"],
    ["1984", "George Orwell", "1949", "328"],
    ["Fahrenheit 451", "Ray Bradbury", "1953", "214"],
    ["O Nome do Vento", "Patrick Rothfuss", "2007", "662"],
    ["Neuromancer", "William Gibson", "1984", "320"],
    ["Fundação", "Isaac Asimov", "1951", "256"]
]

with open("meus_livros.csv", "w", encoding="utf-8", newline='') as f:
    for linha_livro in livros:
        f.write(",".join(map(str, linha_livro)) + "\n")

print("Arquivo 'meus_livros.csv' foi criado com sucesso!")