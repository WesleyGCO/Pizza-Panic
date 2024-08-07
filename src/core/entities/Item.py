import pygame

from core.entities.Objeto import Objeto

class Item(Objeto):
    TIPOS_ITENS = {
        "pizza": {
            "imagem": pygame.image.load("./assets/Imagens/pizza.png"),
            "pontuacao": 5
        },
        "pano": {
            "imagem": pygame.image.load("./assets/Imagens/pano.png"),
            "pontuacao": -3
        },
        "espatula": {
            "imagem": pygame.image.load("./assets/Imagens/espatula.png"),
            "pontuacao": -2
        }
    }

    def __init__(self, tipo, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.tipo = tipo
        self.imagem = self.TIPOS_ITENS[tipo]["imagem"]
        self.pontuacao_valor = self.TIPOS_ITENS[tipo]["pontuacao"]
        self.velocidade.x = vx
        self.velocidade.y = vy
        self.aceleracao.y = 1000

    def desenhar(self, tela):
        super().desenhar(tela, self.imagem)

    def pontuacao(self):
        return self.pontuacao_valor
