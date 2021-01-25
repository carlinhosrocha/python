cont = 0
num = 0
for i in range(1, 500):
    if i % 2 == 1:
        if i % 3 == 0:
            cont += i
            num += 1
print(f'A soma dos {num} números ímpares entre 1 e 500 é {cont}.')
