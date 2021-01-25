print('-'*20)
print('---- ASCII TABLE ---')
print('-'*20)
print()
while True:
    print('-'*28)
    print('---------   MENU  ----------')
    print('- [1] for Code -> Caracter..')
    print('- [2] for Caracter -> Code..')
    print('- [3] All Ancii Table.......')
    print('- [0] Leave program.........')
    print('-'*28)
    choose = int(input('Choose a opition: '))
    if choose == 1:
        code = int(input('Enter with a code between 0 and 123: '))
        caracter = chr(code)
        print('='*40)
        print(f'The code {code} has following equivalent: {caracter}.')
        print('='*40)
    elif choose == 2:
        caracter = input('Enter with a caracter: ')
        code = ord(caracter)
        print('='*40)
        print(f'The caracter {caracter} has following equivalent: {code}.')
        print('='*40)
    elif choose == 3:
        for x in range(123):
            print(x, '->', chr(x))
    elif choose == 0:
        break
    elif choose not in range(5):
        print('Error...')
