import pygame, random
from entities.ItemRuim import ItemRuim
from entities.Personagem import Personagem

class Jogo:
    def __init__(self):
        # Configurações da janela
        self.screen_width = 800
        self.screen_height = 600

        # Cria a tela com o título Pizza Panic
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Pizza Panic")

        self.is_running = False

    def init(self):
        # Inicializa o Pygame
        pygame.init()

        self.relogio = pygame.time.Clock()
        self.personagem = Personagem(cor=(255, 0, 0), tamanho_x = 50, tamanho_y = 50, velocidade = 2, posicao_x = 375, posicao_y = 500)
        self.itemRuim = ItemRuim(0, 300)

        # Variável para controlar a execução do jogo
        self.is_running = True

    def run(self):
        # Executa o loop principal do jogo
        while self.is_running:
            self.screen.fill((255, 255, 255))
            self.handle_input()
            self.update()
            self.render()
            
            # Verificar teclas pressionadas
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                self.personagem.andar_esquerda()
            if teclas[pygame.K_RIGHT]:
                self.personagem.andar_direita()

    def handle_input(self):
        # Lida com a entrada do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        # Verificar colisão entre personagem e item ruim
        if self.checa_colisao(self.personagem, self.itemRuim):
            self.personagem.coletar_item(self.itemRuim)
            # Aqui você pode adicionar a lógica para o que acontece quando ocorre uma colisão
            # Por exemplo, pode reiniciar a posição do item ruim
            self.itemRuim.reseta_posicao()

    def render(self):
        # Renderiza o estado do jogo na tela
        self.screen.fill((255, 255, 255))
        self.personagem.desenhar(self.screen)
        self.itemRuim.draw(self.screen)
        self.itemRuim.update()

        pygame.display.flip()
        self.relogio.tick(60)

    def cleanup(self):
        # Limpa recursos alocados pelo jogo
        pygame.quit()

    def checa_colisao(self, personagem, itemRuim):
        # Verificar colisão entre dois objetos
        return (personagem.posicao_x < itemRuim.x + itemRuim.radius and
                personagem.posicao_x + personagem.tamanho_x > itemRuim.x and
                personagem.posicao_y < itemRuim.y + itemRuim.radius and
                personagem.posicao_y + personagem.tamanho_y > itemRuim.y)