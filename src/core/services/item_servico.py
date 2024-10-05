from adapters.primary import pygame_output_adapter
from core.interfaces.ItemInterface import ItemInterface
from application.models.Item import Item
from application.models.Personagem import Personagem
from adapters.primary.use_cases import gerenciar_item

class ItemService(ItemInterface):

    def criar_item(self):
        return gerenciar_item.criar_item()

    def desenhar_rodar_item(self, item, angulo):
        return gerenciar_item.desenhar_rodar_item(item, angulo)

    def movimento_item(self, itemMovimenta, tempo):
        # Verifica se o objeto é do tipo Item
        if isinstance(itemMovimenta, Item):
            itemMovimenta.processamento_fisica(tempo)

    def reinicia_item(self, itemReinicia):
        pygame_output_adapter.tocar_som("lancamento")
        if isinstance(itemReinicia, Item):
            return self.criar_item()

    def checa_colisao(self, personagem, itemColide):
        if isinstance(personagem, Personagem):
            if isinstance(itemColide, Item):
                return (
                    personagem.posicao.x < itemColide.posicao.x + itemColide.largura and
                    personagem.posicao.x + personagem.largura > itemColide.posicao.x and
                    personagem.posicao.y < itemColide.posicao.y + itemColide.altura and
                    personagem.posicao.y + 0.1 > itemColide.posicao.y) # Considera apenas 0.1 pixels da altura do personagem