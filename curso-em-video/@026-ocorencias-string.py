frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frase.count("a")} vezes na frase.')
print(f'A letra A aparece pela primeira vez na {frase.find("a")+1}° posição.')
print(f'A ultima letra A aparece na {frase.rfind("a")+1}° posição.')
