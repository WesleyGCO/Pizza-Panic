from core.interfaces.TempoInterface import TempoInterface

from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_fase, gerenciar_personagem

class TempoService(TempoInterface):    
    def atualizar_contador(self, personagem, posicao_x_texto, posicao_y_texto):
        
        if (personagem.pontuacao_personagem < 0):
            gerenciar_personagem.ajustar_pontuacao(personagem)
        
        # Desenha a quantidade de itens coletados na tela
        texto_itens_coletados = f"Pontuação: {personagem.pontuacao_personagem}"

        superficie_texto = pygame_output_adapter.renderizar_texto(texto_itens_coletados, (0, 0, 0))
        pygame_output_adapter.desenhar_superficie(superficie_texto, (posicao_x_texto, posicao_y_texto))

    def contagem_regressiva(self, fase_model, tela_altura):        
        # Cria o tempo atual
        tempo_atual = pygame_output_adapter.devolve_tempo()
        tempo_decorrido = (tempo_atual - fase_model.tempo_fase_comeca) // 1000
        
        self.tempo_restante = max(0, fase_model.tempo_inicial - tempo_decorrido)
        tempo_formatado = "{:.0f}".format(self.tempo_restante)
            
        if (self.tempo_restante == 0):
            return gerenciar_fase.setar_fase_perdida(fase_model)
        
        # Desenha o tempo restante na tela
        superficie_texto_relogio = pygame_output_adapter.renderizar_texto(tempo_formatado, (0, 0, 0))
        pygame_output_adapter.desenhar_superficie(superficie_texto_relogio, (tela_altura - superficie_texto_relogio.get_width() - 10, 10))
