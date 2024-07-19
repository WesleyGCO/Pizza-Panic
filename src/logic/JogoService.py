from data.FaseCinco import FaseCinco
from data.FaseDois import FaseDois
from data.FaseQuatro import FaseQuatro
from data.FaseTres import FaseTres
from data.FaseUm import FaseUm
from presentation.PlacarFaseUI import PlacarFaseUI
import pygame # type: ignore

from data.Fase import Fase
from data.Jogo import Jogo

from logic.PersonagemService import PersonagemService
from logic.FaseService import FaseService

from presentation.JogoUI import JogoUI
from presentation.FaseUI import FaseUI

class JogoService:
  
    def __init__(self):
        self.jogo_model = Jogo()
        self.personagem_servico = PersonagemService()

    def iniciar_jogo(self, jogo_servico):
        pygame.init()

        self.tela_altura = 800
        self.tela_largura = 600
        self.tela = pygame.display.set_mode((self.tela_altura, self.tela_largura))
        pygame.display.set_caption("Pizza Panic")

        self.jogo_view = JogoUI(self.tela, self.tela_altura, self.tela_largura)

        self.jogo_servico = jogo_servico

        rodando = True
        while rodando:
            if (self.jogo_view.renderizar_menu_inicial()):
                self.jogo_model.setar_fase(1)
                self.iniciar_fase(self.jogo_model.fase_atual)

            if(self.jogo_model.fase_atual == 5):
                self.encerrar_jogo()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

        pygame.quit()

    def iniciar_fase(self, numero_fase):
        self.prox_fase = False

        rodar_menu_fase = True

        while rodar_menu_fase:
            if (numero_fase == 1):
                faseUm = FaseUm(1, self.jogo_view.personagem, self.jogo_view.itens_ruins, 30)
                faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                    self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                    self.jogo_model.gravidade)
                faseController = FaseService(faseUm, faseView, self.jogo_servico)
                faseController.iniciar()

                if (faseUm.concluida == True):
                    faseUm.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 2
                        self.jogo_view.renderizar_menu_fase(self.jogo_model, numero_fase)
                        numero_fase = self.jogo_model.fase_atual

            if (numero_fase == 2):
                faseDois = FaseDois(2, self.jogo_view.personagem, self.jogo_view.itens_ruins, 45)
                faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                    self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                    self.jogo_model.gravidade)
                faseController = FaseService(faseDois, faseView, self.jogo_servico)
                faseController.iniciar()

                if (faseDois.concluida == True):
                    faseDois.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 3
                        self.jogo_view.renderizar_menu_fase(self.jogo_model, numero_fase)

            if (numero_fase == 3):
                faseTres = FaseTres(3, self.jogo_view.personagem, self.jogo_view.itens_ruins, 60)
                faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                    self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                    self.jogo_model.gravidade)
                faseController = FaseService(faseTres, faseView, self.jogo_servico)
                faseController.iniciar()

                if (faseTres.concluida == True):
                    faseTres.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 4
                        self.jogo_view.renderizar_menu_fase(self.jogo_model, numero_fase)

            if (numero_fase == 4):
                faseQuatro = FaseQuatro(4, self.jogo_view.personagem, self.jogo_view.itens_ruins, 75)
                faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                    self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                    self.jogo_model.gravidade)
                faseController = FaseService(faseQuatro, faseView, self.jogo_servico)
                faseController.iniciar()

                if (faseQuatro.concluida == True):
                    faseQuatro.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 5
                        self.jogo_view.renderizar_menu_fase(self.jogo_model, numero_fase)

            if (numero_fase == 5):
                faseCinco = FaseCinco(5, self.jogo_view.personagem, self.jogo_view.itens_ruins, 90)
                faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                    self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                    self.jogo_model.gravidade)
                faseController = FaseService(faseCinco, faseView, self.jogo_servico)
                faseController.iniciar()

                if (faseCinco.concluida == True):
                    faseCinco.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 6
                        rodar_menu_fase = False
                        break


    pygame.init()

    def encerrar_jogo(self):
        pygame.quit()