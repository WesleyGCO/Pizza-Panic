from adapters.primary import pygame_output_adapter

class Jogo:
    """
    Classe responsável por representar o estado geral do jogo.

    Atributos:
        fase_atual (int): Representa o número da fase atual em que o jogador está.
        is_running (bool): Indica se o jogo está em execução (True) ou parado (False).
        posicao_x_texto (int): Posição no eixo X para exibição de texto na tela.
        posicao_y_texto (int): Posição no eixo Y para exibição de texto na tela.
        relogio (pygame.time.Clock): Instância do relógio do Pygame, utilizada para controlar o tempo no jogo.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Jogo, configurando os atributos padrão do jogo.

        Atributos:
            fase_atual (int): Inicia com a fase 0, indicando o início do jogo.
            is_running (bool): Define o estado inicial do jogo como parado (False).
            posicao_x_texto (int): Define a posição inicial no eixo X para exibir textos.
            posicao_y_texto (int): Define a posição inicial no eixo Y para exibir textos.
            relogio (pygame.time.Clock): Cria uma instância de relógio usando o adaptador do Pygame.
        """
        self.fase_atual = 0
        self.is_running = False
        self.posicao_x_texto = 20
        self.posicao_y_texto = 15

        # Criação de um relógio para controle de tempo do jogo
        self.relogio = pygame_output_adapter.criar_relogio()
