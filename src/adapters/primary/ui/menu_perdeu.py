from adapters.primary import pygame_input_adapter, pygame_output_adapter


class MenuPerdeuUI:
    def __init__(self, tela_altura, tela_largura):
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        botao_largura = 200
        botao_altura = 50
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = (tela_altura - botao_altura) // 2
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.cor_botao_hover = (5, 40, 97)
        self.cor_botao_normal = (5, 40, 97)

    def renderizar_menu_perdeu(self):
        # pygame_output_adapter.tocar_som("menu_perdeu")
        pygame_output_adapter.desenhar_botao_retangulo(self.cor_botao_normal, self.botao_voltar_menu)
        texto_botao = pygame_output_adapter.renderizar_texto("Encerrar jogo e voltar ao menu")
        largura_texto, altura_texto = texto_botao.get_size()
        posicao_x_texto = self.botao_voltar_menu.x + (self.botao_voltar_menu.width - largura_texto) // 2
        posicao_y_texto = self.botao_voltar_menu.y + (self.botao_voltar_menu.height - altura_texto) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_perdeu(self, evento):
        if (pygame_input_adapter.clicado(evento)):
            if (self.botao_voltar_menu.collidepoint(evento.pos)):
                # pygame_output_adapter.parar_som("menu_perdeu")
                return "Voltar ao menu"
            
        else:
            return None