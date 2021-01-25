n = int(input('Digite qual tabuada você quer ver: '))
print(10*'=')
for i in range(10):
    multi = n * i
    print(f'{n} X {i} = {multi}')
print(10*'=')
