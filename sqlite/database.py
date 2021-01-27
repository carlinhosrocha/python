import sqlite3
from sqlite3 import Error
#realizando conexão com o banco de dados
def conexaoBanco():
	caminho = "C:\\Users\\carli\\Dropbox\\Python\\sqlite\\agenda.db"
	con = None
	try:
		con = sqlite3.connect(caminho)
	except Error as ex:
		print(ex)
	return con
vcon = conexaoBanco()
#criando tabela
'''vsql = """CREATE TABLE tb_contatos(
		N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
		T_NOMECONTATO VARCHAR(30),
		T_TELEFONECONTATO VARCHAR(14),
		T_EMAILCONTATO VARCHAR(30)
		);"""
'''
def criarTabela(conexao, sql):
	try:
		c = conexao.cursor()
		c.execute(sql)
		print('Tabela criada com sucesso! :)')
	except Error as ex:
		print(ex)
#encerrando conexão com banco de dados
#criarTabela(vcon, vsql)
#inserindo dados na tabela
nome = input('Nome: ')
tele = input('Telefone: ')
email = input('Email: ')
vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"','"+tele+"','"+email+"')"
def inserir(conexao, sql):
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
		print('Registro inserido!')
	except Error as ex:
		print(ex)
inserir(vcon, vsql)
vcon.close()