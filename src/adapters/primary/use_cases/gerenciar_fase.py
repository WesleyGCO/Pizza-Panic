# Importações de bibliotecas padrão e internas
from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_menus
from application.models.Fase import Fase
from core.services.fase_servico import FaseService

# Funções utilitárias para gerenciar fases do jogo
def setar_fase(jogo_model, numero_fase):
    """
    Define a fase atual do jogo.
    """
    jogo_model.fase_atual = numero_fase

def criar_fase(numero_fase, personagem, itens_ruins):
    """
    Cria uma nova fase com base no número da fase, personagem e itens ruins.
    
    Args:
        numero_fase (int): Número da fase.
        personagem (Objeto): Personagem do jogo.
        itens_ruins (list): Lista de itens que devem ser evitados.

    Returns:
        Fase: Instância da classe Fase.
    """
    tempo_inicial = 60  # Tempo padrão inicial para todas as fases
    pedido = 3 + (numero_fase - 1) * 5  # Quantidade de pedidos necessária para completar a fase
    
    return Fase(numero_fase, personagem, itens_ruins, tempo_inicial, pedido)

def iniciar_fase(menu_fase, jogo_model, jogo_ui, fase_ui, item_servico, personagem_servico, tempo_servico, largura_tela, altura_tela):
    """
    Inicia uma fase do jogo e gerencia o loop principal de execução da fase.
    
    Args:
        menu_fase (Menu): Menu de controle de fases.
        jogo_model (Jogo): Modelo que contém o estado atual do jogo.
        jogo_ui (UI): Interface gráfica do jogo.
        fase_ui (UI): Interface gráfica específica da fase.
        item_servico (Servico): Serviço para manipular itens do jogo.
        personagem_servico (Servico): Serviço para manipular o personagem.
        tempo_servico (Servico): Serviço para controlar o tempo.
        largura_tela (int): Largura da tela.
        altura_tela (int): Altura da tela.
    
    Returns:
        bool: Retorna False se o jogo for encerrado.
    """
    while True:  
        fase = criar_fase(jogo_model.fase_atual, jogo_ui.personagem, jogo_ui.itens_ruins)
        
        # Instancia o serviço da fase com as dependências necessárias
        fase_service = FaseService(
            fase, fase_ui, item_servico, personagem_servico, 
            tempo_servico, jogo_model, largura_tela, altura_tela
        )
        fase_service.iniciar()
        
        # Verifica se a fase foi concluída ou perdida
        if fase.concluida:
            fase.concluir()
            pygame_output_adapter.tocar_som("conclusao_fase")
            jogo_model.fase_atual += 1  # Passa para a próxima fase
            
            # Gerencia o menu de seleção de fase e retorna ao menu principal se necessário
            if not gerenciar_menus.rodar_menu_fase(menu_fase, jogo_model, jogo_model.fase_atual):
                return False
            
        elif fase.perdida:
            fase.perdeu()
            pygame_output_adapter.tocar_som("perdeu_fase")
            pygame_output_adapter.preencher_tela((0, 0, 0))
            
            # Gerencia o menu de derrota
            if not gerenciar_menus.rodar_menu_perdeu(largura_tela, altura_tela):
                return False

# Funções auxiliares para manipular o estado da fase
def setar_fase_perdida(fase_model):
    """
    Marca a fase como perdida.
    """
    fase_model.perdida = True

def verificar_conclusao_fase(fase_model):
    """
    Verifica se a fase foi concluída com base nos pedidos coletados.

    Args:
        fase_model (Fase): Instância da fase atual.
    
    Returns:
        None
    """
    if fase_model.pedido == fase_model.pedido_coletado:
        fase_model.concluida = True
