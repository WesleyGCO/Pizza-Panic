from adapters.primary import pygame_output_adapter
 

class Sprites():

    def __init__(self):
        self.index_sprite = 0
        self.frame_counter = 0
        self.frame_delay = 8

    def get_personagem_sprite_direita(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_right.png')
        
        return self.imagens_pesonagem
    
    def get_personagem_sprite_esquerda(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_left.png')

        return self.imagens_pesonagem
    
    def get_personagem_sprite_direita_parado(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_right_parado.png')

        return self.imagens_pesonagem
    
    def get_personagem_sprite_esquerda_parado(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_left_parado.png')

        return self.imagens_pesonagem
    


    def animar_personagem_direita(self):
        sprites_direita = [
            pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_right_parado.png'),
            pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_right.png')
        ]
        
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.index_sprite = (self.index_sprite + 1) % len(sprites_direita)
            self.frame_counter = 0
        return sprites_direita[self.index_sprite]

    def animar_personagem_esquerda(self):
        sprites_esquerda = [
            pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_left_parado.png'),
            pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_left.png')
        ]
        
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.index_sprite = (self.index_sprite + 1) % len(sprites_esquerda)
            self.frame_counter = 0
        return sprites_esquerda[self.index_sprite]

