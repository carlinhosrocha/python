#importação das bibliotecas
from pyfirmata import Arduino, util
import time
#definição da porta
Uno = Arduino('COM6')
print('Olá, mundo!')
#loop infinito
while True:
	#led ligado
	Uno.digital[13].write(1)
	print('Led ligado!')
	time.sleep(1)
	#led desligado
	Uno.digital[13].write(0)
	print('Led desligado!')
	time.sleep(1)