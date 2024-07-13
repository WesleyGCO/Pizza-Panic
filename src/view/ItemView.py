import random
from models.Espatula import Espatula
from models.Pano import Pano
from models.Pizza import Pizza


class ItemView:
    def __init__(self):
        self.classes_item = [Pizza, Pano, Espatula]

    def criar_item(self):
        classe_item = random.choice(self.classes_item)
        itemCriado = classe_item(0, 300, 40, 40, random.uniform(5, 10), random.uniform(-5, -15))  # Velocidade horizontal inicial aleatória)
        return itemCriado

    def desenhar_item(self, itemDesenho, tela):        
        if any(isinstance(itemDesenho, classe) for classe in self.classes_item):
            itemDesenho.desenhar(tela)
