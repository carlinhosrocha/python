lista = [] # lista inicialmente vazia
out = 0 # flag de saída
while out != 1: # a condição do laço é inicialmente verdadeira 
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num) # método que insere valores na lista
        print('Valor adicionado com sucesso...')
    else:
        print('O valor está duplicado. Não será adicionado...')
    sair = ' '
    # checa se a opção de saída está correta
    while sair not in "NS":
        sair = input('Quer continuar? [S/N]: ').upper()
        if sair == 'N':
            out = 1 # altera o valor da variável, logo o laço externo se torna falso
        elif sair == 'S':
            continue
        else:
            print('Opção inválida...')
lista.sort() # método que organiza a lista em ordem crescente
print(f'Você digitou os seguintes valores: {lista}.')
