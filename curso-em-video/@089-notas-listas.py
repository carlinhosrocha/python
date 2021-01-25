total = []
notas = []
while True:
    n = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2 # media das notas
    notas.append(n) # armazena o nome do aluno na lista
    notas.append(n1) # armazena primeira nota na lista
    notas.append(n2) # armazena segunda nota na lista
    notas.append(media) # armazena media das notas na lista
    total.append(notas[:]) # guarda o primeiro cadastro na lista final (cópia)
    notas.clear() # limpa dados da lista
    out = str(input('Quer continuar?[S/N]: '))
    if out in 'Nn':
        break
print('='*30)
print('N.   Nome    Média')
for i in range(0, len(total)):
    print(f'{i}  -  {total[i][0]}  -  {total[i][3]}')
print('='*30)
while True:
    al = int(input('Qual aluno você deseja vizualizar? [999 para sair]: '))
    if al == 999:
        break
    else:
        print(f'{total[al][0]} - [{total[al][1]}, {total[al][2]}]')
print('Programa FINALIZADO...\n<<< Volte Sempre  >>>')