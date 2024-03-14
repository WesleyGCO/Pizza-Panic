import random

from entities.Item import Item
from entities.Personagem import Personagem

class Item_Servico:
    
    def criar_item():
        itemCriado = Item(0, 300, 40, 40, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória)
        return itemCriado
    
    def desenhar_item(itemDesenho, screen, imagem):
        # Verifica se o objeto é do tipo Item
        if isinstance(itemDesenho, Item):
            itemDesenho.desenhar(screen, imagem)

    def movimento_item(itemMovimenta, gravidade):
        # Verifica se o objeto é do tipo Item
        if isinstance(itemMovimenta, Item):
            itemMovimenta.movimento_parabolico(gravidade)

    def reinicia_item(itemReinicia):
        # Verifica se o objeto é do tipo Item
        if isinstance(itemReinicia, Item):
            if itemReinicia.posicao.y > 600:
                itemReinicia.reinicia_item()

    def checa_colisao(personagem, itemColide):
        if isinstance(personagem, Personagem):
            if isinstance(itemColide, Item):
                return(personagem.posicao.x < itemColide.posicao.x + itemColide.largura and 
                    personagem.posicao.x + personagem.altura > itemColide.posicao.x and 
                    personagem.posicao.y < itemColide.posicao.y + itemColide.largura and 
                    personagem.posicao.y + personagem.altura > itemColide.posicao.y)