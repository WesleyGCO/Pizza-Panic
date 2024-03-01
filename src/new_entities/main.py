import pygame
import sys
from Vetor import Vetor

def main():
    # Inicialização do Pygame
    pygame.init()
    largura, altura = 800, 600
    screen = pygame.display.set_mode((largura, altura))
    clock = pygame.time.Clock()

    # Criar um objeto personagem
    personagem = Vetor(cor=(255, 0, 0), tamanho_x=50, tamanho_y=50, velocidade=5, posicao_x=375, posicao_y=500)

    # Loop principal
    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Verificar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            personagem.andar_esquerda()
        if teclas[pygame.K_RIGHT]:
            personagem.andar_direita()

        # Desenhar o objeto personagem na tela
        personagem.desenhar(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
