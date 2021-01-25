import math
angulo = float(input('Digite o valor do ângulo em graus: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo}° tem SENO {seno:.2f}.')
print(f'O ângulo de {angulo}° tem COSENO {coseno:.2f}.')
print(f'O ângulo de {angulo}° tem TANGENTE {tangente:.2f}.')
