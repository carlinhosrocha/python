valor = float(input('Digite o valor a ser dado o desconto: R$'))
taxa = float(input('Agora digite a taxa do desconto: %'))
novo = valor - (valor * (taxa/100))
print(f'Um produto de R${valor:.2f} à uma taxa de desconto de {taxa}% custará R${novo:.2f}.')
