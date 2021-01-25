maior = menor = cont = soma = 0 # declaração das variáveis
while True: # laço de repetição infinito 
    num = int(input('Digite um número: '))
    soma = soma + num
    if maior == 0:
        maior = num
    if menor == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    sair = str(input('Quer continuar? [S/N]: ')).strip()[0] # retira os espaços e considera 1° letra
    if sair in 'Nn': # se valor sair está na lista
        break # condição de parada do laço (flag)
media = soma / cont
print(f'Você digitou {cont} digitos e a média foi de {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
