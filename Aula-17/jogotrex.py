#bibliotecas que foram importaas, a patir delas, é possível executar comandos ja prontos (desde que a biblioteca tenha sido chamada)
import pygame 
import sys
import random

#comando que da inicio ao pygame
pygame.init()

#variavel onde o valor 800 foi atribuido ao nome largura e o valor 400 atribuido ao nome altura
LARGURA =  800
ALTURA  =  400

#guarda a variavel "tela" que cria a janela pro jogo, chama o pygame display responsavel pela tela e a função set mode que cria a janela baseada nas outras varias a qual ja foram atribuidas valores
tela  =  pygame.display.set_mode([LARGURA, ALTURA])

#chamo o módulo display responsavel pela tela e a função set_caption responsavel por carregar o nome nessa tela
pygame.display.set_caption('JOGO TREX')

# CARREGAR AS IMAGENS 

#tupla armazena na variavel t 
t  =  (20,20)

# Usa o módulo image do Pygame e executa a função load() para carregar a imagem "1.png"
# O resultado é guardado na variável trex1.
trex1 = pygame.image.load('1.png')

# Usa o módulo transform do Pygame e executa a função scale() para alterar o tamanho da imagem que está em trex1. A tupla (60, 60) informa a largura e a altura da nova imagem.
# O resultado é guardado na variável picture.
picture = pygame.transform.scale(trex1, (60, 60))

trex2 = pygame.image.load('2.png')
picture2 = pygame.transform.scale(trex2, (60, 60))

trex3 = pygame.image.load('3.png')
picture3 = pygame.transform.scale(trex2, (60, 60))


cacto_img = pygame.image.load('cacto.png')
# cacto2 = pygame.image.load('obstacle2.png') 
chao = pygame.image.load('chao.png')
# msc = pygame.mixer_music.load('arca.mp3')
# msc2 =  pygame.mixer_music.load('go.mp3')



# Cria uma variável para guardar a posição X (horizontal) do T-Rex.
trex_x = 100

# Cria uma variável para guardar a posição Y (vertical) do T-Rex.
trex_y = 300


# Guarda a velocidade vertical do T-Rex.
# Começa em 0 porque o T-Rex começa parado.
vel_y = 0

# Guarda o valor da gravidade que será aplicada ao T-Rex.
gravidade = 1

# Guarda se o T-Rex está pulando.
# False = não está pulando.
pulando = False


# Guarda a posição X do chão.
chao_x = 0

# Guarda a posição X do cacto.
# Começa em 800, provavelmente na parte direita da tela.
cacto_x = 800

# Guarda a posição Y do cacto.
cacto_y = 300

# Guarda a quantidade de pontos do jogador.
score = 0


# Guarda um contador de frames.
# Ele será usado para controlar a animação do T-Rex.
frame = 0


# Usa o módulo "font" do Pygame e executa a função SysFont().
# Cria uma fonte Arial com tamanho 30 e em negrito.
# O resultado é guardado na variável "fonte".
fonte = pygame.font.SysFont("Arial", 30, bold=True)


# Guarda se o jogo terminou.
# False = o jogo ainda está acontecendo.
game_over = False

# Usa o módulo "time" do Pygame e executa a função Clock().
# Cria um relógio para controlar a velocidade do jogo.
# O resultado é guardado na variável "clock".
clock = pygame.time.Clock()


