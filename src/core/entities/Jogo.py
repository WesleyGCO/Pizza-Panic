import pygame # type: ignore

class Jogo:
    def __init__(self):
        self.fase_atual = 0
        self.is_running = False
        self.posicao_x_texto = 20
        self.posicao_y_texto = 15

        self.velocidade = 0.20

        # Seta o tempo inicial
        self.tempo_inicial = 60
        self.relogio = pygame.time.Clock()

    def setar_fase(self, numero):
        self.fase_atual = numero