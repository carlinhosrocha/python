def primo(n):
    numero = 2
    while numero <= n:
        for i in range(2, numero//2+1):
            if (numero % i == 0):
                print(numero)
        numero = numero + 1
valor = int(input("Digite até qual intervalo procurar primos: "))
primo(valor)

