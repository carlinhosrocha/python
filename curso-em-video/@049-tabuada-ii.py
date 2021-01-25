num = int(input('Digite qual tabuada a ser mostrada: '))
for i in range(1, 11):
    mult = i * num
    print(f'{i:2} x {num} = {mult}')
