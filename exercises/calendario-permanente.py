#****************************
#**CALENDÁRIO***PERMANENTE***
#****************************
#Variáveis:
#ListaA = 1901 à 1924
#ListaB = 1925 à 1952
#ListaC = 1953 à 1980
#ListaD = 1981 à 2008
#ListaE = 2009 à 2036
#ListaF = 2037 à 2064
#ListaG = 2065 à 2092
#Listas dos meses:
JAN = [4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2]
FEV = [0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2,3,4,5]
MAR = [0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6]
ABR = [3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2]
MAI = [5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4]
JUN = [1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2,3,4,5,0]
JUL = [3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2]
AGO = [6,0,1,3,4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5]
SET = [2,3,4,6,0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1]
OUT = [4,5,6,1,2,3,4,6,0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3]
NOV = [0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1,2,3,4,6]
DEZ = [2,3,4,6,0,1,2,4,5,6,0,2,3,4,5,0,1,2,3,5,6,0,1,3,4,5,6,1]
#Listas dos anos:
ListaA = [0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
ListaB = [25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
ListaC = [53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
ListaD = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,0,1,2,3,4,5,6,7,8]
ListaE = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
ListaF = [37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
ListaG = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92]
#Listas dos dias:
#Dom = [1,8,15,22,29,36]
#Seg = [2,9,16,23,30,37]
#Ter = [3,10,17,24,31]
#Qua = [4,11,18,25,32]
#Qui = [5,12,19,26,33]
#Sex = [6,13,20,27,34]
#Sab = [7,14,21,28,35]
#--------------------
#----- ALGORITMO ----
#--------------------
print('='*49)
print('===          CALENDÁRIO PERMANENTE 0.1        ===')
print('='*49)
dia = int(input('Digite o dia:.............................. '))
mes = input('Digite o mês:................................ ')
ano = int(input('Digite o ano entre 1900 à 2092: '))
#Mês digitado:
if(mes == 'jan') or (mes == 'Jan') or (mes == 'JAN') or (mes == '1') or (mes == '01'):
    month = JAN
if(mes == 'fev') or (mes == 'Fev') or (mes == 'FEV') or (mes == '2') or (mes == '02'):
    month = FEV
if(mes == 'mar') or (mes == 'Mar') or (mes == 'MAR') or (mes == '3') or (mes == '03'):
    month = MAR
if(mes == 'abr') or (mes == 'Abr') or (mes == 'ABR') or (mes == '4') or (mes == '04'):
    month = ABR
if(mes == 'mai') or (mes == 'Mai') or (mes == 'MAI') or (mes == '5') or (mes == '05'):
    month = MAI
if(mes == 'jun') or (mes == 'Jun') or (mes == 'JUN') or (mes == '6') or (mes == '06'):
    month = JUN
if(mes == 'jul') or (mes == 'Jul') or (mes == 'JUL') or (mes == '7') or (mes == '07'):
    month = JUL
if(mes == 'ago') or (mes == 'Ago') or (mes == 'AGO') or (mes == '8') or (mes == '08'):
    month = AGO
if(mes == 'set') or (mes == 'Set') or (mes == 'SET') or (mes == '9') or (mes == '09'):
    month = SET
if(mes == 'out') or (mes == 'Out') or (mes == 'OUT') or (mes == '10'):
    month = OUT
if(mes == 'nov') or (mes == 'Nov') or (mes == 'NOV') or (mes == '11'):
    month = NOV
if(mes == 'dez') or (mes == 'Dez') or (mes == 'DEZ') or (mes == '12'):
    month = DEZ

#Ano digitado:
if(ano >= 1901) and (ano <= 1924):
    year = ano - 1900
    pos = ListaA.index(year)
if(ano >= 1925) and (ano <= 1952):
    year = ano - 1900
    pos = ListaB.index(year)
if(ano >= 1953) and (ano <= 1980):
    year = ano - 1900
    pos = ListaC.index(year)
if(ano >= 1981) and (ano <= 1999):
    year = ano - 1900
    pos = ListaD.index(year)
if(ano >= 2000) and (ano <= 2008):
    year = ano - 2000
    pos = ListaD.index(year)
if(ano >= 2009) and (ano <= 2036):
    year = ano - 2000
    pos = ListaE.index(year)
if(ano >= 2037) and (ano <= 2064):
    year = ano - 2000
    pos = ListaF.index(year)
if(ano >= 2065) and (ano <= 2092):
    year = ano - 2000
    pos = ListaG.index(year)
#-----Algoritmo_Matador-----#
numMagico = (month[pos] + dia)
#---------------------------#
if numMagico in range(1,37,7):
    calendario = 'DOMINGO'
if numMagico in range(2,38,7):
    calendario = 'SEGUNDA-FEIRA'
if numMagico in range(3,32,7):
    calendario = 'TERÇA-FEIRA'   
if numMagico in range(4,33,7):
    calendario = 'QUARTA-FEIRA'
if numMagico in range(5,34,7):
    calendario = 'QUINTA-FEIRA'
if numMagico in range(6,35,7):
    calendario = 'SEXTA-FEIRA'
if numMagico in range(7,36,7):
    calendario = 'SÁBADO'
print(f'A data digitada {dia}/{mes}/{ano} correnponde a {calendario}.')
saida = input('Click qualquer tecla para sair...')





