import pygame
from entities.Personagem import Personagem
from servicos.gerenciamentoItens_servico import GerenciamentoItens_Servico
from servicos.tempo_servico import Tempo_Servico
from servicos.jogo_servico import Jogo_Servico

class Jogo:
    def __init__(self):
        # Configurações da janela
        self.tela_altura = 800
        self.tela_largura = 600

        # Cria a tela com o título Pizza Panic
        self.tela = pygame.display.set_mode((self.tela_altura, self.tela_largura))
        # Seta o nome do título
        pygame.display.set_caption("Pizza Panic")
        
        self.jogo_servico = Jogo_Servico()
        self.configuracao_geral()
        
        # Cria a variável se jogo está rodando ou não
        self.is_running = False

    def init(self):
        pygame.init()
        
        self.gerenciamentoItens_servico = GerenciamentoItens_Servico()
        self.tempo_servico = Tempo_Servico()
        
        self.fonte = pygame.font.Font(None, 30)   
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.9
        self.personagem = Personagem((237, 14, 178), int(self.personagem_posicao_x_ratio * self.tela_altura), int(self.personagem_posicao_y_ratio * self.tela_largura), 40, 40, 5)
        
        self.imagem_item_ruim = pygame.image.load("assets/Imagens/pizza.png")
        self.itens_ruins = [self.gerenciamentoItens_servico.criar_item() for _ in range(3)]
        
        self.is_running = True

    def run(self):
        while self.is_running:
            self.tela.fill((255, 255, 255))
            self.handle_input()
            self.update()
            self.render()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        # Verificar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.personagem.andar_esquerda()
        if teclas[pygame.K_RIGHT]:
            self.personagem.andar_direita(self.tela_altura)

    def update(self):
        # Verificar colisão entre personagem e item
        for item in self.itens_ruins:
            if self.gerenciamentoItens_servico.checa_colisao(self.personagem, item):
                self.personagem.coletar_item()
                item.reinicia_item()

    def render(self):
        # Renderiza o estado do jogo na tela
        self.tela.fill((255, 255, 255))

        self.jogo_servico.menu_borda(self.tela, self.tela_altura, self.tela_largura)
        
        self.personagem.desenhar(self.tela)
        
        self.tempo_servico.atualizar_contador(self.tela, self.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)
        self.tempo_servico.contagem_regressiva(self.tela, self.tempo_inicial, self.tela_altura, self.fonte)
        
        # Desenha, movimenta e reinicia os itens
        for item in self.itens_ruins:
            self.gerenciamentoItens_servico.desenhar_item(item, self.tela, self.imagem_item_ruim)
            self.gerenciamentoItens_servico.movimento_item(item, self.gravidade)
            self.gerenciamentoItens_servico.reinicia_item(item)

        pygame.display.flip()
        self.relogio.tick(60)

    def cleanup(self):
        pygame.quit()

    def configuracao_geral(self):
        # Posição do texto de contador
        self.posicao_x_texto = 20
        self.posicao_y_texto = 50

        # Seta o tempo inicial
        self.tempo_inicial = 60

        # Seta o valor da gravidade
        self.gravidade = 0.20

        # Seta o clock
        self.relogio = pygame.time.Clock()