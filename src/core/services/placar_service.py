from core.interfaces.PlacarInterface import PlacarInterface
from adapters.primary.use_cases import gerenciar_placar
from adapters.primary import pygame_output_adapter

class PlacarService(PlacarInterface):
    def renderizar_placar(self, fase_model):
        informacoes_placar = gerenciar_placar.obter_informacoes_placar(fase_model)

        texto_pedidos = f"Atender: {informacoes_placar['pedidos']}"
        texto_atendidos = f"Atendidos: {informacoes_placar['pedidos_coletados']}"

        pygame_output_adapter.renderizar_texto_placar(texto_pedidos, texto_atendidos)
        