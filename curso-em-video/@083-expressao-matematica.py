aberto = fechado = 0
exp = str(input('Digite uma expressão matemática: '))
for i in exp:
    if i == '(':
        aberto += 1
    elif i == ')':
        fechado += 1
if aberto == fechado:
    print('Expressão correta!')
else:
    print('Expressão inválida!')
#---------------------------------------------------#
expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valendo!')
else:
    print('Expressão inválida!')
