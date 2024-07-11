from entities.FaseUm import FaseUm
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

        self.relogio = pygame.time.Clock()

    def init(self):
        pygame.init()
        
        self.item_servico = Item_Servico()
        self.personagem_servico = Personagem_Servico()
        
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
                    self.iniciar_fase(1)
            
            self.menu_inicial.renderizar()
            pygame.display.update()

    def iniciar_fase(self, numero_fase):
        if numero_fase == 1:
            fase = FaseUm(numero_fase, self.tela, self.tela_altura, 
                          self.tela_largura, self.personagem, self.itens_ruins,
                          self.tempo_inicial, self.posicao_x_texto, self.posicao_y_texto, self.fonte, self.gravidade, self.relogio)

        fase.iniciar()

    def run(self):
        self.iniciar_fase(1)

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