from adapters.primary.use_cases import gerenciar_personagem
from core.interfaces.PersonagemInterface import PersonagemInterface
from core.services import pontuacao_servico

class PersonagemService(PersonagemInterface):
    """
    Serviço responsável por gerenciar as ações relacionadas ao personagem no jogo.

    Esta classe implementa a interface `PersonagemInterface` e lida com a criação, 
    desenho e manipulação da pontuação do personagem, delegando parte da lógica para 
    o caso de uso `gerenciar_personagem` e o serviço `pontuacao_servico`.

    Atributos:
        pontuacao_servico (module): Módulo responsável por manipular a pontuação do personagem.
    """

    def __init__(self):
        """
        Inicializa uma nova instância do `PersonagemService`, associando o serviço de pontuação.

        Atributos:
            pontuacao_servico (module): Serviço responsável por adicionar pontuações ao personagem.
        """
        self.pontuacao_servico = pontuacao_servico

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        """
        Cria um novo personagem com base nas dimensões da tela e outras propriedades.

        Args:
            tela_largura (int): Largura da tela onde o personagem será exibido.
            tela_altura (int): Altura da tela onde o personagem será exibido.
            posicao_x_ratio (float): Proporção da posição inicial do personagem no eixo X.
            posicao_y_ratio (float): Proporção da posição inicial do personagem no eixo Y.
            aceleracao (float): Aceleração inicial do personagem.

        Returns:
            Personagem: Instância do personagem criado.
        """
        return gerenciar_personagem.criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao)

    def desenhar_personagem(self, personagem, imagens):
        """
        Desenha o personagem na tela utilizando as imagens fornecidas.

        Args:
            personagem (Personagem): Instância do personagem a ser desenhado.
            imagens (list): Lista de imagens que representam as animações ou estados do personagem.

        Returns:
            None
        """
        return gerenciar_personagem.desenhar_personagem(personagem, imagens)

    def adicionar_pontuacao(self, personagem, item):
        """
        Adiciona a pontuação ao personagem com base no item coletado.

        Args:
            personagem (Personagem): Instância do personagem que receberá a pontuação.
            item (Item): Instância do item que foi coletado, que impacta a pontuação.

        Returns:
            None
        """
        self.pontuacao_servico.adicionar_pontuacao(personagem, item)
