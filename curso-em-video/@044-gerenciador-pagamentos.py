print('{:=^40}'.format(' LOJAS CARLOS '))#^centraliza em 40 espaços
compra = float(input('Digite o valor das compras: R$'))
print('='*40)
print('[1] para à vista no dinheiro/cheque    =')
print('[2] para à vista no cartão             =')
print('[3] para 2x no cartão                  =')
print('[4] para 3x ou mais no cartão          =')
print('='*40)
opcao = int(input('Digite a forma de pagamento: '))
if opcao == 1:
    preco = compra - (compra * 0.10) #10% de desconto
    print(f'Com 10% de desconto você pagará R${preco:.2f}.')
elif opcao == 2:
    preco = compra - (compra * 0.05)
    print(f'Você pagará R${preco:.2f} com 5% de desconto.')
elif opcao == 3:
    parcela = compra / 2
    print(f'Você pagará 2 (duas) parcelas sem juros de R${parcela:.2f}.')
elif opcao == 4:
    par = int(input('Digite em quantas parcelas você quer pagar: '))
    parcela = (compra + (compra * 0.20)) / par
    print(f'Você pagará {par} parcelas de R${parcela:.2f} com 20% de juros.')
else:
    print('Opção inválida de pagamento... tente novamente!')
