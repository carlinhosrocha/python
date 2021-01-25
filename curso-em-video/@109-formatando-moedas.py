from moedas import *
num = float(input('Digite o valor: R$'))
print(f'O dobro de {moeda(num)} é {dobro(num)}.')
print(f'A metade de {moeda(num)} é {metade(num)}.')
print(f'Com 10% de aumento será {aumento(num)}.')