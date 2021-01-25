from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print(f'Quem nasceu em {nasc} terá {idade} anos em {ano}.')
if idade == 18:
    print('Você deve alistar-se IMEDIATAMENTE!')
elif idade < 18:
    print(f'Você ainda não tem 18 anos. Faltam {(18-idade)} anos para alistamento.')
else:
    print(f'Você já deveria ter se alistado {idade-18} anos atrás.')
    print(f'Seu alistamento foi em {ano-(idade-18)}.')
