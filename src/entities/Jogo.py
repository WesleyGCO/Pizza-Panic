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
        self.posicao_x_texto = 20
        self.posicao_y_texto = 50

        self.tempo_inicial = 60

        self.is_running = False

    def init(self):
        # Inicializa o Pygame
        pygame.init()

        self.fonte = pygame.font.Font(None, 30)   


        self.relogio = pygame.time.Clock()
        self.personagem = Personagem(cor=(255, 0, 0), tamanho_x = 50, tamanho_y = 50, velocidade = 5, posicao_x = 375, posicao_y = 500)
        #self.itemRuim = ItemRuim(0, 300)

        self.itemRuim = ItemRuim(0, 300, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória
        self.itemRuim2 = ItemRuim(0, 300, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória
        self.itemRuim3 = ItemRuim(0, 300, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória

        # Variável para controlar a execução do jogo
        self.is_running = True

        self.gravidade = 0.20

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
        if self.checa_colisao_ruim(self.personagem, self.itemRuim):
            self.personagem.coletar_item(self.itemRuim)
            # Aqui você pode adicionar a lógica para o que acontece quando ocorre uma colisão
            # Por exemplo, pode reiniciar a posição do item ruim
            self.itemRuim.reinicia()

        # Verificar colisão entre personagem e item ruim
        if self.checa_colisao_ruim(self.personagem, self.itemRuim2):
            self.personagem.coletar_item(self.itemRuim2)
            # Aqui você pode adicionar a lógica para o que acontece quando ocorre uma colisão
            # Por exemplo, pode reiniciar a posição do item ruim
            self.itemRuim2.reinicia()

        # Verificar colisão entre personagem e item ruim
        if self.checa_colisao_ruim(self.personagem, self.itemRuim3):
            self.personagem.coletar_item(self.itemRuim3)
            # Aqui você pode adicionar a lógica para o que acontece quando ocorre uma colisão
            # Por exemplo, pode reiniciar a posição do item ruim
            self.itemRuim3.reinicia()

    def render(self):
        # Renderiza o estado do jogo na tela
        self.screen.fill((255, 255, 255))
        self.personagem.desenhar(self.screen)
        self.atualizar_contador()
        self.contagem_regressiva()
        self.desenhar_item()
        self.movimento_item()
        self.reinicia_item()

        pygame.display.flip()
        self.relogio.tick(60)

    def cleanup(self):
        # Limpa recursos alocados pelo jogo
        pygame.quit()

    def checa_colisao_ruim(self, personagem, itemRuim):
        # Verificar colisão entre dois objetos
        return (personagem.posicao_x < itemRuim.x + itemRuim.largura and 
                personagem.posicao_x + personagem.tamanho_x > itemRuim.x and 
                personagem.posicao_y < itemRuim.y + itemRuim.largura and 
                personagem.posicao_y + personagem.tamanho_y > itemRuim.y)

    def atualizar_contador(self):
        # Obtém a quantidade de itens coletados
        quantidade_itens_coletados = self.personagem.itens_coletados

        # Desenha a quantidade de itens coletados na tela
        texto_itens_coletados = f"Coletados: {quantidade_itens_coletados}"

        superficie_texto = self.fonte.render(texto_itens_coletados, True, (17, 0, 255))
        self.screen.blit(superficie_texto, (self.posicao_x_texto, self.posicao_x_texto))

    def contagem_regressiva(self):
        self.tempo_atual = pygame.time.get_ticks() // 1000
        self.tempo_formatado = "{:.0f}".format(max(0, self.tempo_inicial - self.tempo_atual))

        self.superficie_texto_relogio = self.fonte.render(self.tempo_formatado, True, (0, 26, 255))
        self.screen.blit(self.superficie_texto_relogio, (self.screen_width - self.superficie_texto_relogio.get_width() - 10, 10))

    def desenhar_item(self):
        self.itemRuim.desenhar(self.screen)
        self.itemRuim2.desenhar(self.screen)
        self.itemRuim3.desenhar(self.screen)

    def movimento_item(self):
        self.itemRuim.movimento_parabolico(self.gravidade)
        self.itemRuim2.movimento_parabolico(self.gravidade)
        self.itemRuim3.movimento_parabolico(self.gravidade)

    def reinicia_item(self):
        if self.itemRuim.y > 600:
            self.itemRuim.reinicia()

        if self.itemRuim2.y > 600:
            self.itemRuim2.reinicia()

        if self.itemRuim3.y > 600:
            self.itemRuim3.reinicia()