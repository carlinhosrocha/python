x = 22
print('='*x)
print('Sequência de Fibonacci')
print('='*x)
num = int(input('Quantos termos você quer mostrar? '))
i = 3 # variável contadora inicia-se a partir do terceiro termo
a = 0 # termo a
b = 1 # termo b
print(f'{a} - ', end='')
print(f'{b} ', end='')
while i <= num: # laço de repetição 
    fibo = a + b # próximo termo é sempre a soma dos dois anteriores
    print(f' - {fibo}', end='') # mostra na tela a sequência
    a = b # o termo a passa a ser o b
    b = fibo # o termo b recebe o valor de fibo
    i += 1 # acrescenta um à variável
print(' - FIM!')
