cadastro = list()
pessoa = dict()
flag = True
print('=='*30)
while flag:
	pessoa['nome'] = str(input('Nome: '))
	while True:
		sexy = str(input('Sexo:[M/F]: ')).upper()[0]
		if sexy not in 'MF':
			print('ERRO! Por favor, digite apenas M ou F.')
			continue
		pessoa['sexo'] = sexy
		break
	pessoa['idade'] = int(input('Idade: '))
	cadastro.append(pessoa.copy())
	while True:
		out = str(input('Quer continuar?[S/N]: ')).upper()
		if out not in 'SN':
			print('ERRO! Por favor, digite apenas S ou N.')
			continue
		elif out == 'S':
			break
		elif out == 'N':
			flag = False
			break
print('=='*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas.')
tot = 0
for c in range(0, len(cadastro)):
	idade = cadastro[c]["idade"]
	tot += idade
média = tot / len(cadastro)
print(f'B) A média de idade é de {média:.2f} anos.')
mulheres = []
for c in range(0, len(cadastro)):
	if cadastro[c]['sexo'] in 'F':
		mulher = cadastro[c]['nome']
		mulheres.append(mulher)
print(f'C) As mulheres cadastradas foram: ', end='')
for n in mulheres:
	print(f'{n} - ', end='')
print('FIM!')
print('D) Lista das pessoas que estão acima da média:')
for c in range(0, len(cadastro)):
	old = cadastro[c]['idade']
	if old > média:
		print(f' -> nome: {cadastro[c]["nome"]}; sexo: {cadastro[c]["sexo"]}; idade: {cadastro[c]["idade"]}.')
print('Encerrado...')
print('=='*30)
