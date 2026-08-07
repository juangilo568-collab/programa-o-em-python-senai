import pygame 
import sys
import random

pygame.init()
LARGURA =  800
ALTURA  =  400
tela  =  pygame.display.set_mode([LARGURA, ALTURA])

pygame.display.set_caption('JOGO TREX')
# CARREGAR AS IMAGENS 

trex1 = pygame.image.load('trex1.png')
trex4 = pygame.image.load('trex4.png')
cacto_img = pygame.image.load('obstacle1.png')
# cacto2 = pygame.image.load('obstacle2.png') 
chao = pygame.image.load('ground2.png')

trex_x = 100
trex_y = 300

vel_y =  0
gravidade = 1
pulando = False
chao_x = 0
cacto_x = 800
cacto_y = 300
score =  0

frame =  0

fonte = pygame.font.SysFont("Arial", 30, bold=True)

game_over  = False 
clock = pygame.time.Clock()


while True:
    # captura de eventos no jogo .... 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
               vel_y = -20
               pulando = True
            if  evento.key == pygame.K_w and game_over: 
                trex_y = 300
                cacto_x = 800
                score = 0
                game_over = False
# -------------------------------------------------------
    if not game_over:
        vel_y += gravidade
        trex_y += vel_y

        if  trex_y >= 300:
            trex_y = 300
            pulando  = False

        chao_x -=  5
        if chao_x <= -800:
           chao_x = 0

        cacto_x -= 5
        if cacto_x <= 50 :
            cacto_x = random.randint(800,1000)  
            score += 1

        frame += 1
        if frame >= 20:
            frame = 0
        if frame < 10:
            trex = trex1
        else:
            trex = trex4            

        trex_rect  =  trex.get_rect(topleft = (trex_x, trex_y))
        cacto_rect  = cacto_img.get_rect(topleft = (cacto_x, cacto_y))

        if trex_rect.colliderect(cacto_rect):
            game_over = True

    tela.fill(('yellow'))

    tela.blit(chao,(chao_x, 340))    

    tela.blit(chao,(+800,340))

    tela.blit(trex, (trex_x, trex_y))

    tela.blit(cacto_img, (cacto_x, cacto_y))


    texto = fonte.render('PONTOS: ', score, True)

    tela.blit(texto, (600,20))

    if game_over:
        texto2 =  fonte.render('GAME OVER', str(score), True)
        tela.blit(texto2, (310,400))
          





    pygame.display.update()
    clock.tick(30)