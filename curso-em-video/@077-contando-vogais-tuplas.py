palavras = ('programar', 'aprender', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print('Procurador de Vogais...')
print('-'*40)
for i in palavras:
    word = i
    word = word.upper()
    print(f'Na palavra {word} temos: ', end='')
    if 'A' in word:
        print(' A ', end='')
    if 'E' in word:
        print(' E ', end='')
    if 'I' in word:
        print(' I ', end='')
    if 'O' in word:
        print(' O ', end='')
    if 'U' in word:
        print(' U ', end='')
    print()
print('-'*40)
