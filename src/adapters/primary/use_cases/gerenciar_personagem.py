from application.models.Personagem import Personagem
from adapters.primary import pygame_output_adapter

def criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        personagem_criado = Personagem(0, int(posicao_x_ratio * tela_altura), int(posicao_y_ratio * tela_largura), 100, 100, aceleracao)
        return personagem_criado

def desenhar_personagem(personagem, imagens):
        pygame_output_adapter.desenhar_personagem(personagem, imagens)