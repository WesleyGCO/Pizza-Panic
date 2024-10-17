from core.interfaces.JogoInterface import JogoInterface

from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_jogo

class JogoService(JogoInterface):
    """
    Classe que representa o serviço do jogo.
    Esta classe é responsável por inicializar e encerrar o jogo.
    
    A classe JogoService implementa a interface JogoInterface, que define os métodos necessários para controlar o fluxo do jogo.
    Ela gerencia as configurações do jogo, inicializa o estado do jogo e finaliza as operações relacionadas ao jogo.
    
    Args:
        configuracoes (dict): Dicionário com as configurações do jogo.   
    
    Métodos:
        iniciar_jogo(): Inicializa o jogo.
        encerrar_jogo(): Encerra o jogo.
    """
    def __init__(self, configuracoes):
        """
        Construtor da classe JogoService
        Esse método é responsável por inicializar a tela do jogo e definir as dimensionalidades da tela com base nas configurações
        
        Args:
            configuracoes (dict): Dicionário com as configurações do jogo.
            
        Atributos:
            tamanho_tela_altura (int): A altura da tela do jogo, obtida das configurações.
            tamanho_tela_largura (int): A largura da tela do jogo, obtida das configurações.
            tela (pygame.Surface): A suprefície da tela do jogo criada com o Pygame.
        """
        self.tamanho_tela_altura = configuracoes['video']['screen_width']
        self.tamanho_tela_largura = configuracoes['video']['screen_height']
        pygame_output_adapter.iniciar()
        
        self.tela = pygame_output_adapter.criar_tela((self.tamanho_tela_altura, self.tamanho_tela_largura))
        pygame_output_adapter.criar_titulo("Pizza Panic")

    def iniciar_jogo(self):
        """
        Método responsável por iniciar o jogo
        Este método invoca a função "iniciar_jogo" do módulo "gerenciar_jogo", utilizando as dimensões da tela configuradas.
        """
        gerenciar_jogo.iniciar_jogo(self.tamanho_tela_largura, self.tamanho_tela_altura)
                
    def encerrar_jogo(self):
        """
        Método responsável por encerrar o jogo
        Este método invoca a função "encerrar_jogo" do módulo "gerenciar_jogo".
        """
        gerenciar_jogo.encerrar_jogo()