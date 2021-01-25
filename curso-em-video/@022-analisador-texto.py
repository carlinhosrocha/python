# entrada do nome:
# .stript() elimina os espaços antes e depois da string
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')} letras.")
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
