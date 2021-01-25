peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (cm) '))
altura = altura / 100 #conversão para metros
indice = peso / (altura**2)
print(f'Seu índice de massa corporal (IMC) é de {indice:.2f}kg/m².')
if indice <= 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < indice <= 25:
    print('Você está com o peso normal.')
elif 25 < indice <= 30:
    print('Você está com sobrepeso.')
elif 30 > indice <= 40:
    print('Você está com obesidade.')
elif indice > 40:
    print('Você está com obesidade mórbida.')
