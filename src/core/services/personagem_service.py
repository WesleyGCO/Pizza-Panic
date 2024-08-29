from adapters.primary import pygame_output_adapter
from adapters.primary.use_cases import gerenciar_personagem
from application.models.Item import Item
from core.interfaces.PersonagemInterface import PersonagemInterface
from core.services import pontuacao_service

class PersonagemService(PersonagemInterface):
    def __init__(self):
        self.pontuacao_service = pontuacao_service

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        return gerenciar_personagem.criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao)

    def desenhar_personagem(self, personagem):
        return gerenciar_personagem.desenhar_personagem(personagem)

    def adicionar_pontuacao(self, personagem, item):
        self.pontuacao_service.adicionar_pontuacao(personagem, item)