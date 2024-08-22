from adapters.primary.ui.menu_fase_ui import MenuFaseUI
from adapters.primary.ui.menu_inicial import MenuInicialUI
from adapters.primary import pygame_input_adapter, pygame_output_adapter
from adapters.primary.use_cases import gerenciar_fase

class JogoUI:
    def __init__(self, tela_altura, tela_largura, item_service, personagem_service):
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.item_service = item_service
        self.personagem_service = personagem_service
        self.menu_inicial = MenuInicialUI(tela_largura, tela_altura)
        self.menu_fase = MenuFaseUI(tela_altura, tela_largura)
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.8
        self.aceleracao = 0
        self.personagem = self.personagem_service.criar_personagem(tela_altura, tela_largura, self.personagem_posicao_x_ratio, self.personagem_posicao_y_ratio, self.aceleracao)
        self.itens_ruins = [self.item_service.criar_item() for _ in range(5)]
        self.is_running = True
        
    def rodar_menu_inicial(self):
        rodando_menu = True
        
        while rodando_menu:
            for evento in pygame_input_adapter.capturar_eventos():
                if (evento.type == pygame_input_adapter.eh_sair(evento)):
                    pygame_output_adapter.sair()
                    quit()
                    
                resultado = self.menu_inicial.lidar_entrada_menu_inicial(evento)
                if (resultado == "JOGAR"):
                    rodando_menu = False
                    return True
                
            self.menu_inicial.renderizar_menu_inicial()
            pygame_output_adapter.atualizacao_tela()
            
    def rodar_menu_fase(self, jogo_model, numero_fase):
        rodando_menu_fase = True
        while rodando_menu_fase:
            for evento in pygame_input_adapter.capturar_eventos():
                if (evento.type == pygame_input_adapter.eh_sair(evento)):
                    pygame_output_adapter.sair()
                    quit()
                    
                resultado_fase = self.menu_fase.lidar_entrada_menu_fase(evento)
                if (resultado_fase == "Próxima fase"):
                    gerenciar_fase.setar_fase(jogo_model, numero_fase)
                    rodando_menu_fase = False
                    return True
                elif (resultado_fase == "Reiniciar fase"):
                    gerenciar_fase.setar_fase(jogo_model, numero_fase - 1)
                    rodando_menu_fase = False
                    return True
                elif (resultado_fase == "Voltar ao menu"):
                    rodando_menu_fase = False
                    pygame_output_adapter.preencher_tela((0,0,0))
                    return self.rodar_menu_inicial()
                
            self.menu_fase.renderizar_menu_fase()
            pygame_output_adapter.atualizacao_tela()
        return False