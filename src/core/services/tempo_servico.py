from core.interfaces.TempoInterface import TempoInterface

from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_fase

class TempoService(TempoInterface):
    
    def __init__(self):
        self.tempo_restante = 1
    
    def atualizar_contador(self, personagem, posicao_x_texto, posicao_y_texto):
        # Obtém a quantidade de itens coletados
        quantidade_itens_coletados = personagem.pontuacao_personagem

        # Desenha a quantidade de itens coletados na tela
        texto_itens_coletados = f"Pontuação: {quantidade_itens_coletados}"

        superficie_texto = pygame_output_adapter.renderizar_texto(texto_itens_coletados, (0, 0, 0))
        pygame_output_adapter.desenhar_superficie(superficie_texto, (posicao_x_texto, posicao_y_texto))

    def contagem_regressiva(self, fase_model, tela_altura):        
        # Cria o tempo atual
        tempo_atual = pygame_output_adapter.devolve_tempo() // 1000
        
        if (tempo_atual <= fase_model.tempo_inicial):
            self.tempo_restante = max(0, fase_model.tempo_inicial - tempo_atual)
            tempo_formatado = "{:.0f}".format(self.tempo_restante)            
        
        if (tempo_atual > fase_model.tempo_inicial):
            # Calcular o tempo excedente
            tempo_excedente = tempo_atual - fase_model.tempo_inicial
            self.tempo_restante = max(0, fase_model.tempo_inicial - tempo_excedente)  # Tempo restante não pode ser negativo
            tempo_formatado = "{:.0f}".format(self.tempo_restante)  # Formata o tempo restante
            
        if (self.tempo_restante == 0):
            return gerenciar_fase.setar_fase_perdida(fase_model)
        
        # Desenha o tempo restante na tela
        superficie_texto_relogio = pygame_output_adapter.renderizar_texto(tempo_formatado, (0, 0, 0))
        pygame_output_adapter.desenhar_superficie(superficie_texto_relogio, (tela_altura - superficie_texto_relogio.get_width() - 10, 10))
