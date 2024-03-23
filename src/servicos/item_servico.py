import random

from entities.Espatula import Espatula
from entities.Pano import Pano
from entities.Pizza import Pizza
from entities.Personagem import Personagem

class Item_Servico:

    def __init__(self):
        self.classes_item = [Pizza, Pano, Espatula]
    
    def criar_item(self):
        classe_item = random.choice(self.classes_item)
        itemCriado = classe_item(0, 300, 40, 40, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória)
        return itemCriado

    def desenhar_item(self, itemDesenho, screen):        
        if any(isinstance(itemDesenho, classe) for classe in self.classes_item):
            itemDesenho.desenhar(screen)

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