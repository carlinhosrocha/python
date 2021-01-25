sexo = ''
while True: #enquanto a condição for verdadeira o laço se repete infinitamente
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]#pega a primeira letra
    if ((sexo == 'M') or (sexo == 'F')):
        break #se a condição for atendida o laço while finda-se
    else:
        print('Opção inválida...')
print(f'Muito bem! O sexo digitado é {sexo}.')
