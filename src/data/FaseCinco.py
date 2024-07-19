from data.Fase import Fase

class FaseCinco(Fase):
    def __init__(self, numero, personagem, itens_ruins, tempo_inicial):
        super().__init__(numero, personagem, itens_ruins, tempo_inicial)
        self.pedido = 8

    def init():
        pass

    def concluir(self):
        return super().concluir()
    
    def resetar(self):
        return super().resetar()