var = input('Digite alguma coisa: ')
print(f'O tipo primitivo deste valor é {type(var)}.')
print(f'Só tem espaços? {var.isspace()}')
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f'É alfanumérico? {var.isalnum()}')
print(f'Está em maiúscula? {var.isupper()}')
print(f'Está em minúscula? {var.islower()}')
print(f'Está capitalizado? {var.istitle()}')

