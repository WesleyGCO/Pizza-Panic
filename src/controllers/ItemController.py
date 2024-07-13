import random

from models.Espatula import Espatula
from models.Pano import Pano
from models.Pizza import Pizza
from models.Personagem import Personagem
from view.ItemView import ItemView

class ItemController:

    def __init__(self):
        self.classes_item = [Pizza, Pano, Espatula]
        self.item_view = ItemView()
    
    def criar_item(self):
        return self.item_view.criar_item()

    def desenhar_item(self, itemDesenho, tela):        
        if any(isinstance(itemDesenho, classe) for classe in self.classes_item):
            self.item_view.desenhar_item(itemDesenho, tela)

    def movimento_item(self, itemMovimenta, gravidade):
        # Verifica se o objeto é do tipo Item
        if any(isinstance(itemMovimenta, classe) for classe in self.classes_item):
            itemMovimenta.movimento_parabolico(gravidade)

    def reinicia_item_sumiu(self, itemReinicia):
        # Verifica se o objeto é do tipo Item
        if any(isinstance(itemReinicia, classe) for classe in self.classes_item):
            if itemReinicia.posicao.y > 600:
                itemReinicia.reinicia()

    def reinicia_item_coletou(self, itemReinicia):
        if any(isinstance(itemReinicia, classe) for classe in self.classes_item):
            itemReinicia.reinicia()

    def checa_colisao(self, personagem, itemColide):
        if isinstance(personagem, Personagem):
            if any(isinstance(itemColide, classe) for classe in self.classes_item):
                return(personagem.posicao.x < itemColide.posicao.x + itemColide.largura and 
                    personagem.posicao.x + personagem.altura > itemColide.posicao.x and 
                    personagem.posicao.y < itemColide.posicao.y + itemColide.largura and 
                    personagem.posicao.y + personagem.altura > itemColide.posicao.y)