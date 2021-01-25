nome = str(input('Digite seu nome completo: ')).strip() #elimina espaços
n = nome.split() #fatia string
print(f'Prazer em te conhecer! Seu primeiro nome é {n[0].upper()} e seu último nome é {n[-1].upper()}.')
