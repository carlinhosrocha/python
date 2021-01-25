a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if(((a+b)>c)and((b+c)>a)and((a+c)>b)):
    print('Com os lados digitados é possível formar um triângulo.')
    if((a**2)+(b**2)==(c**2))or((b**2)+(c**2)==(a**2))or((a**2)+(c**2)==(b**2)):
        print('Além disso, o triângulo digitado é do tipo RETÂNGULO.')
    if a==b==c:
        print('O triângulo digitado é do tipo EQUILÁTERO.')
    if a!=b!=c!=a:
        print('O triângulo é do tipo ESCALENO.')
    else:
        print('O triângulo digitado é do tipo ISÓSCELES.')
else:
    print('Não é possível formar um triângulo com os lados digitados.')
