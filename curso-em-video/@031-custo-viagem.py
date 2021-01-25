dist = int(input('Digite a distância em km: '))
valor = dist * 0.50 if(dist < 200) else dist * 0.45
print(f'O valor da viagem será de R${valor:.2f}.')
    
