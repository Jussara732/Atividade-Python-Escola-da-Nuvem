# Média da turma
qtde_alunos = int(input("Digite a quantidade de alunos na turma: "))
soma_notas = 0.0
for i in range(qtde_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / qtde_alunos
print(f"A média da turma é: {media}")