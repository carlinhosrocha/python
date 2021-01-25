soma = 0
cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999: # condição de parada (flag)
        break
    else:
        soma = soma + num
        cont += 1
print(f'A soma dos {cont} números digitados é {soma}.')
