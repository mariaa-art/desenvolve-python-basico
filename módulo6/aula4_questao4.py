alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [aluno for aluno, nota in zip(alunos, notas) if nota >= 60]

print(aprovados)