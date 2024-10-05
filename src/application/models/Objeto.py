from adapters.primary import pygame_output_adapter
from application.models.Vetor import Vetor
import pygame  # type: ignore

class Objeto:
    """
    Classe base para representar um objeto no jogo com propriedades físicas básicas.
    
    Args:
        x (float): Posição inicial no eixo X.
        y (float): Posição inicial no eixo Y.
        largura (int): Largura do objeto.
        altura (int): Altura do objeto.
    """
    
    def __init__(self, x, y, largura, altura):
        # Propriedades do objeto
        self.posicao = Vetor(x, y)
        self.largura = largura
        self.altura = altura

        # Posições iniciais
        self.start_x = self.posicao.x
        self.start_y = self.posicao.y

        # Vetores de velocidade e aceleração
        self.velocidade = Vetor(x=0, y=0)
        self.aceleracao = Vetor(x=0, y=0)

    def desenhar(self, tela, imagem):
        """
        Desenha o objeto na tela do jogo.
        
        Args:
            tela (pygame.Surface): Superfície onde o objeto será desenhado.
            imagem (pygame.Surface): Imagem a ser desenhada.
        """
        imagem_redimensionada = pygame.transform.scale(imagem, (self.largura, self.altura))
        tela.blit(imagem_redimensionada, (self.posicao.x, self.posicao.y))

    def processamento_fisica(self, tempo):
        """
        Atualiza a posição e velocidade do objeto de acordo com as leis básicas da física.

        Args:
            tempo (float): Intervalo de tempo para calcular o movimento.
        """
        # Atualiza a posição com base na velocidade e aceleração
        self.posicao.x += self.velocidade.x * tempo + 0.5 * self.aceleracao.x * (tempo ** 2)
        self.posicao.y += self.velocidade.y * tempo + 0.5 * self.aceleracao.y * (tempo ** 2)

        # Atualiza a velocidade com base na aceleração
        self.velocidade.x += self.aceleracao.x * tempo
        self.velocidade.y += self.aceleracao.y * tempo

    def resetar_posicao(self):
        """
        Reseta o objeto para sua posição inicial.
        """
        self.posicao.x = self.start_x
        self.posicao.y = self.start_y

    def pontuacao(self):
        """
        Método a ser implementado pelas subclasses para calcular a pontuação do objeto.
        """
        raise NotImplementedError("Método `pontuacao` deve ser implementado na subclasse.")

    def contar_pedido(self):
        """
        Retorna a quantidade de pedidos coletados pelo objeto.
        
        Returns:
            int: Quantidade de pedidos (por padrão, retorna 1).
        """
        return 1
