from adapters.primary import pygame_output_adapter
from adapters.primary.ui.fase_ui import FaseUI
from adapters.primary.ui.jogo_ui import JogoUI
from adapters.primary.use_cases import gerenciar_fase, gerenciar_menus
from application.models.Jogo import Jogo
from adapters.primary.ui.menu_fase_ui import MenuFaseUI
from adapters.primary.ui.menu_inicial_ui import MenuInicialUI
from core.services.item_servico import ItemService
from core.services.personagem_servico import PersonagemService
from core.services.tempo_servico import TempoService

def iniciar_jogo(tamanho_tela_largura, tamanho_tela_altura):
    """
    Inicia o jogo, configurando os serviços e interfaces gráficas necessárias.
    
    Este método é responsável por iniciar o jogo criando instâncias dos modelos e serviços,
    bem como os menus e interfaces gráficas de acordo com as dimensões da tela.

    Args:
        tamanho_tela_largura (int): A largura da tela do jogo.
        tamanho_tela_altura (int): A altura da tela do jogo.

    Atributos:
        jogo_model (Jogo): Instância da classe Jogo, que representa o estado do jogo.
        personagem_servico (PersonagemService): Serviço que gerencia as ações do personagem no jogo.
        item_servico (ItemService): Serviço que gerencia os itens do jogo.
        tempo_servico (TempoService): Serviço responsável por controlar o tempo do jogo.
        menu_inicial (MenuInicialUI): Interface do menu inicial, configurada com base nas dimensões da tela.
        menu_fase (MenuFaseUI): Interface do menu de fases, configurada com base nas dimensões da tela.
    
    Funciona em um loop até que o menu inicial seja aceito e o jogo seja executado.
    """
    jogo_model = Jogo()
    personagem_servico = PersonagemService()
    item_servico = ItemService()
    tempo_servico = TempoService()
    menu_inicial = MenuInicialUI(tamanho_tela_altura, tamanho_tela_largura)
    menu_fase = MenuFaseUI(tamanho_tela_largura, tamanho_tela_altura)
    
    while True:
        if gerenciar_menus.rodar_menu_inicial(menu_inicial):
            jogo_ui = JogoUI(tamanho_tela_largura, tamanho_tela_altura, item_servico, personagem_servico)
            fase_ui = FaseUI(tamanho_tela_altura, tamanho_tela_largura, jogo_model.relogio, jogo_model.posicao_x_texto, jogo_model.posicao_y_texto)
    
            executar_jogo(jogo_model, jogo_ui, fase_ui, menu_fase, item_servico, personagem_servico, tempo_servico, tamanho_tela_largura, tamanho_tela_altura)
            break

def executar_jogo(jogo_model, jogo_ui, fase_ui, menu_fase, item_servico, personagem_servico, tempo_servico,
                  tamanho_tela_largura, tamanho_tela_altura):
    """
    Executa o ciclo principal do jogo, gerenciando as fases e a lógica de jogo.

    Args:
        jogo_model (Jogo): Modelo do jogo contendo as informações do estado atual.
        jogo_ui (JogoUI): Interface gráfica do jogo, usada para renderizar elementos na tela.
        fase_ui (FaseUI): Interface gráfica específica das fases.
        menu_fase (MenuFaseUI): Menu usado para gerenciar as fases.
        item_servico (ItemService): Serviço de gerenciamento de itens do jogo.
        personagem_servico (PersonagemService): Serviço de gerenciamento do personagem.
        tempo_servico (TempoService): Serviço de controle do tempo.
        tamanho_tela_largura (int): Largura da tela do jogo.
        tamanho_tela_altura (int): Altura da tela do jogo.

    Funciona em um loop contínuo até que a fase seja finalizada ou o jogo seja reiniciado.
    """
    while True:
        gerenciar_fase.setar_fase(jogo_model, 1)
        if not gerenciar_fase.iniciar_fase(menu_fase, jogo_model, jogo_ui, fase_ui, 
                                           item_servico, personagem_servico, tempo_servico, tamanho_tela_largura, tamanho_tela_altura):
            pygame_output_adapter.preencher_tela((0, 0, 0))
            iniciar_jogo(tamanho_tela_largura, tamanho_tela_altura)
            break

def encerrar_jogo():
    """
    Encerra o jogo e fecha a janela do Pygame.
    """
    pygame_output_adapter.sair()

def setar_jogo_perdido(jogo_model):
    """
    Marca o jogo como perdido.

    Args:
        jogo_model (Jogo): Instância do modelo de jogo que terá o estado de fase perdida atualizado.
    """
    jogo_model.fase_perdida = True
