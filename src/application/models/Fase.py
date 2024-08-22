class Fase:
    def __init__(self, numero, personagem, itens_ruins, tempo_inicial, pedido):
        self.numero = numero
        self.concluida = False
        self.personagem = personagem
        self.itens_ruins = itens_ruins
        self.tempo_inicial = tempo_inicial
        self.pedido_coletado = 0
        self.pedido = pedido

    def concluir(self):
        self.concluida = True
        print(f"Fase {self.numero} concluída!")

    def resetar(self):
        self.concluida = False
        print(f"Fase {self.numero} resetada")

    def adicionar_pedido_coletado(self):
        self.pedido_coletado += 1