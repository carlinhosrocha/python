sal = float(input('Digite seu salário: R$'))
novo = sal + (sal * 0.15) if (sal <= 1250) else sal + (sal * 0.10)
print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo:.2f}.')
