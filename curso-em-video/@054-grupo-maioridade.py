from datetime import date
menor = 0
maior = 0
for i in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = date.today().year - nasc
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print(f'Temos {maior} pessoas maiores de idade.')
print(f'Temos {menor} pessoas menores de idade.')
