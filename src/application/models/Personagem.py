import pygame # type: ignore

from application.models.Objeto import Objeto
from adapters.primary import pygame_output_adapter

class Personagem(Objeto):

    def __init__(self, cor, x, y, largura, altura, aceleracao):
        super().__init__(x, y, largura, altura)
        self.cor = cor
        self.itens_coletados = 0
        self.aceleracao.x = aceleracao
        self.imagem_pizzaiolo = pygame_output_adapter.carregar_imagem("./adapters/primary/sprites/pizzaiolo.png")

    def coletar_item(self, pontuacao):
        # Adiciona o item coletado à lista de itens coletados
        self.itens_coletados += pontuacao
    
    def pegar_itens_coletados(self):
        return self.itens_coletados