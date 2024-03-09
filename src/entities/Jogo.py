import pygame, random
from entities.ItemRuim import ItemRuim
from entities.Personagem import Personagem
from servicos.gerenciamentoItens_servico import GerenciamentoItens_Servico
from servicos.tempo_servico import Tempo_Servico
from servicos.jogo_servico import Jogo_Servico

class Jogo:
    def __init__(self):

        # Configuraçõe s da janela
        self.screen_width = 800
        self.screen_height = 600
        
        # Cria a tela com o título Pizza Panic
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        # Seta o nopme do título
        pygame.display.set_caption("Pizza Panic")
        
        self.jogo_servico = Jogo_Servico()
        self.configuracao_geral()

        # Cria a variável se jogo está rodando ou não
        self.is_running = False

    def init(self):
        # Inicializa o Pygame
        pygame.init()

        self.gerenciamentoItens_servico = GerenciamentoItens_Servico()
        self.tempo_servico = Tempo_Servico()

        # Inicia uma fonte que podemos utilizar dentro do código
        self.fonte = pygame.font.Font(None, 30)   
        
        # Cria o personagem
        self.personagem = Personagem(cor=(255, 0, 0), tamanho_x = 50, tamanho_y = 50, velocidade = 5, posicao_x = 375, posicao_y = 500)
        
        # Cria o itemRuim
        self.itemRuim = self.gerenciamentoItens_servico.criar_item()
        self.itemRuim2 = self.gerenciamentoItens_servico.criar_item()
        self.itemRuim3 = self.gerenciamentoItens_servico.criar_item()

        # Variável para controlar a execução do jogo
        self.is_running = True

    def run(self):
        # Executa o loop principal do jogo
        while self.is_running:
            # Cria a janela na cor desejada
            self.screen.fill((255, 255, 255))
            
            # Métodos gerais
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
        if self.gerenciamentoItens_servico.checa_colisao(self.personagem, self.itemRuim):
            # Contagem para a coleta de item
            self.personagem.coletar_item(self.itemRuim)
            # Reinicia a posição do item
            self.itemRuim.reinicia()

        # Verificar colisão entre personagem e item ruim2
        if self.gerenciamentoItens_servico.checa_colisao(self.personagem, self.itemRuim2):
            # Contagem para a coleta de item
            self.personagem.coletar_item(self.itemRuim2)
            # Reinicia a posição do item
            self.itemRuim2.reinicia()

        # Verificar colisão entre personagem e item ruim
        if self.gerenciamentoItens_servico.checa_colisao(self.personagem, self.itemRuim3):
            # Contagem para a coleta de item
            self.personagem.coletar_item(self.itemRuim3)
            # Reinicia a posição do item
            self.itemRuim3.reinicia()

    def render(self):
        # Renderiza o estado do jogo na tela
        self.screen.fill((255, 255, 255))

        self.jogo_servico.menu_borda(self.screen, self.screen_width, self.screen_width)

        # Desenha o personagem na tela
        self.personagem.desenhar(self.screen)

        # Atualiza o contador
        self.tempo_servico.atualizar_contador(self.screen, self.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)

        # Contagem regressiva
        self.tempo_servico.contagem_regressiva(self.screen, self.tempo_inicial, self.screen_width, self.fonte)

        # Desenha os itens na tela
        self.gerenciamentoItens_servico.desenhar_item(self.itemRuim, self.screen)
        self.gerenciamentoItens_servico.desenhar_item(self.itemRuim2, self.screen)
        self.gerenciamentoItens_servico.desenhar_item(self.itemRuim3, self.screen)

        # Seta o movimento parabólico do item
        self.gerenciamentoItens_servico.movimento_item(self.itemRuim, self.gravidade)
        self.gerenciamentoItens_servico.movimento_item(self.itemRuim2, self.gravidade)
        self.gerenciamentoItens_servico.movimento_item(self.itemRuim3, self.gravidade)

        # Reinicia a posição do item
        self.gerenciamentoItens_servico.reinicia_item(self.itemRuim)
        self.gerenciamentoItens_servico.reinicia_item(self.itemRuim2)
        self.gerenciamentoItens_servico.reinicia_item(self.itemRuim3)

        pygame.display.flip()
        self.relogio.tick(60)

    def cleanup(self):
        # Limpa recursos alocados pelo jogo
        pygame.quit()

    def configuracao_geral(self):
        # Posição do text de contador
        self.posicao_x_texto = 20
        self.posicao_y_texto = 50

        # Seta o tempo inicial
        self.tempo_inicial = 60

        # Seta o valor da gravidade
        self.gravidade = 0.20

        # Seta o clock
        self.relogio = pygame.time.Clock()