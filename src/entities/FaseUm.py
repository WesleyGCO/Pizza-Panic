from entities.Fase import Fase

class FaseUm(Fase):
    def init(self, numero, tela, tela_altura, tela_largura, personagem, itens_ruins, 
             tempo_inicial, posicao_x_texto, posicao_y_texto, fonte, gravidade, relogio):
        
        super.__init__(self, numero, tela, tela_altura, tela_largura, personagem, itens_ruins, 
                       tempo_inicial, posicao_x_texto, posicao_y_texto, fonte, gravidade, relogio)

    