import pygame # type: ignore

from logic.ItemService import ItemService
from logic.PersonagemService import PersonagemService

from presentation.MenuInicialUI import MenuInicialUI

class JogoUI:
    def __init__(self, tela, tela_altura, tela_largura):
        self.tela = tela
        self.menu_inicial = MenuInicialUI(self.tela)
        pygame.init()
        
        self.item_controller = ItemService()
        self.personagem_servico = PersonagemService()
        
        self.fonte = pygame.font.Font(None, 30)   
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.9
        self.personagem = self.personagem_servico.criar_personagem(tela_largura, tela_altura, self.personagem_posicao_x_ratio, self.personagem_posicao_y_ratio)
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
