'''
=================================================================
PROGRAMAÇÃO: imperativa/procedural -> orientada a objetos
-----------------------------------------------------------------
= imperativa/procedural:
- passo a passo das instruções a serem executadas
- dividida em funções
= orientada a objetos:
- em python tudo são objetos (valores: listas, strigs, números)
- objetos tem ATRIBUTOS
- objetos são capazes de realizar AÇÕES
-----------------------------------------------------------------
'''
# objeto é um valor manipulado pelo programa que possui atributos e métodos
num = 7 # o valor 7 é apenas um atributo de um objeto que armazena a variável num
soma = num + 8 # o objeto é capaz de realizar ações com um outro objeto de mesmo tipo
nome = 'Python' # objeto com um atributo que armazena a sequência de caracteres
frase = nome + 'Orientado a Objetos' # ação (concatenação) realizada pelo objeto
condição = nome == 'Carlos' # outra ação realizada pelo objeto
nome.upper() # ação que retorna a sequência de caracteres todos em maiúsculos
nome.find("a")# ação que retorna a posição do caracter especificado
nome.endswith('tos')# ação que verifica se nome termina com a sequência especificada
nome.split() # ação que retorna uma lista com os elementos separadas da string
# [nome da variável][ponto][nome da função]<<<<<Notação de Ponto
# os atributos de um objeto são como variáveis internas internas a ele
# as ações que os objetos podem realizar são como funções internas a ele
# =======================
#   OBJETO.FUNÇÃO()
# =======================
# geralmente as funções internas utilizam os valores dos atributos para realizar suas tarefas
# ********************************************
#  FUNÇÕES INTERNAS >>>>>>> MÉTODOS DO OBJETO
# ********************************************
# exemplo: STRING.UPPER() <<< objeto do tipo string possui um método chamado upper
# quando pedimos para um objeto realizar uma de suas ações dizemos que enviamos uma MENSAGEM
# [OBJETO].MÉTODO(PARÂMETRO)
