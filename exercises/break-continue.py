#Intrução Break e Continue
i = int(input("Digite um valor: "))
b = 0
while (b < i):
     b += 1
     if (b%2 == 0):
          continue
     print(b)
     if (i > 100):
          break
else:
     print("Fim do laço de repetição... ")
