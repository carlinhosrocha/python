frase = str(input('Digite uma frase: ')).strip().upper() #elimina os espaços nas extremidades
palavras = frase.split()                                 #separa a frase em palavras
junto = ''.join(palavras)                                #junta as palavras em uma string
inverso = ''
for letra in range((len(junto) - 1), -1, -1):           #inverte a string
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase não é um palíndromo.')
#OBS: sem o for (com fatiamento)
#inverso = junto[::2]
    
    

