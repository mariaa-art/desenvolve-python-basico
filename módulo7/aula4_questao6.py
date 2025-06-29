print("--- 5 primeiras linhas do arquivo spotify-2023.csv ---")
with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    for i in range(5):
        print(f.readline().strip())
print("-" * 50)

top_musicas_por_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    next(f) # Pula cabeçalho
    for linha in f:
        if '"' in linha:
            continue
        
        partes = linha.strip().split(',')
        try:
            track_name, artists_name = partes[0], partes[1]
            released_year, streams = int(partes[3]), int(partes[8])
        except (ValueError, IndexError):
            continue

        if 2012 <= released_year <= 2022:
            if released_year not in top_musicas_por_ano or streams > top_musicas_por_ano[released_year][2]:
                top_musicas_por_ano[released_year] = [track_name, artists_name, streams]

resultado_final = []
for ano, dados in sorted(top_musicas_por_ano.items()):
    resultado_final.append([dados[0], dados[1], ano, dados[2]])

print("\n--- Músicas mais tocadas por ano (2012-2022) ---")
for item in resultado_final:
    print(item)