import random

from core.entities.Pizza import Pizza
from core.entities.Espatula import Espatula
from core.entities.Pano import Pano

class ItemUI:
    def __init__(self):
        self.classes_item = [Pano]

    def criar_item(self):
        classe_item = random.choice(self.classes_item)
        itemCriado = classe_item(0, 300, 40, 40, random.uniform(300, 600), random.uniform(-200, -500))  # Velocidade horizontal inicial aleatória)
        return itemCriado
    
    # def criar_item_novamente(self):
    #     classe_item = random.choice(self.classes_item)
    #     itemCriado = classe_item(0, 300, 40, 40, random.uniform(2, 5), -12)  # Velocidade horizontal inicial aleatória)
    #     return itemCriado

    def desenhar_item(self, itemDesenho, tela):        
        if any(isinstance(itemDesenho, classe) for classe in self.classes_item):
            itemDesenho.desenhar(tela)