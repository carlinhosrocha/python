while True: # laço infinito
    print('='*25)
    tab = int(input('Digite qual tabuada: '))
    if tab < 0:
        break # flag de parada
    for i in range(1, 11):
        print(f'{tab} x {i} = {tab * i}')
print('Programa encerrado com sucesso...')
