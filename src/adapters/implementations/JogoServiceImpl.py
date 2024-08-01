import pygame #type: ignore

from adapters.implementations.FaseServiceImpl import FaseServiceImpl

from ports.ui.JogoUI import JogoUI
from ports.ui.FaseUI import FaseUI

from adapters.implementations.PersonagemServiceImpl import PersonagemServiceImpl
from core.entities.FaseUm import FaseUm
from core.entities.FaseDois import FaseDois
from core.entities.FaseTres import FaseTres
from core.entities.FaseQuatro import FaseQuatro
from core.entities.FaseCinco import FaseCinco
from core.entities.Jogo import Jogo

from core.interfaces.JogoInterface import JogoInterface

class JogoServiceImpl(JogoInterface):
    def __init__(self, settings):
        self.jogo_entidade = Jogo()
        self.personagem_servico = PersonagemServiceImpl()
        self.tamanho_tela_altura = settings['video']['screen_width']
        self.tamanho_tela_largura = settings['video']['screen_height']
        
    def iniciar_jogo(self, jogo_servico):
        pygame.init()

        self.tela = pygame.display.set_mode((self.tamanho_tela_altura, self.tamanho_tela_largura))
        pygame.display.set_caption("Pizza Panic")

        self.jogo_ui = JogoUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura)

        self.jogo_servico = jogo_servico

        rodando = True
        while rodando:
            if (self.jogo_ui.renderizar_menu_inicial()):
                self.jogo_entidade.setar_fase(1)
                self.iniciar_fase(self.jogo_entidade.fase_atual)

            if(self.jogo_entidade.fase_atual == 5):
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
                fase_um = FaseUm(1, self.jogo_ui.personagem, self.jogo_ui.itens_ruins, 30)
                fase_ui_um = FaseUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura, 
                                    self.jogo_ui.fonte, self.jogo_entidade.relogio, self.jogo_entidade.posicao_x_texto, self.jogo_entidade.posicao_y_texto, 
                                    self.jogo_entidade.velocidade)
                fase_servico = FaseServiceImpl(fase_um, fase_ui_um, self.jogo_servico, self.jogo_ui)
                fase_servico.iniciar()

                if (fase_um.concluida == True):
                    fase_um.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 2
                        self.jogo_ui.renderizar_menu_fase(self.jogo_entidade, numero_fase)
                        numero_fase = self.jogo_entidade.fase_atual

            if (numero_fase == 2):
                fase_dois = FaseDois(2, self.jogo_ui.personagem, self.jogo_ui.itens_ruins, 45)
                fase_ui_dois = FaseUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura, 
                                    self.jogo_ui.fonte, self.jogo_entidade.relogio, self.jogo_entidade.posicao_x_texto, self.jogo_entidade.posicao_y_texto, 
                                    self.jogo_entidade.velocidade)
                fase_servico = FaseServiceImpl(fase_dois, fase_ui_dois, self.jogo_servico, self.jogo_ui)
                fase_servico.iniciar()

                if (fase_dois.concluida == True):
                    fase_dois.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 3
                        self.jogo_ui.renderizar_menu_fase(self.jogo_entidade, numero_fase)

            if (numero_fase == 3):
                fase_tres = FaseTres(3, self.jogo_ui.personagem, self.jogo_ui.itens_ruins, 60)
                fase_ui_tres = FaseUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura, 
                                    self.jogo_ui.fonte, self.jogo_entidade.relogio, self.jogo_entidade.posicao_x_texto, self.jogo_entidade.posicao_y_texto, 
                                    self.jogo_entidade.velocidade)
                fase_servico = FaseServiceImpl(fase_tres, fase_ui_tres, self.jogo_servico, self.jogo_ui)
                fase_servico.iniciar()

                if (fase_tres.concluida == True):
                    fase_tres.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 4
                        self.jogo_ui.renderizar_menu_fase(self.jogo_entidade, numero_fase)

            if (numero_fase == 4):
                fase_quatro = FaseQuatro(4, self.jogo_ui.personagem, self.jogo_ui.itens_ruins, 75)
                fase_ui_quatro = FaseUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura, 
                                    self.jogo_ui.fonte, self.jogo_entidade.relogio, self.jogo_entidade.posicao_x_texto, self.jogo_entidade.posicao_y_texto, 
                                    self.jogo_entidade.velocidade)
                fase_servico = FaseServiceImpl(fase_quatro, fase_ui_quatro, self.jogo_servico, self.jogo_ui)
                fase_servico.iniciar()

                if (fase_quatro.concluida == True):
                    fase_quatro.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 5
                        self.jogo_ui.renderizar_menu_fase(self.jogo_entidade, numero_fase)

            if (numero_fase == 5):
                fase_cinco = FaseCinco(5, self.jogo_ui.personagem, self.jogo_ui.itens_ruins, 90)
                fase_ui_cinco = FaseUI(self.tela, self.tamanho_tela_altura, self.tamanho_tela_largura, 
                                    self.jogo_ui.fonte, self.jogo_entidade.relogio, self.jogo_entidade.posicao_x_texto, self.jogo_entidade.posicao_y_texto, 
                                    self.jogo_entidade.velocidade)
                fase_servico = FaseServiceImpl(fase_cinco, fase_ui_cinco, self.jogo_servico, self.jogo_ui)
                fase_servico.iniciar()

                if (fase_cinco.concluida == True):
                    fase_cinco.concluir()
                    self.prox_fase = True
                    if (self.prox_fase):
                        numero_fase = 6
                        rodar_menu_fase = False
                        break


    pygame.init()

    def encerrar_jogo(self):
        pygame.quit()