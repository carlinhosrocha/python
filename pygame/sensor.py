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
x = 350
y = 350
w = 50
h = 50
# variáveis dos sensores:
laranja = (255, 100, 0)
cinza = (150, 150, 150)
r_x = x+w/2
r_y = y+h/2
z = 0
a = alt
l = larg
e = 0
m = y
obstaculos = [[], [], [], [], [], [], []]
# tela principal:
tela = pygame.display.set_mode((larg, alt)) 
pygame.display.set_caption('OBR Simulator')
# controle do tempo:
relogio = pygame.time.Clock()
# loop principal:
while True:
    relogio.tick(60) # 60 frames por segundo
    tela.fill((255, 255, 255)) # limpa a tela a cada loop
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
    # desenhando o robô:
    sensor_top = pygame.draw.line(tela, (255, 0, 0), (x+w/2, y), (x+w/2, z), 1)
    sensor_down = pygame.draw.line(tela, (255, 0, 0), (x+w/2, y+w), (x+w/2, a), 1)
    sensor_right = pygame.draw.line(tela, (255, 0, 0), (x+w, y+h/2), (l, y+h/2), 1)
    sensor_left = pygame.draw.line(tela, (255, 0, 0), (x, y+h/2), (e, y+h/2), 1)
    # desenhando paredes:
    obstaculos[0] = pygame.draw.rect(tela, cinza, (0, 0, 700, 5))
    obstaculos[1] = pygame.draw.rect(tela, cinza, (0, 0, 5, 700))
    obstaculos[2] = pygame.draw.rect(tela, cinza, (0, 695, 700, 5))
    obstaculos[3] = pygame.draw.rect(tela, cinza, (695, 0, 5, 700))
    # desenhando obstáculos:
    obstaculos[4] = pygame.draw.rect(tela, (255, 0, 255), (300, 100, 50, 30))
    obstaculos[5] = pygame.draw.rect(tela, (255, 0, 255), (100, 400, 50, 30))
    obstaculos[6] = pygame.draw.rect(tela, (255, 0, 255), (500, 500, 50, 30))
    # desenhando robo:
    robo = pygame.draw.rect(tela, laranja, (x, y, w, h))
    # mensurando distância dos sensores:
    for i in range(0, 7, 1):
      if sensor_top.colliderect(obstaculos[i]):
        z = obstaculos[i][1]+15
      if sensor_down.colliderect(obstaculos[i]):
        a = obstaculos[i][1]
      if sensor_right.colliderect(obstaculos[i]):
        l = obstaculos[i][0]
      if sensor_left.colliderect(obstaculos[i]):
        e = obstaculos[i][0]+15
      else:
        z -= 5
        a += 5
        l += 5
        e -= 5
    # colisão com obstáculos:
    for i in range(0, 7, 1):
      if robo.colliderect(obstaculos[i]):
        y = 350
        x = 350
    # distâncias:
    dist_top = sensor_top[1]
    dist_down = sensor_down[1]
    dist_right = sensor_right[0]
    dist_left = sensor_left[0]
    print(f"{dist_top} - {dist_down} - {dist_right} - {dist_left}")
    # atualizando a tela a cada loop:      
    pygame.display.update()