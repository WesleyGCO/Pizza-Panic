import random

from entities.ItemRuim import ItemRuim
from entities.Personagem import Personagem

class Item_Servico:
    
    def criar_item():
        itemCriado = ItemRuim(0, 300, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória)
        return itemCriado
    
    def desenhar_item(itemDesenho, screen):
        # Verifica se o objeto é do tipo ItemRuim
        if isinstance(itemDesenho, ItemRuim):
            itemDesenho.desenhar(screen)

    def movimento_item(itemMovimenta, gravidade):
        # Verifica se o objeto é do tipo ItemRuim
        if isinstance(itemMovimenta, ItemRuim):
            itemMovimenta.movimento_parabolico(gravidade)

    def reinicia_item(itemReinicia):
        # Verifica se o objeto é do tipo ItemRuim
        if isinstance(itemReinicia, ItemRuim):
            if itemReinicia.y > 600:
                itemReinicia.reinicia()

    def checa_colisao(personagem, itemColide):
        if isinstance(personagem, Personagem):
            if isinstance(itemColide, ItemRuim):
                return(personagem.posicao_x < itemColide.x + itemColide.largura and 
                    personagem.posicao_x + personagem.tamanho_x > itemColide.x and 
                    personagem.posicao_y < itemColide.y + itemColide.largura and 
                    personagem.posicao_y + personagem.tamanho_y > itemColide.y)