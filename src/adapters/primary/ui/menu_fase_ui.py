from adapters.primary import pygame_input_adapter, pygame_output_adapter

class MenuFaseUI:
    def __init__(self, tela_altura, tela_largura):
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        botao_largura = 200
        botao_altura = 50
        
        # Centraliza os botões horizontalmente
        botao_posicao_x = (tela_largura - botao_largura) // 2

        # Espaçamento vertical entre os botões
        espaco_entre_botoes = 20

        # Centraliza o primeiro botão verticalmente
        botao_posicao_y = (tela_altura - (3 * botao_altura + 2 * espaco_entre_botoes)) // 2
        
        self.botao_proxima_fase = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.botao_reiniciar = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y + botao_altura + espaco_entre_botoes, botao_largura, botao_altura)
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y + 2 * (botao_altura + espaco_entre_botoes), botao_largura, botao_altura)
        
        self.cor_botao_hover = (5, 40, 97)
        self.cor_botao_normal = (5, 40, 97)
        
    def renderizar_menu_fase(self):
        # Desenha e centraliza o texto no botão "Próxima fase"
        pygame_output_adapter.desenhar_botao_retangulo(self.cor_botao_normal, self.botao_proxima_fase)
        texto_botao_proxima = pygame_output_adapter.renderizar_texto("Próxima fase")
        texto_largura, texto_altura = texto_botao_proxima.get_size()
        posicao_x_texto_proxima = self.botao_proxima_fase.x + (self.botao_proxima_fase.width - texto_largura) // 2
        posicao_y_texto_proxima = self.botao_proxima_fase.y + (self.botao_proxima_fase.height - texto_altura) // 2

        pygame_output_adapter.desenhar_superficie(texto_botao_proxima, (posicao_x_texto_proxima, posicao_y_texto_proxima))

        # Desenha e centraliza o texto no botão "Reiniciar"
        pygame_output_adapter.desenhar_botao_retangulo(self.cor_botao_normal, self.botao_reiniciar)
        texto_botao_reiniciar = pygame_output_adapter.renderizar_texto("Reiniciar fase")
        texto_largura, texto_altura = texto_botao_reiniciar.get_size()
        posicao_x_texto_reiniciar = self.botao_reiniciar.x + (self.botao_reiniciar.width - texto_largura) // 2
        posicao_y_texto_reiniciar = self.botao_reiniciar.y + (self.botao_reiniciar.height - texto_altura) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao_reiniciar, (posicao_x_texto_reiniciar, posicao_y_texto_reiniciar))

        # Desenha e centraliza o texto no botão "Voltar ao menu"
        pygame_output_adapter.desenhar_botao_retangulo(self.cor_botao_normal, self.botao_voltar_menu)
        texto_botao_voltar_menu = pygame_output_adapter.renderizar_texto("Voltar ao menu")
        texto_largura, texto_altura = texto_botao_voltar_menu.get_size()
        posicao_x_texto_voltar_menu = self.botao_voltar_menu.x + (self.botao_voltar_menu.width - texto_largura) // 2
        posicao_y_texto_voltar_menu = self.botao_voltar_menu.y + (self.botao_voltar_menu.height - texto_altura) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao_voltar_menu, (posicao_x_texto_voltar_menu, posicao_y_texto_voltar_menu))

    def lidar_entrada_menu_fase(self, evento):
        if (pygame_input_adapter.clicado(evento)):
            if (self.botao_proxima_fase.collidepoint(evento.pos)):
                return "Próxima fase"
            elif (self.botao_reiniciar.collidepoint(evento.pos)):
                return "Reiniciar fase"
            elif (self.botao_voltar_menu.collidepoint(evento.pos)):
                return "Voltar ao menu"
        
        return None