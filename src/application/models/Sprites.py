from adapters.primary import pygame_output_adapter
 

class Sprites():

    def __init__(self):
        self.index_sprite = 0

    def get_personagem_sprite_direita(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo.png')
        
        return self.imagens_pesonagem
    
    def get_personagem_sprite_esquerda(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo_left.png')

        return self.imagens_pesonagem
    
    def get_personagem_sprite_direita_parado(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_right_parado.png')

        return self.imagens_pesonagem
    
    def get_personagem_sprite_esquerda_parado(self):
        self.imagens_pesonagem = pygame_output_adapter.carregar_imagem('./adapters/primary/sprites/pizzaiolo/pizzaiolo_left_parado.png')

        return self.imagens_pesonagem
    
    def mov_direita():
        pass

    def mov_esquerda():
        pass
    
    def loop_mov(self, tempo, posicao):
        if tempo >= 1:
            if posicao == 'esquerda':
                self.index_sprite = (self.index_sprite + 1) % self.mov_esquerda() 
            else:
                self.index_sprite = (self.index_sprite + 1) % self.mov_direita() 
        tempo = 0 

