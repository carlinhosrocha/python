nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi de {media:.2f}.')
if media < 5:
    print('Você está REPROVADO!')
elif 5 <= media <= 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Parabéns! Você está APROVADO!')
