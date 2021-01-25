nome = ''
idade = 0
sexo = ''
maior = 0
ident = ''
mulher = 0
media = 0
final = 0
for i in range(1, 6):
    print(f'----- {i}° PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade
    if i == 1:
        maior = idade
        ident = nome
    else:
        if (idade > maior) and (sexo == 'm' or sexo == 'M'):
            maior = idade
            ident = nome
        if ((sexo == 'f' or sexo == 'F') and idade < 20):
            mulher += 1
final = media / 5
print(f'A média de idade do grupo é de {final} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {ident}.')
print(f'Ao todo são {mulher} melhur(es) com menos de 20 anos.')
