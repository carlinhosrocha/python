# =============================== Classes - Orientação à Objetos ===================================
# O que define os ATRIBUTOS e MÉTODOS dos OBJETOS? Seus TIPOS, ou melhor CLASSES.
# Classe é uma espécie de molde (forma).
# ======================================= Exemplos =================================================
# Criação da Classe para contruir Objetos do tipo FRAÇÃO.
# Com isso poderemos criar novos 'tipos', além dos já existentes tipos primitivos.
# **************************************************************************************************
class Fracao:
    # Atributos: [1° numerador]-[2° denominador]
    # Métodos: [somar]-[subtrair]-[multiplica]-[inverter]-[inverter-polaridade]-[simplificar]
    def __init__(self, num, den): # função especial construtora da classe
        # self -> objeto a ser construido
        # parâmetros -> num e den 
        self.numerador = num # criação de uma variável (espaço de armazenamento)
        if den == 0: # denominador não pode ser zero
            self.denominador = 1 # se o denominador for 0 o contrutor substituirá por 1
        else:
            self.denominador = den # criação de uma variável (espaço de armazenamento)
    def somar(self, outra): # método que soma duas frações
        pass # a ser passado
    def subtrair(self, outra): # método para subtrair fração
        return self.somar(outra.negar()) # método que evoca outros métodos
    def multiplicar(self, outra): # método para multiplicar a fração
        x = self.numerador * outra.numerador #numerador do objeto que chamou vezes o do outro objeto
        y = self.denominador * outra.denominador #denominador de um objeto vezes o do outro objeto
        return Fracao(x, y) # retorno do método
    def dividir(self, outra): # método para dividir uma fracao por outra
        return self.multiplicar(outra.inverter()) # utilizando métodos dentro de outros métodos
    def inverter(self): # método que retorna a fração invertida
        # o self é uma referência para o próprio objeto que chamou o método
        return Fracao(self.denominador, self.numerador) # retorno invertido do num e den
    def negar(self): # método que inverte polaridade de uma fração
        return Fracao(-self.numerador, self.denominador) #retorno da fração com polaridade invertida
    def simplificar(self): # método para simplificar fração
        pass # a ser passado
a = Fracao(4, 5)        # cria um objeto
b = Fracao(-2, 7)       # cria outro objeto
resultado = a.multiplicar(b)        # passa-se a outra fração como argumento 
c = Fracao.inverter(a)  # forma pouco usual de evocar o método
d = a.inverter()        # forma mais usual de evocar método
