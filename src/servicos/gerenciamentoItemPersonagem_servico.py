import random

from servicos.item_servico import Item_Servico
from servicos.personagem_servico import Personagem_Servico

class GerenciamentoItemPersonagem_Servico:

    def criar_item(self):
        return Item_Servico.criar_item()
    
    def desenhar_item(self, itemRuim, screen):
        id_item = random.randint(0, 2)
        imagem_definida = self.definir_imagem(id_item)

        Item_Servico.desenhar_item(itemRuim, screen, imagem_definida)

    def movimento_item(self, itemRuim, gravidade):
        # Dá movimento para os itens baseados na gravidade
        Item_Servico.movimento_item(itemRuim, gravidade)

    def reinicia_item(self, itemRuim):
        # Reinicia os itens de acordo com o eixo y
        Item_Servico.reinicia_item(itemRuim)

    def checa_colisao(self, personagem, itemColide):
        return Item_Servico.checa_colisao(personagem, itemColide)
    
    def definir_imagem(self, id):
        return Item_Servico.definir_imagem(id)
    
    def desenhar_personagem(self, personagem, tela):
        Personagem_Servico.desenhar_personagem(personagem, tela)

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio):
        return Personagem_Servico.criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio)
