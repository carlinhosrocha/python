#programa que retorna se um numero eh primo ou nao.
#funcao de verificao do numero digitado:
def eh_primo(n):
    #gera um intervalo entre 2 e 1/2 do numero digitado.
    for d in range(2, n//2+1):
        #verifica se o numero possui modulo nulo:
        if n % d == 0:
            return False
    #se o modulo for diferente de nulo, entao o numero eh primo.
    return True
numero = int(input("Digite um numero para ver se ele eh primo: "))
#chamada da funcao verfica-primo:
primo = eh_primo(numero)
print("O numero {} eh primo? Resposta: {}".format(numero, primo))
