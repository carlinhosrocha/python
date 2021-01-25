medida = float(input('Digite a distância em metros: '))
km = medida*0.001
hm = medida*0.01
dam = medida*0.1
dm = medida*10
cm = medida*100
mm = medida*1000
print(20*'-')
print(f'{medida}m em:')
print(f'km é {km:.2f}')
print(f'hm é {hm:.2f}')
print(f'dam é {dam:.2f}')
print(f'cm é {cm:.2f}')
print(f'mm é {mm:.2f}')
print(10*'-')
