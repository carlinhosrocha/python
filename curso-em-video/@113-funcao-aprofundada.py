def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n
num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}.')
