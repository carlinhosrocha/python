#programa que retorna o enesimo termo de uma P.A.
#funcao que ira calcular o valor do enesimo termo:
def pa_termo(a_zero, razao, enesimo):
    a_inicial = a_zero
    for i in range(enesimo):
        a_inicial = a_inicial + razao
    return a_inicial
#funcao que ira calcular o valor da soma dos termos:
def pa_soma(a_zero, razao, enesimo):
    soma = 0
    for i in range(enesimo+1):
        #adiciona a variavel soma o valor calculado na funcao anterior:
        soma = soma + pa_termo(a_zero, razao, enesimo)
        return soma
#entrada de valores:
a_zero = int(input("Digite o valor inicial da P.A.: "))
razao = int(input("Informe a razao da P.A.: "))
enesimo = int(input("Por fim, qual elemento [posicao] voce quer: "))
pa = pa_termo(a_zero, razao, enesimo)
sum = pa_soma(a_zero, razao, enesimo)
print("O valor do {}° elemento da P.A eh: {}.".format(enesimo, pa))
print("A soma de todos os termos eh: {}.".format(sum))