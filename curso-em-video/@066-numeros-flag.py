soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break # flag para interromper o laço
    else:
        soma = soma + num
        cont += 1
print(f'Você digitou {cont} valor(es) e a soma entre eles é de {soma}.')
