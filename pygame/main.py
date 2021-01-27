import pygame # importando biblioteca principal
from pygame.locals import * # importando todas as funções de locals
from sys import exit # função que fecha a janela
from random import randint # função que sorteia valores entre duas variáveis

pygame.init() # inicializando todas a funções e variáveis da biblioteca

largura = 640
altura = 480
y1 = 0
x1 = 0
y2 = altura/2
x2 = largura/2
y_cinza = randint(50, 430)
x_cinza = randint(40, 600)
fonte = pygame.font.SysFont('consolas', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura)) # objeto tela
pygame.display.set_caption('Jogo') # nome da janela
relógio = pygame.time.Clock() # controlando o tempo do jogo

# o jogo sempre está dentro de um loop infinito (carregamento automático)
while True:
  relógio.tick(60) # em frames por segundo
  tela.fill((0, 0, 0)) # "limpa" a tela a cada loop
  mensagem = f'Pontos: {pontos}'
  texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
  for event in pygame.event.get():
    if event.type == QUIT: # chegando condição de saída do jogo
      pygame.quit()
      exit()
    # controlando objetos:
    # para teclas clicadas:
    if event.type == KEYDOWN:
      if event.key == K_a:
        x2 = x2 - 5
      if event.key == K_d:
        x2 = x2 + 5
      if event.key == K_w:
        y2 = y2 - 5
      if event.key == K_s:
        y2 = y2 + 5
    # para teclas pressionadas:
    if pygame.key.get_pressed()[K_a]:
      x2 = x2 - 5
    if pygame.key.get_pressed()[K_d]:
      x2 = x2 + 5
    if pygame.key.get_pressed()[K_w]:
      y2 = y2 - 5
    if pygame.key.get_pressed()[K_s]:
      y2 = y2 + 5

  # desenhando figuras:
  # desenha um retângulo (objeto tela, cores rbg, coordenadas com largura e altura)
  pygame.draw.rect(tela, (255, 0, 0), (400, 400, 50, 50))
  pygame.draw.circle(tela, (0, 0, 255), (600, 400), 40) # último parâmetro -> raio do circulo
  pygame.draw.line(tela, (255, 255, 0), (320, 0), (320, 480), 5) # último parâmetro -> espessura da linha
  # dando movimentos às formas:
  pygame.draw.rect(tela, (0, 255, 255), (x1, y1, 40, 50))
  if y1 >= altura:
    y1 = 0
  y1 = y1 + 5
  # colisões:
  ret_silver = pygame.draw.rect(tela, (100, 100, 100), (x2, y2, 40, 50))
  ret_cinza = pygame.draw.rect(tela, (200, 200, 200), (x_cinza, y_cinza, 40, 50))

  # condição de colisão:
  if ret_silver.colliderect(ret_cinza):
    y_cinza = randint(50, 430)
    x_cinza = randint(40, 600)
    pontos = pontos + 1
  tela.blit(texto_formatado, (430, 10))
  pygame.display.update() # a cada loop será atualizada a tela do jogo