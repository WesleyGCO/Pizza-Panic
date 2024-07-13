import pygame # type: ignore
from models.JogoModel import JogoModel
from models.FaseModel import FaseModel

from view.JogoView import JogoView
from view.FaseView import FaseView

from controllers.FaseController import FaseController

from servicos.personagem_servico import Personagem_Servico

class JogoController:
    def __init__(self):
        self.jogo_model = JogoModel()
        self.personagem_servico = Personagem_Servico()

    def iniciar_jogo(self):
        pygame.init()

        self.tela_altura = 800
        self.tela_largura = 600
        self.tela = pygame.display.set_mode((self.tela_altura, self.tela_largura))
        pygame.display.set_caption("Pizza Panic")

        self.jogo_view = JogoView(self.tela, self.tela_altura, self.tela_largura)

        rodando = True
        while rodando:
            if self.jogo_view.renderizar_menu_inicial():
                self.jogo_model.setar_fase(1)
                self.iniciar_fase(self.jogo_model.fase_atual)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

        pygame.quit()

    def iniciar_fase(self, numero_fase):
        if numero_fase == 1:
            faseModel = FaseModel(1, self.jogo_view.personagem, self.jogo_view.itens_ruins, self.jogo_model.tempo_inicial)
            faseView = FaseView(self.tela, self.tela_altura, self.tela_largura, 
                                self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                self.jogo_model.gravidade)
            faseController = FaseController(faseModel, faseView)
            faseController.iniciar()
