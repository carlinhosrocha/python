from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
	criarArquivo(arq)
while True:
	resposta = menu(['Ver Cadastros', 'Cadastrar Novos', 'Sair do Sistema'])
	if resposta == 1:
		lerArquivo(arq)
	elif resposta == 2:
		cabeçalho('NOVO CADASTRO')
		nome = str(input('Nome: '))
		idade = leiaInt('Idade: ')
		cadastrar(arq, nome, idade)
	elif resposta == 3:
		cabeçalho('Saindo do Sistema... Até logo!')
		break
	else:
		print('Erro! Digite uma opção válida!')
	sleep(2)

