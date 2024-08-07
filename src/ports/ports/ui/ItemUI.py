import random

from core.entities.Item import Item

class ItemUI:
    def __init__(self):
        self.tipos_item = list(Item.TIPOS_ITENS.keys())

    def criar_item(self):
        tipo_item = random.choice(self.tipos_item)
        return Item(tipo_item, 0, 300, 40, 40, random.uniform(300, 600), random.uniform(-200, -500))

    def desenhar_item(self, item, tela):
        item.desenhar(tela)
