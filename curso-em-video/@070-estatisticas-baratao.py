a = 20
print('{:=^20}'.format(''))
print('{:^20}'.format('LOJA SUPER BARATÃO'))
print('='*a)
cont = maior = soma = 0
while True:
    cont += 1
    nome = str(input('Nome do Produto: '))
    valor = int(input('Preço do Produto: R$'))
    soma += valor
    if valor > 1000:
        maior += 1
    if cont == 1 or valor < menorValor:
        menorValor = valor
        nomeMenor = nome
    flag = ' '
    while flag not in 'NS':
        flag = str(input('Quer cotinuar? [S/N] ')).upper().strip()
    if flag == 'N':
        break
print(f'Total da compra: R${soma:.2f}.')
print(f'Produto(s) que custou mais de R$1000.00: {maior}.')
print(f'Produto mais barato: {nomeMenor}. Valor: R${menorValor:.2f}.')