# Cria um loop infinito.
# Enquanto o programa estiver rodando, tudo dentro do while será repetido.
while True:

    # Inicializa o sistema de áudio do Pygame.
    pygame.mixer.init()


    # Usa o módulo "event" do Pygame e executa a função get().
    # Pega todos os eventos que aconteceram desde a última verificação.
    # Cada evento será colocado na variável "evento".
    for evento in pygame.event.get():

        # Verifica se o evento foi o fechamento da janela.
        if evento.type == pygame.QUIT:

            # Encerra o Pygame.
            pygame.quit()

            # Encerra o programa Python.
            sys.exit()


        # Verifica se alguma tecla do teclado foi pressionada.
        if evento.type == pygame.KEYDOWN:

            # Verifica se a tecla pressionada foi ESPAÇO
            # E também verifica se o T-Rex NÃO está pulando.
            if evento.key == pygame.K_SPACE and not pulando:

                # Coloca a velocidade vertical em -20.
                # O valor negativo faz o T-Rex subir.
                vel_y = -20

                # Informa que o T-Rex está pulando.
                pulando = True


            # Verifica se a tecla pressionada foi W
            # E se o jogo está no estado de Game Over.
            if evento.key == pygame.K_w and game_over:

                # Coloca o T-Rex novamente na posição inicial.
                trex_y = 300

                # Coloca o cacto novamente na posição inicial.
                cacto_x = 800

                # Zera a pontuação.
                score = 0

                # Informa que o jogo não está mais em Game Over.
                game_over = False


    # Verifica se o jogo NÃO está em Game Over.
    # Todo o código abaixo só funciona enquanto o jogo estiver ativo.
    if not game_over:

        # Aumenta a velocidade vertical usando a gravidade, cada repetição, o T-Rex vai ficando mais rápido para baixo.
        vel_y += gravidade

        # Altera a posição vertical do T-Rex usando sua velocidade.
        trex_y += vel_y


        # Verifica se o T-Rex chegou ou passou do chão.
        if trex_y >= 300:

            # Mantém o T-Rex exatamente na altura do chão.
            trex_y = 300

            # Informa que o T-Rex não está mais pulando.
            pulando = False


        # Move o chão 5 pixels para a esquerda, isso cria a sensação de que o T-Rex está correndo.
        chao_x -= 5

        # Verifica se o chão já saiu completamente pela esquerda da tela.
        if chao_x <= -800:

            # Coloca o chão novamente na posição 0, assim ele pode aparecer novamente pela direita.
            chao_x = 0


        # Move o cacto 5 pixels para a esquerda.
        cacto_x -= 5

        # Verifica se o cacto saiu da tela pela esquerda.
        if cacto_x < -50:

            # Coloca o cacto novamente em uma posição aleatória.
            # random.randint() sorteia um número entre 800 e 1000.
            cacto_x = random.randint(800, 1000)

            # Aumenta a pontuação em 1.
            score = score + 1


        # Aumenta o contador de frames em 1.
        # Ele será usado para controlar a animação do T-Rex.
        frame += 1

        # Verifica se o contador passou de 30.
        if frame > 30:

            # Volta o contador para 0.
            # Assim a animação começa novamente.
            frame = 0


        # Verifica se o frame está entre 0 e 9.
        if frame < 10:

            # Usa a imagem "picture" para representar o T-Rex.
            trex = picture

        # Se o frame estiver entre 15 e 30...
        elif frame >= 15 and frame <= 30:

            # Usa a imagem "picture2" para representar o T-Rex.
            trex = picture2

        # Se nenhuma das condições anteriores for verdadeira...
        else:

            # Usa a imagem "picture3" para representar o T-Rex.
            trex = picture3


        # Executa a função get_rect() da imagem do T-Rex.
        # Cria um retângulo que representa a área do T-Rex.
        # Esse retângulo será usado para verificar colisões.
        # topleft define a posição do canto superior esquerdo.
        trex_rect = trex.get_rect(topleft=(trex_x, trex_y))


        # Executa a função get_rect() da imagem do cacto.
        # Cria um retângulo que representa a área do cacto.
        # Esse retângulo também será usado para verificar colisões.
        cacto_rect = cacto_img.get_rect(topleft=(cacto_x, cacto_y))


        # Verifica se o retângulo do T-Rex encostou no retângulo do cacto.
        if trex_rect.colliderect(cacto_rect):

            # Se houver colisão, muda o estado do jogo para Game Over.
            game_over = True


    # Preenche toda a tela com a cor amarela.
    # fill() é uma função que preenche a superfície com uma cor.
    tela.fill(('yellow'))


    # Desenha a imagem do chão na tela.
    # chao = imagem do chão.
    # (chao_x, 340) = posição onde o chão será desenhado.
    tela.blit(chao, (chao_x, 340))


    # Desenha uma segunda imagem do chão.
    # Ela fica 800 pixels à frente da primeira.
    # Isso ajuda a criar um chão contínuo.
    tela.blit(chao, (chao_x + 800, 340))


    # Desenha a imagem atual do T-Rex na tela.
    # A posição é determinada por trex_x e trex_y.
    tela.blit(trex, (trex_x, trex_y))


    # Desenha a imagem do cacto na tela.
    # A posição é determinada por cacto_x e cacto_y.
    tela.blit(cacto_img, (cacto_x, cacto_y))


    # Usa a função render() da fonte.
    # Cria uma imagem contendo o texto "PONTOS:" + a pontuação.
    # str(score) transforma o número da pontuação em texto.
    # True ativa o anti-aliasing para deixar o texto mais suave.
    # A cor do texto será vermelha.
    # O resultado é guardado na variável "texto".
    texto = fonte.render('PONTOS:' + str(score), True, 'red')


    # Desenha o texto da pontuação na tela.
    # (600, 20) define a posição do texto.
    tela.blit(texto, (600, 20))


    # Verifica se o jogo está em Game Over.
    if game_over:

        # Cria o texto "GAME OVER".
        # O resultado é guardado na variável "texto2".
        texto2 = fonte.render('GAME OVER', str(score), True)

        # Desenha o texto "GAME OVER" na tela.
        # (310, 400) define a posição.
        tela.blit(texto2, (310, 400))


    # Atualiza a tela.
    # Faz com que tudo que foi desenhado apareça na janela.
    pygame.display.update()


    # Usa o objeto Clock e executa a função tick().
    # Limita o jogo para aproximadamente 30 frames por segundo.
    clock.tick(30)

					