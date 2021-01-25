cont = 0
soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i:2}° número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números inteiros pares, cuja soma é igual a {soma}.')
