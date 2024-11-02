from application.models.Objeto import Objeto

class Personagem(Objeto):

    def __init__(self, cor, x, y, largura, altura, aceleracao):
        super().__init__(x, y, largura, altura)
        self.cor = cor
        self.aceleracao.x = aceleracao
        self.pontuacao_personagem = 0
        self.nome_personagem = None

    def adicionar_pontuacao(self, pontuacao):
        # Adiciona o item coletado à lista de itens coletados
        self.pontuacao_personagem += pontuacao