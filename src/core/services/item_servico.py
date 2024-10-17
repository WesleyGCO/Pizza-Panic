from adapters.primary import pygame_output_adapter
from core.interfaces.ItemInterface import ItemInterface
from application.models.Item import Item
from application.models.Personagem import Personagem
from adapters.primary.use_cases import gerenciar_item

class ItemService(ItemInterface):
    """
    Serviço responsável por gerenciar as ações relacionadas aos itens no jogo.

    Esta classe implementa a interface `ItemInterface` e lida com a criação, 
    desenho, movimento, reinício e verificação de colisão dos itens, delegando 
    parte da lógica para o caso de uso `gerenciar_item`.

    Métodos:
        criar_item: Cria um novo item.
        desenhar_rodar_item: Desenha e roda um item na tela com um ângulo específico.
        movimento_item: Aplica movimento físico a um item.
        reinicia_item: Reinicia um item e toca um som de lançamento.
        checa_colisao: Verifica a colisão entre um personagem e um item.
    """

    def criar_item(self):
        """
        Cria um novo item.

        Returns:
            Item: Instância do item criado.
        """
        return gerenciar_item.criar_item()

    def desenhar_rodar_item(self, item, angulo):
        """
        Desenha e roda o item na tela com o ângulo fornecido.

        Args:
            item (Item): Instância do item a ser desenhado e rodado.
            angulo (float): O ângulo em graus para rodar o item.

        Returns:
            None
        """
        return gerenciar_item.desenhar_rodar_item(item, angulo)

    def movimento_item(self, itemMovimenta, tempo):
        """
        Aplica o movimento físico a um item baseado no tempo.

        Args:
            itemMovimenta (Item): O item que será movimentado.
            tempo (float): O tempo decorrido que influencia a movimentação.

        Returns:
            None
        """
        # Verifica se o objeto é do tipo Item
        if isinstance(itemMovimenta, Item):
            itemMovimenta.processamento_fisica(tempo)

    def reinicia_item(self, itemReinicia):
        """
        Reinicia um item e toca um som de lançamento.

        Args:
            itemReinicia (Item): O item que será reiniciado.

        Returns:
            Item: Uma nova instância do item criado, se o item reiniciado for válido.
        """
        pygame_output_adapter.tocar_som("lancamento")
        if isinstance(itemReinicia, Item):
            return self.criar_item()

    def checa_colisao(self, personagem, itemColide):
        """
        Verifica a colisão entre um personagem e um item.

        Args:
            personagem (Personagem): Instância do personagem que colidirá com o item.
            itemColide (Item): Instância do item que será verificado para colisão.

        Returns:
            bool: Verdadeiro se há colisão, falso caso contrário.
        """
        if isinstance(personagem, Personagem):
            if isinstance(itemColide, Item):
                return (
                    personagem.posicao.x < itemColide.posicao.x + itemColide.largura and
                    personagem.posicao.x + personagem.largura > itemColide.posicao.x and
                    personagem.posicao.y < itemColide.posicao.y + itemColide.altura and
                    personagem.posicao.y + 0.1 > itemColide.posicao.y  # Considera apenas 0.1 pixels da altura do personagem
                )
