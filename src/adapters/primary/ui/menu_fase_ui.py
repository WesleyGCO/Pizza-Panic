from adapters.primary import pygame_input_adapter, pygame_output_adapter

class MenuFaseUI:
    """
    Classe responsável pela interface do menu de fases, incluindo botões e tratamento de eventos.
    
    Esta classe gerencia a exibição do menu de fase, incluindo os botões de próxima
    ou voltar ao menu, e lida com a entrada do usuário.
    
    Métodos:
        renderizar_menu_fase(): Faz a renderização na tela do menu de fase para o jogador escolher as opções disponíveis
        lidar_entrada_menu_fase(): Lida com a entrada do jogador no menu_fase
    """
    
    def __init__(self, tela_altura, tela_largura):
        """
        Inicializa o menu de fase com os parâmetros de tela e define os botões.

        Args:
            tela_altura (int): Altura da tela do jogo.
            tela_largura (int): Largura da tela do jogo.
            
        Atributos:
            tela_largura (int): A largura da tela do jogo.
            tela_altura (int): A altura da tela do jogo.
            botao_proxima_fase (pygame.Rect): O retângulo que representa o botão de próxima fase.
            botao_voltar_menu (pygame.Rect): O retângulo que representa o botão de voltar ao menu.
            cor_botao_hover (tuple): A cor do botão quando o mouse está sobre ele.
            cor_botao_normal (tuple): A cor do botão em seu estado normal.

        Returns:
            None
        """
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura

        # Configuração dos botões
        botao_largura = 200
        botao_altura = 50
        espaco_entre_botoes = 20

        # Definir posição dos botões
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = (tela_altura - (3 * botao_altura + 2 * espaco_entre_botoes)) // 2
        
        # Criar botões
        self.botao_proxima_fase = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y + 2 * (botao_altura + espaco_entre_botoes), botao_largura, botao_altura)

        # Cores dos botões
        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

    def renderizar_menu_fase(self):
        """
        Renderiza o menu de fase, desenhando os botões e seus textos.

        Returns:
            None
        """
        # Renderizar botões
        self.renderizar_botao(self.botao_proxima_fase, "Próxima fase")
        self.renderizar_botao(self.botao_voltar_menu, "Voltar ao menu")

    def renderizar_botao(self, botao, texto):
        """
        Renderiza um botão retangular com o texto centralizado.
        Este método muda a cor do botão dependendo se o mouse está sobre ele ou não.

        Args:
            botao (pygame.Rect): Retângulo representando o botão.
            texto (str): Texto a ser exibido no botão.
        """
        
        mouse_pos = pygame_input_adapter.mouse_posicao()
        
        # Verificar se o mouse está sobre o botão
        if botao.collidepoint(mouse_pos):
            cor_atual = self.cor_botao_hover
        else:
            cor_atual = self.cor_botao_normal
        
        # Desenhar o botão
        pygame_output_adapter.desenhar_botao_retangulo(cor_atual, botao)

        # Centralizar o texto no botão
        texto_renderizado = pygame_output_adapter.renderizar_texto(texto)
        texto_largura, texto_altura = texto_renderizado.get_size()
        posicao_x_texto = botao.x + (botao.width - texto_largura) // 2
        posicao_y_texto = botao.y + (botao.height - texto_altura) // 2

        # Renderizar o texto no botão
        pygame_output_adapter.desenhar_superficie(texto_renderizado, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_fase(self, evento):
        """
        Lida com a entrada do usuário no menu de fase, verificando cliques nos botões.

        Args:
            evento (pygame.event): Evento de entrada do usuário.

        Returns:
            str: Retorna o nome do botão clicado ou None.
        """
        if pygame_input_adapter.clicado(evento):
            if self.botao_proxima_fase.collidepoint(evento.pos):
                return "Próxima fase"
            elif self.botao_voltar_menu.collidepoint(evento.pos):
                return "Voltar ao menu"
        
        return None
