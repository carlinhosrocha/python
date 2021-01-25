import random
alunos = []
for i in range(5):
    x = i
    x = x + 1
    aluno = input(f'Digite o nome do {x}° aluno: ')
    alunos.append(aluno)
escolhido = random.choice(alunos)
print(f'O aluno escolhido foi: {escolhido}!')

