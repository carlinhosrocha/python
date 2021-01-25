a = 20
maior = homem = mulher = 0
while True:
    print('='*a)
    print('CADASTRO DE PESSOA')
    print('-'*a)
    idade = int(input('Digite a IDADE: '))
    sexo = str(input('Digite o SEXO: [M/F]')).upper().strip()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    flag = str(input('Quer continuar? [S/N] ')).strip().upper()
    if flag == 'N':
        break
    elif flag == 'S':
        continue
    else:
        print('Opção inválida...')
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Total de homens cadastrados: {homem}.')
print(f'Total de mulheres com menos de 20 anos: {mulher}.')
