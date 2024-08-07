import pygame # type:ignore

class MenuInicialUI:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.Font(None, 36)
        largura_tela, altura_tela = tela.get_size()
        largura_botao = 200
        altura_botao = 50
        posicao_x_botao = (largura_tela - largura_botao) // 2  # Centraliza o botão horizontalmente
        posicao_y_botao = (altura_tela - altura_botao) // 2  # Centraliza o botão verticalmente
        self.botao_jogar = pygame.Rect(posicao_x_botao, posicao_y_botao, largura_botao, altura_botao)
        self.cor_botao_hover = (5, 40, 97)
        self.cor_botao_normal = (5, 40, 97)

    def renderizar(self):
        pygame.draw.rect(self.tela, self.cor_botao_normal, self.botao_jogar)
        texto_botao = self.fonte.render("Jogar", True, (255, 255, 255))
        largura_texto, altura_texto = texto_botao.get_size()
        posicao_x_texto = self.botao_jogar.x + (self.botao_jogar.width - largura_texto) // 2  # Centraliza o texto horizontalmente no botão
        posicao_y_texto = self.botao_jogar.y + (self.botao_jogar.height - altura_texto) // 2  # Centraliza o texto verticalmente no botão
        self.tela.blit(texto_botao, (posicao_x_texto, posicao_y_texto))

    def handle_eventos(self, evento):
        if evento.type == pygame.MOUSEMOTION:
            if self.botao_jogar.collidepoint(evento.pos):
                self.cor_botao_hover = (66, 135, 245)
            else:
                self.cor_botao_hover = (200, 200, 200)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.collidepoint(evento.pos):
                return "JOGAR"
        return None
