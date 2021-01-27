import pygame
from pygame.locals import *
from sys import exit
from time import sleep
# iniciando o game:
pygame.init()
# variáveis da janela:
larg = 700
alt = 700
# variáveis do robô:
passo = 5
x = 75
y = 630
w = 50
h = 50
#=================================================================================================#
# variáveis dos sensores:
# sensor de linha do topo:
sensor_line_top = [[], [], [], [], [], [], [], [], [], []] # armazena os 10 pixels verificados
status_line_top = "" # 0 -> branco | 1 -> preto | 2 -> verde
cont_top = 0
# sensor de linha do fundo:
sensor_line_bottom = [[], [], [], [], [], [], [], [], [], []] # armazena os 10 pixels verificados
status_line_bottom = "" # 0 -> branco | 1 -> preto | 2 -> verde
cont_bottom = 0
# sensor de linha da esquerda:
sensor_line_left = [[], [], [], [], [], [], [], [], [], []] # armazena os 10 pixels verificados
status_line_left = "" # 0 -> branco | 1 -> preto | 2 -> verde
cont_left = 0
# sensor de linha da direita:
sensor_line_right = [[], [], [], [], [], [], [], [], [], []] # armazena os 10 pixels verificados
status_line_right = "" # 0 -> branco | 1 -> preto | 2 -> verde
cont_right = 0
#=================================================================================================#
distance = 100
laranja = (255, 100, 0)
cinza = (150, 150, 150)
preto = (0, 0, 0, 255)
r_x = x+w/2
r_y = y+h/2
z = 0
a = alt
l = larg
e = 350
m = y
dist = []
obstaculos = [[], [], [], [], [], [], []]
# tela principal:
tela = pygame.display.set_mode((larg, alt)) 
pygame.display.set_caption('OBR Simulator')
arena = pygame.image.load("C:/Users/carli/Documents/Code/trash/pygame/arena.png")
# controle do tempo:
relogio = pygame.time.Clock()
# loop principal:
while True:
    relogio.tick(60) # 60 frames por segundo
    #tela.fill((255, 255, 255)) # limpa a tela a cada loop
    # desenhando sensores:
    dist_sensor = pygame.draw.circle(tela, (0, 150, 150), (x+w/2, y+h/2), z)
    oculto = pygame.draw.circle(tela, (255, 255, 255), (x+w/2, y+h/2), z-2)
    tela.blit(arena,(0, 0)) # desenhando arena
    # cheando eventos externos (imputs):
    for event in pygame.event.get():
        if event.type == QUIT: # chegando condição de saída do jogo
            pygame.quit()
            exit()
    # para teclas clicadas:
    if event.type == KEYDOWN:
      if event.key == K_LEFT:
        x = x - passo
      if event.key == K_RIGHT:
        x = x + passo
      if event.key == K_UP:
        y = y - passo
      if event.key == K_DOWN:
        y = y + passo
    # desenhando sensores:
    
    # desenhando paredes:
    obstaculos[0] = pygame.draw.rect(tela, cinza, (0, 0, 700, 5))
    obstaculos[1] = pygame.draw.rect(tela, cinza, (0, 0, 5, 700))
    obstaculos[2] = pygame.draw.rect(tela, cinza, (0, 695, 700, 5))
    obstaculos[3] = pygame.draw.rect(tela, cinza, (695, 0, 5, 700))
    # desenhando obstáculos:
    obstaculos[4] = pygame.draw.rect(tela, (255, 0, 255), (75, 300, 50, 30))
    obstaculos[5] = pygame.draw.rect(tela, (255, 0, 255), (435, 490, 50, 30))
    obstaculos[6] = pygame.draw.rect(tela, (255, 0, 255), (570, 80, 30, 50))
    # ver sensores de distância:
    dist_sensor = pygame.draw.circle(tela, (0, 150, 150), (x+w/2, y+h/2), z)
    oculto = pygame.draw.circle(tela, (255, 255, 255), (x+w/2, y+h/2), z-2)
    # desenhando robo:
    robo = pygame.draw.rect(tela, (255, 204, 0), (x, y, w, h))
    line_sensor = pygame.draw.rect(tela, (0, 150, 150), ((x+w/2-10), (y+h/2-10), 20, 20))
    # sensor de distância:
    for i in range(len(obstaculos)):
      if dist_sensor.colliderect(obstaculos[i]):
        distance = abs(z-25)
        z = 0
      else:
        z += 1
    # colisão do robô:
    if distance < 10:
      x = 75
      y = 630
    # sensores de linha:
    for n in (range(10)):
      sensor_line_top[n] = tela.get_at((x+20+n, y-1)) # sensor do topo
      sensor_line_bottom[n] = tela.get_at((x+20+n, y+h+1)) # sensor do fundo
      sensor_line_left[n] = tela.get_at((x-1, y+20+n)) # sensor esquerdo
      sensor_line_right[n] = tela.get_at((x+w+1, y+20+n)) # sensor direito
    # tratamento dos dados de entrada:
    # sensor do topo:
    for i in sensor_line_top:
      if i == preto:
        status_line_top = 1
      else:
        cont_top += 1
    if cont_top == 10:
      status_line_top = 0
    # sensor do fundo:
    for i in sensor_line_bottom:
      if i == preto:
        status_line_bottom = 1
      else:
        cont_bottom += 1
    if cont_bottom == 10:
      status_line_bottom = 0
    # sensor da esquerda:
    for i in sensor_line_left:
      if i == preto:
        status_line_left = 1
      else:
        cont_left += 1
    if cont_left == 10:
      status_line_left = 0
    # sensor da direita:
    for i in sensor_line_right:
      if i == preto:
        status_line_right = 1
      else:
        cont_right += 1
    if cont_right == 10:
      status_line_right = 0
    cont_top = 0
    cont_bottom = 0
    cont_left = 0
    cont_right = 0
    print(f"top: {status_line_top} | bottom: {status_line_bottom} | left: {status_line_left} | right: {status_line_right} | distance: {distance}")
    # atualizando a tela a cada loop:
    pygame.display.update()