from adapters.primary import pygame_output_adapter, pygame_input_adapter

class MenuInicialUI:
    """
    Classe responsável pela interface do menu inicial do jogo.

    Esta classe gerencia a exibição do menu inicial, incluindo o botão de jogar, e lida com a entrada do usuário.

    Métodos:
        renderizar_menu_inicial(): Faz a renderização na tela do menu inicial para o jogador escolher as opções disponíveis
        lidar_entrada_menu_inicial(): Lida com a entrada do jogador no menu_inicial
    """
    
    def __init__(self, tela_largura, tela_altura):
        """
        Inicializa a interface do menu inicial.

        Args:
            tela_largura (int): A largura da tela do jogo.
            tela_altura (int): A altura da tela do jogo.

        Atributos:
            tela_largura (int): A largura da tela do jogo.
            tela_altura (int): A altura da tela do jogo.
            botao_jogar (pygame.Rect): O retângulo que representa o botão de jogar.
            cor_botao_hover (tuple): A cor do botão quando o mouse está sobre ele.
            cor_botao_normal (tuple): A cor do botão em seu estado normal.

        Returns:
            None
        """
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        botao_largura = 200
        botao_altura = 50
        espaco_entre_botoes = 20  # Espaço entre os botões

        # Calculando a posição inicial dos botões para centralizar o conjunto
        total_altura_botoes = 3 * botao_altura + 2 * espaco_entre_botoes
        posicao_inicial_y = (tela_altura - total_altura_botoes) // 2

        botao_posicao_x = (tela_largura - botao_largura) // 2
        self.botao_jogar = pygame_output_adapter.criar_retangulo(botao_posicao_x, posicao_inicial_y, botao_largura, botao_altura)
        self.botao_creditos = pygame_output_adapter.criar_retangulo(botao_posicao_x, posicao_inicial_y + botao_altura + espaco_entre_botoes, botao_largura, botao_altura)
        self.botao_scoreboard = pygame_output_adapter.criar_retangulo(botao_posicao_x, posicao_inicial_y + 2 * (botao_altura + espaco_entre_botoes), botao_largura, botao_altura)

        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

        # Carregar a imagem com blur no Pygame
        self.imagem = pygame_output_adapter.carregar_imagem("./adapters/primary/sprites/fundo8x6_new.png")
        self.imagem_redimensionada = pygame_output_adapter.redimensionar_imagem(self.imagem, self.tela_largura, self.tela_altura)

    def renderizar_menu_inicial(self):
        """
        Renderiza o menu inicial na tela, incluindo o botão de jogar.

        Este método também toca a música do menu inicial e muda a cor 
        do botão dependendo se o mouse está sobre ele ou não.

        Returns:
            None
        """
        pygame_output_adapter.desenhar_superficie(self.imagem_redimensionada, (0, 0))
        self.renderizar_botao(self.botao_jogar, "Jogar")
        self.renderizar_botao(self.botao_creditos, "Créditos")
        self.renderizar_botao(self.botao_scoreboard, "Scoreboard")

    def renderizar_botao(self, botao, texto):
        mouse_pos = pygame_input_adapter.mouse_posicao()
        
        # Verificar se o mouse está sobre o botão
        if botao.collidepoint(mouse_pos):
            cor_atual = self.cor_botao_hover
        else:
            cor_atual = self.cor_botao_normal
        
        pygame_output_adapter.desenhar_botao_retangulo(cor_atual, botao)

        texto_botao = pygame_output_adapter.renderizar_texto(texto)
        largura_texto, altura_texto = texto_botao.get_size()
        posicao_x_texto = botao.x + (botao.width - largura_texto) // 2
        posicao_y_texto = botao.y + (botao.height - altura_texto) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_inicial(self, evento):
        """
        Lida com a entrada do usuário no menu inicial.

        Args:
            evento (Evento): O evento gerado pela entrada do usuário.

        Returns:
            str: Retorna "JOGAR" se o botão de jogar for clicado, caso contrário, retorna None.
        """
        if (pygame_input_adapter.clicado(evento)):
            pygame_output_adapter.parar_som("menu_inicial")
            if (self.botao_jogar.collidepoint(evento.pos)):
                return "JOGAR"
            if (self.botao_creditos.collidepoint(evento.pos)):
                return "Créditos"
            if (self.botao_scoreboard.collidepoint(evento.pos)):
                return "Scoreboard"

        return None
