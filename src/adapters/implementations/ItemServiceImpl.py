from core.interfaces.ItemInterface import ItemInterface
from core.entities.Personagem import Personagem
from core.entities.Item import Item

from ports.ui.ItemUI import ItemUI

class ItemServiceImpl(ItemInterface):
    def __init__(self):
        self.item_view = ItemUI()
    
    def criar_item(self):
        return self.item_view.criar_item()

    def desenhar_item(self, itemDesenho, tela):        
        if isinstance(itemDesenho, Item):
            self.item_view.desenhar_item(itemDesenho, tela)

    def movimento_item(self, itemMovimenta, tempo):
        # Verifica se o objeto é do tipo Item
        if isinstance(itemMovimenta, Item):
            itemMovimenta.processamento_fisica(tempo)

    def reinicia_item(self, itemReinicia):
        if isinstance(itemReinicia, Item):
            return self.criar_item()

    def checa_colisao(self, personagem, itemColide):
        if isinstance(personagem, Personagem):
            if isinstance(itemColide, Item):
                return (
                    personagem.posicao.x < itemColide.posicao.x + itemColide.largura and
                    personagem.posicao.x + personagem.largura > itemColide.posicao.x and
                    personagem.posicao.y < itemColide.posicao.y + itemColide.altura and
                    personagem.posicao.y + 5 > itemColide.posicao.y) # Considera apenas 5 pixels da altura do personagem