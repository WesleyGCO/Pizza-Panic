from adapters.primary import pygame_output_adapter
from application.models.Objeto import Objeto
from application.models.Personagem import Personagem

def adicionar_pontuacao(personagem, item):
    if isinstance(item, Objeto):
        pontuacao = item.pontuacao()
    if isinstance(personagem, Personagem):
        personagem.adicionar_pontuacao(pontuacao)
    if (item.tipo != "pizza"):
        pygame_output_adapter.tocar_som("erro_item")