import pygame # type: ignore

from adapters.implementations.ItemServiceImpl import ItemServiceImpl
from adapters.implementations.PersonagemServiceImpl import PersonagemServiceImpl

from ports.ui.MenuFaseUI import MenuFaseUI
from ports.ui.MenuInicialUI import MenuInicialUI

class JogoUI:
    def __init__(self, tela, tela_altura, tela_largura):
        self.tela = tela
        self.menu_inicial = MenuInicialUI(self.tela)
        self.menu_fase = MenuFaseUI(self.tela)
        pygame.init()
        
        self.item_controller = ItemServiceImpl()
        self.personagem_servico = PersonagemServiceImpl()
        
        self.fonte = pygame.font.Font(None, 30)   
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.8
        self.aceleracao = 0
        self.personagem = self.personagem_servico.criar_personagem(tela_largura, tela_altura, self.personagem_posicao_x_ratio, self.personagem_posicao_y_ratio, self.aceleracao)
        self.itens_ruins = [self.item_controller.criar_item() for _ in range(5)]
        self.is_running = True

    def renderizar_menu_inicial(self):
        rodando_menu = True
        while rodando_menu:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                resultado = self.menu_inicial.handle_eventos(evento)
                if resultado == "JOGAR":
                    rodando_menu = False
                    return True  # Indica que o jogo deve iniciar a fase

            self.menu_inicial.renderizar()
            pygame.display.update()

        return False  # Indica que o jogo deve ser encerrado
    
    def renderizar_menu_fase(self, jogo_model, numero_fase):
        rodando_menu_fase = True
        while rodando_menu_fase:
            for evento in pygame.event.get():
                if (evento.type == pygame.QUIT):
                    pygame.quit()
                    quit()
                resultado = self.menu_fase.handle_eventos(evento)
                if (resultado == "Próxima fase"):
                    jogo_model.setar_fase(numero_fase)
                    rodando_menu_fase = False
                    return True
                
                if (resultado == "Reiniciar fase"):
                    jogo_model.setar_fase(numero_fase - 1)
                    rodando_menu_fase = False
                    return True
                
                if (resultado == "Voltar ao menu"):
                    rodando_menu_fase = False
                    return self.renderizar_menu_inicial()
                
            self.menu_fase.renderizar()
            pygame.display.update()
        return False
