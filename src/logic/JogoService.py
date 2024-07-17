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
            if self.jogo_view.renderizar_menu_inicial():
                self.jogo_model.setar_fase(1)
                self.iniciar_fase(self.jogo_model.fase_atual)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

        pygame.quit()

    def iniciar_fase(self, numero_fase):
        if numero_fase == 1:
            faseModel = Fase(1, self.jogo_view.personagem, self.jogo_view.itens_ruins, self.jogo_model.tempo_inicial)
            faseView = FaseUI(self.tela, self.tela_altura, self.tela_largura, 
                                self.jogo_view.fonte, self.jogo_model.relogio, self.jogo_model.posicao_x_texto, self.jogo_model.posicao_y_texto, 
                                self.jogo_model.gravidade)
            faseController = FaseService(faseModel, faseView, self.jogo_servico)
            faseController.iniciar()
    pygame.init()

    def menu_borda(self, tela, tela_altura, tela_largura):
        # Desenha a borda
        pygame.draw.rect(tela, (0, 0, 0), (0, 0, tela_altura, tela_largura), 7)

        self.menu_superior = pygame.Surface((tela_altura, 50))
        self.menu_superior.fill((77, 68, 57))

        tela.blit(self.menu_superior, (0, 0))