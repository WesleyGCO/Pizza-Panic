from adapters.primary import pygame_input_adapter, pygame_output_adapter

class MenuScoreboardUI:
    def __init__(self, tela_altura, tela_largura):
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        self.pontuacoes = []  # Lista para armazenar pontuações
        self.carregar_pontuacoes()  # Carrega pontuações do arquivo

        # Configuração do botão "Voltar ao menu"
        botao_largura = 200
        botao_altura = 50
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = int(tela_altura * 0.75)
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

    def carregar_pontuacoes(self):
        pass

    def renderizar_scoreboard(self):
        pass

    def renderizar_botao(self, botao):
        pass

    def lidar_entrada_menu_scoreboard(self, evento):
        
        """Lida com a entrada do jogador na tela do scoreboard."""
        if pygame_input_adapter.clicado(evento) and self.botao_voltar_menu.collidepoint(evento.pos):
            return "Voltar ao menu"
