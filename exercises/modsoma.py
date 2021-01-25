#Função Fatorial
def fatorial(numero):
    if numero < 0:
        print('Digite um número maior ou igual a zero.')
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            elementos = []
            resul = 1
            fat = 1
            num = 1
            for n in range(1, numero, 1):
                fat = (numero * (numero - n))
                elementos.append(fat)
            return elementos
                
        
a = fatorial(5)
print(a)
