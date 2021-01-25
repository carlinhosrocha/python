dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km foi percorrido com o carro? '))
valor = (dia * 60) + (km * 0.15)
print(f'Você deve pagar R${valor:.2f}.')
