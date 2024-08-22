from adapters.primary import pygame_output_adapter

class Jogo:
    def __init__(self):
        self.fase_atual = 0
        self.is_running = False
        self.posicao_x_texto = 20
        self.posicao_y_texto = 15
        self.fase_perdida = False

        # Seta o tempo inicial
        self.tempo_inicial = 60
        self.relogio = pygame_output_adapter.criar_relogio()