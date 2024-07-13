from models.Objeto import Objeto
import pygame # type: ignore

class Pano(Objeto):
    def __init__(self, x, y, largura, altura, vx, vy):
        super().__init__(x, y, largura, altura)
        self.vx = vx
        self.vy = vy
        self.imagem_pano = pygame.image.load("./assets/Imagens/Pano 300.png")

    def desenhar(self, tela):
        tela.blit(pygame.transform.scale(self.imagem_pano, (self.largura, self.altura)), (self.posicao.x, self.posicao.y))

    def movimento_parabolico(self, gravidade):
        self.atualiza(self.vx, self.vy)
        self.vy += gravidade

    def reinicia(self):
        super().reinicia_item()

    def pontuacao(self):
        return -3