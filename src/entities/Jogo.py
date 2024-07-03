import pygame, random # type: ignore

from components.MenuInicial_componente import MenuInicial
from servicos.personagem_servico import Personagem_Servico
from servicos.tempo_servico import Tempo_Servico
from servicos.jogo_servico import Jogo_Servico
from servicos.item_servico import Item_Servico

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
        self.menu_inicial = MenuInicial(self.tela)
        
        # Cria a variável se jogo está rodando ou não
        self.is_running = False

    def init(self):
        pygame.init()
        
        self.item_servico = Item_Servico()
        self.personagem_servico = Personagem_Servico()
        self.tempo_servico = Tempo_Servico()
        
        self.fonte = pygame.font.Font(None, 30)   
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.9
        self.personagem = self.personagem_servico.criar_personagem(self.tela_largura, self.tela_altura, self.personagem_posicao_x_ratio, self.personagem_posicao_y_ratio)
        self.itens_ruins = [self.item_servico.criar_item() for _ in range(5)]
        
        self.is_running = True

    def iniciar_menu(self):
        rodando_menu = True
        while rodando_menu:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                resultado = self.menu_inicial.handle_eventos(evento)
                if resultado == "JOGAR":
                    rodando_menu = False
                    self.run()
            
            self.menu_inicial.renderizar()
            pygame.display.update()

    def run(self):
        while self.is_running:
            self.tela.fill((0, 0, 0))
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
            self.personagem_servico.andar_esquerda(self.personagem)
        if teclas[pygame.K_RIGHT]:
            self.personagem_servico.andar_direita(self.personagem, self.tela_altura)

    def update(self):
        # Verificar colisão entre personagem e item
        for item in self.itens_ruins:
            if self.item_servico.checa_colisao(self.personagem, item):
                self.personagem_servico.coletar_item(self.personagem, item)
                self.item_servico.reinicia_item_coletou(item)

    def render(self):
        # Renderiza o estado do jogo na tela
        self.tela.fill((147, 158, 150))

        self.jogo_servico.menu_borda(self.tela, self.tela_altura, self.tela_largura)
        
        self.personagem_servico.desenhar_personagem(self.personagem, self.tela)
        
        self.tempo_servico.atualizar_contador(self.tela, self.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)
        self.tempo_servico.contagem_regressiva(self.tela, self.tempo_inicial, self.tela_altura, self.fonte)
        
        # Desenha, movimenta e reinicia os itens
        for item in self.itens_ruins:
            self.item_servico.desenhar_item(item, self.tela)
            self.item_servico.movimento_item(item, self.gravidade)
            self.item_servico.reinicia_item_sumiu(item)

        pygame.display.flip()
        self.relogio.tick(60)

    def cleanup(self):
        pygame.quit()

    def configuracao_geral(self):
        # Posição do texto de contador
        self.posicao_x_texto = 20
        self.posicao_y_texto = 15

        # Seta o tempo inicial
        self.tempo_inicial = 60

        # Seta o valor da gravidade
        self.gravidade = 0.20

        # Seta o clock
        self.relogio = pygame.time.Clock()