import pygame #type: ignore

from core.interfaces.TempoInterface import TempoInterface

class TempoServiceImpl(TempoInterface):
    def atualizar_contador(self, tela, personagem, posicao_x_texto, posicao_y_texto, fonte):
        # Obtém a quantidade de itens coletados
        quantidade_itens_coletados = personagem.itens_coletados

        # Desenha a quantidade de itens coletados na tela
        texto_itens_coletados = f"Pontuação: {quantidade_itens_coletados}"

        # Cria a superfície do texto
        superficie_texto = fonte.render(texto_itens_coletados, True, (0, 0, 0))
        tela.blit(superficie_texto, (posicao_x_texto, posicao_y_texto))

    def contagem_regressiva(self, tela, tempo_inicial, tela_altura, fonte):
        # Cria o tempo atual
        self.tempo_atual = pygame.time.get_ticks() // 1000
        # Formata o tempo
        self.tempo_formatado = "{:.0f}".format(max(0, tempo_inicial - self.tempo_atual))

        # Cria a superfície para o relógio
        self.superficie_texto_relogio = fonte.render(self.tempo_formatado, True, (0, 0, 0))
        # Cria o timer na tela
        tela.blit(self.superficie_texto_relogio, (tela_altura - self.superficie_texto_relogio.get_width() - 10, 10))