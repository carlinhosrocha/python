from time import sleep
numUm = int(input('Primeiro número: '))
numDois = int(input('Segundo número: '))
sleep(1)
while True:
    print('='*20)
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('='*20)
    escolha = int(input('Qual é sua escolha? '))
    sleep(1)
    if escolha == 1:
        soma = numUm + numDois
        print(f'A soma dos números digitados é {soma}.')
        sleep(1)
    elif escolha == 2:
        multi = numUm * numDois
        print(f'A multiplicação dos números digitados é {multi}.')
        sleep(1)
    elif escolha == 3:
        if numUm == numDois:
            print('Os números digitados são iguais!')
        else:
            maior = numUm
            if maior < numDois:
                maior = numDois
            print(f'O maior número é {maior}.')
        sleep(1)
    elif escolha == 4:
        numUm = int(input('Primeiro número: '))
        numDois = int(input('Segundo número: '))
        continue
    elif escolha == 5:
        print('Finalizando programa...')
        sleep(1)
        break
    else:
        print('Opção digitada inválida... tente novamente')
        sleep(1)
        continue
print('Programa finalizado com sucesso! Volte sempre! :) ')
