casa = int(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
ano = int(input('Em quanto tempo você quer pagar o financiamento? '))
parcela = casa / (ano * 12)
print(f'O valor da casa é R${casa:.2f} e da parcela será de R${parcela:.2f} em {ano} anos.')
if((sal * 0.30) > parcela):
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')
