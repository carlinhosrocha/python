a = float(input('Primeira aresta: '))
b = float(input('Segunda aresta: '))
c = float(input('Terceira aresta: '))
if (a<b+c) and (b<a+c) and (c<a+b):
    print('Com as arestas digitadas é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
