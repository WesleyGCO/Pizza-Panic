import pygame
from adapters.primary import pygame_output_adapter, pygame_input_adapter

class MenuCreditosUI:
    """
    Classe responsável pela interface do menu de créditos do jogo.

    Esta classe exibe as informações dos créditos, como desenvolvedores e contribuidores.
    
    Métodos:
        renderizar_menu_creditos(): Faz a renderização dos créditos na tela.
        lidar_entrada_menu_creditos(): Lida com a entrada do jogador no menu de créditos.
    """
    
    def __init__(self, tela_largura, tela_altura):
        """
        Inicializa o menu de créditos com os parâmetros de tela e define os elementos de interface.

        Args:
            tela_largura (int): Largura da tela do jogo.
            tela_altura (int): Altura da tela do jogo.
        
        Atributos:
            tela_largura (int): A largura da tela do jogo.
            tela_altura (int): A altura da tela do jogo.
            botao_voltar (pygame.Rect): O retângulo que representa o botão de voltar ao menu principal.
            cor_botao_hover (tuple): A cor do botão quando o mouse está sobre ele.
            cor_botao_normal (tuple): A cor do botão em seu estado normal.
            texto_creditos (list): Lista contendo as linhas de texto dos créditos.
        """
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        self.velocidade_rolagem = 0.1

        botao_largura = 200
        botao_altura = 50
        espaco_entre_botoes = 20
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = tela_altura - botao_altura - espaco_entre_botoes
        self.botao_voltar = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)

        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

        self.texto_creditos = [
            "Desenvolvedores:",
            "  - Pedro Augusto",
            "  - Wesley Castilho",
        ]
        
        self.posicao_y_texto = tela_altura

    def renderizar_menu_creditos(self):
        """
        Renderiza o menu de créditos na tela.

        Exibe o texto dos créditos e o botão de voltar.
        
        Returns:
            None
        """
        
        pygame_output_adapter.preencher_tela((0, 0, 0)) 

        for i, linha in enumerate(self.texto_creditos):
            texto_renderizado = pygame_output_adapter.renderizar_texto(linha)
            posicao_x_texto = (self.tela_largura - texto_renderizado.get_width()) // 2
            posicao_y_texto = self.posicao_y_texto + i * 30
            pygame_output_adapter.desenhar_superficie(texto_renderizado, (posicao_x_texto, posicao_y_texto))

        self.posicao_y_texto -= self.velocidade_rolagem

        self.renderizar_botao(self.botao_voltar, "Voltar")

    def renderizar_botao(self, botao, texto):
        """
        Renderiza um botão retangular com o texto centralizado.

        Args:
            botao (pygame.Rect): Retângulo representando o botão.
            texto (str): Texto a ser exibido no botão.
        """
        
        mouse_pos = pygame_input_adapter.mouse_posicao()
        cor_atual = self.cor_botao_hover if botao.collidepoint(mouse_pos) else self.cor_botao_normal
        pygame_output_adapter.desenhar_botao_retangulo(cor_atual, botao)

        texto_renderizado = pygame_output_adapter.renderizar_texto(texto)
        posicao_x_texto = botao.x + (botao.width - texto_renderizado.get_width()) // 2
        posicao_y_texto = botao.y + (botao.height - texto_renderizado.get_height()) // 2
        pygame_output_adapter.desenhar_superficie(texto_renderizado, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_creditos(self, evento):
        """
        Lida com a entrada do usuário no menu de créditos.

        Args:
            evento (pygame.event): Evento de entrada do usuário.

        Returns:
            str: Retorna "VOLTAR" se o botão de voltar for clicado, caso contrário, retorna None.
        """
        
        if pygame_input_adapter.clicado(evento) and self.botao_voltar.collidepoint(evento.pos):
            return "VOLTAR"
        return None
