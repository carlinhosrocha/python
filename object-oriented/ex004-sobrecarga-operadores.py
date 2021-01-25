# =============================== SOBRECARGA DE OPERADORES =========================================
# Capacidade da linguagem de permitir que você defina ou modifique o comportamento dos operadores
# Na construção de uma classe como os objetos irão interagir com os operadores
# ==================================================================================================
class Fracao:
    def __init__(self, num, den): 
        self.numerador = num
        if den == 0:
            self.denominador = 1 
        else:
            self.denominador = den 
    def somar(self, outra):
        pass 
    def subtrair(self, outra): 
        return self.somar(outra.negar()) 
    def multiplicar(self, outra): 
        x = self.numerador * outra.numerador 
        y = self.denominador * outra.denominador 
        return Fracao(x, y) 
    def dividir(self, outra): 
        return self.multiplicar(outra.inverter()) 
    def inverter(self): 
        return Fracao(self.denominador, self.numerador)
    def negar(self):
        return Fracao(-self.numerador, self.denominador) 
    def simplificar(self):
        pass 
    def __str__(self):
        representation = "{}/{}".format(self.numerador, self.denominador)
        return representation 
    def __repr__(self):
        representation = "Fracao({},{})".format(self.numerador, self.denominador)
        return representation
    def __add__(self, outra): # método especial que usa o operador + 
        return self.somar(outra)
    def __sub__(self, outra): # método especial que usa o operador -
        return self.subtrair(outra)
    def __mul__(self, outra): # método especial que usa o operador *
        return self.multiplicar(outra)
    def __truediv__(self, outra): # método especial que usa o operador /
        return self.dividir(outra)
a = Fracao(4, 5)
b = Fracao(3, 2)
c = b.multiplicar(a)
print(a, b, c)
d = a * b
print(d)
