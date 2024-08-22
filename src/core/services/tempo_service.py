from core.interfaces.TempoInterface import TempoInterface

from adapters.primary import pygame_output_adapter

class TempoService(TempoInterface):
    def atualizar_contador(self, personagem, posicao_x_texto, posicao_y_texto):
        # Obtém a quantidade de itens coletados
        quantidade_itens_coletados = personagem.itens_coletados

        # Desenha a quantidade de itens coletados na tela
        texto_itens_coletados = f"Pontuação: {quantidade_itens_coletados}"

        superficie_texto = pygame_output_adapter.renderizar_texto(texto_itens_coletados, (0, 0, 0))
        pygame_output_adapter.desenhar_superficie(superficie_texto, (posicao_x_texto, posicao_y_texto))

    def contagem_regressiva(self, tempo_inicial, tela_altura):
        # Cria o tempo atual
        tempo_atual = pygame_output_adapter.devolve_tempo() // 1000        

        tempo_formatado = "{:.0f}".format(max(0, tempo_inicial - tempo_atual))

        superficie_texto_relogio = pygame_output_adapter.renderizar_texto(tempo_formatado, (0, 0, 0))

        pygame_output_adapter.desenhar_superficie(superficie_texto_relogio, (tela_altura - superficie_texto_relogio.get_width() - 10, 10))

        if (tempo_formatado == 0):
            return False