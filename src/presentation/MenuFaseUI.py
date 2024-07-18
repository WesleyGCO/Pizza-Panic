import pygame # type:ignore

class MenuFaseUI:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.Font(None, 36)
        largura_tela, altura_tela = tela.get_size()
        largura_botao = 200
        altura_botao = 50

        # Centraliza os botões horizontalmente
        posicao_x_botao = (largura_tela - largura_botao) // 2

        # Espaçamento vertical entre os botões
        espaco_entre_botoes = 20

        # Centraliza o primeiro botão verticalmente
        posicao_y_botao = (altura_tela - (3 * altura_botao + 2 * espaco_entre_botoes)) // 2

        self.botao_jogar = pygame.Rect(posicao_x_botao, posicao_y_botao, largura_botao, altura_botao)
        self.botao_reiniciar = pygame.Rect(posicao_x_botao, posicao_y_botao + altura_botao + espaco_entre_botoes, largura_botao, altura_botao)
        self.botao_voltar_menu = pygame.Rect(posicao_x_botao, posicao_y_botao + 2 * (altura_botao + espaco_entre_botoes), largura_botao, altura_botao)

        self.cor_botao_hover = (5, 40, 97)
        self.cor_botao_normal = (5, 40, 97)

    def renderizar(self):
        # Desenha e centraliza o texto no botão "Próxima fase"
        pygame.draw.rect(self.tela, self.cor_botao_normal, self.botao_jogar)
        texto_botao_proximo = self.fonte.render("Próxima fase", True, (255, 255, 255))
        largura_texto, altura_texto = texto_botao_proximo.get_size()
        posicao_x_texto = self.botao_jogar.x + (self.botao_jogar.width - largura_texto) // 2
        posicao_y_texto = self.botao_jogar.y + (self.botao_jogar.height - altura_texto) // 2
        self.tela.blit(texto_botao_proximo, (posicao_x_texto, posicao_y_texto))

        # Desenha e centraliza o texto no botão "Reiniciar fase"
        pygame.draw.rect(self.tela, self.cor_botao_normal, self.botao_reiniciar)
        texto_botao_reiniciar = self.fonte.render("Reiniciar fase", True, (255, 255, 255))
        largura_texto, altura_texto = texto_botao_reiniciar.get_size()
        posicao_x_texto = self.botao_reiniciar.x + (self.botao_reiniciar.width - largura_texto) // 2
        posicao_y_texto = self.botao_reiniciar.y + (self.botao_reiniciar.height - altura_texto) // 2
        self.tela.blit(texto_botao_reiniciar, (posicao_x_texto, posicao_y_texto))

        # Desenha e centraliza o texto no botão "Voltar ao menu"
        pygame.draw.rect(self.tela, self.cor_botao_normal, self.botao_voltar_menu)
        texto_botao_menu = self.fonte.render("Voltar ao menu", True, (255, 255, 255))
        largura_texto, altura_texto = texto_botao_menu.get_size()
        posicao_x_texto = self.botao_voltar_menu.x + (self.botao_voltar_menu.width - largura_texto) // 2
        posicao_y_texto = self.botao_voltar_menu.y + (self.botao_voltar_menu.height - altura_texto) // 2
        self.tela.blit(texto_botao_menu, (posicao_x_texto, posicao_y_texto))

    def handle_eventos(self, evento):
        if evento.type == pygame.MOUSEMOTION:
            if self.botao_jogar.collidepoint(evento.pos):
                self.cor_botao_hover = (66, 135, 245)
            else:
                self.cor_botao_hover = (200, 200, 200)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.collidepoint(evento.pos):
                return "Próxima fase"
            elif self.botao_reiniciar.collidepoint(evento.pos):
                return "Reiniciar fase"
            elif self.botao_voltar_menu.collidepoint(evento.pos):
                return "Voltar ao menu"
        return None
