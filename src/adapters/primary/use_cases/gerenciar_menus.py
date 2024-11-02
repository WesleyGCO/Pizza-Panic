from adapters.primary import pygame_input_adapter, pygame_output_adapter
from adapters.primary.ui.menu_creditos_ui import MenuCreditosUI
from adapters.primary.ui.menu_perdeu_ui import MenuPerdeuUI
from adapters.primary.ui.menu_scoreboard_ui import MenuScoreboardUI
from adapters.primary.use_cases import gerenciar_fase

def rodar_menu_inicial(menu_inicial):
    rodando_menu = True
    while rodando_menu:
        for evento in pygame_input_adapter.capturar_eventos():
            if evento.type == pygame_input_adapter.eh_sair(evento):
                pygame_output_adapter.sair()
                quit()
                
            resultado = menu_inicial.lidar_entrada_menu_inicial(evento)
            if resultado == "JOGAR":
                rodando_menu = False
                return True
            
            elif resultado == "Créditos":
                pygame_output_adapter.preencher_tela((0, 0, 0))
                rodar_menu_creditos(MenuCreditosUI(menu_inicial.tela_largura, menu_inicial.tela_altura))
            
            # elif resultado == "Scoreboard":
            #     pygame_output_adapter.preencher_tela((0, 0, 0))
            #     rodar_menu_scoreboard(MenuScoreboardUI(menu_inicial.tela_largura, menu_inicial.tela_altura))
                
        menu_inicial.renderizar_menu_inicial()
        pygame_output_adapter.atualizacao_tela()

            
def rodar_menu_fase(menu_fase, jogo_model, numero_fase):
    rodando_menu_fase = True
    while rodando_menu_fase:
        for evento in pygame_input_adapter.capturar_eventos():
            if (evento.type == pygame_input_adapter.eh_sair(evento)):
                pygame_output_adapter.sair()
                quit()
                    
            resultado_fase = menu_fase.lidar_entrada_menu_fase(evento)
            if (resultado_fase == "Próxima fase"):
                gerenciar_fase.setar_fase(jogo_model, numero_fase)
                rodando_menu_fase = False
                return True
            elif (resultado_fase == "Voltar ao menu"):
                rodando_menu_fase = False
                return False
                
        menu_fase.renderizar_menu_fase()
        pygame_output_adapter.atualizacao_tela()
    return False
    
def rodar_menu_perdeu(tela_altura, tela_largura, personagem):
    
    menu_perdeu = MenuPerdeuUI(tela_altura, tela_largura, personagem)
    
    rodando_menu_perdeu = True
    while rodando_menu_perdeu:
        for evento in pygame_input_adapter.capturar_eventos():
            if evento.type == pygame_input_adapter.eh_sair(evento):
                pygame_output_adapter.sair()
                quit()

            resultado_perdeu = menu_perdeu.lidar_entrada_menu_perdeu(evento)
            if resultado_perdeu == "Voltar ao menu":
                rodando_menu_perdeu = False
                return False

        menu_perdeu.renderizar_menu_perdeu()
        pygame_output_adapter.atualizacao_tela()
        
def rodar_menu_creditos(menu_creditos):
    rodando_menu_creditos = True
    while rodando_menu_creditos:
        for evento in pygame_input_adapter.capturar_eventos():
            if evento.type == pygame_input_adapter.eh_sair(evento):
                pygame_output_adapter.sair()
                quit()
                
            resultado = menu_creditos.lidar_entrada_menu_creditos(evento)
            if resultado == "VOLTAR":
                rodando_menu_creditos = False
        
        menu_creditos.renderizar_menu_creditos()
        pygame_output_adapter.atualizacao_tela()
        
def rodar_menu_scoreboard(menu_scoreboard):
    rodando_menu_scoreboard = True
    while rodando_menu_scoreboard:
        for evento in pygame_input_adapter.capturar_eventos():
            if evento.type == pygame_input_adapter.eh_sair(evento):
                pygame_output_adapter.sair()
                quit()
                
            resultado = menu_scoreboard.lidar_entrada_menu_scoreboard(evento)
            if (resultado == "Voltar ao menu"):
                rodando_menu_scoreboard = False
                
        menu_scoreboard.renderizar_scoreboard()
        pygame_output_adapter.atualizacao_tela()