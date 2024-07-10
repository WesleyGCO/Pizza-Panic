from entities import Fase

class FaseUm(Fase):
    def __init__(self, qtde_pedidos):
        super.__init__(1)
        self.pedidos = qtde_pedidos
