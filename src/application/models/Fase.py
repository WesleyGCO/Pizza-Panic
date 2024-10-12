class Fase:
    def __init__(self, numero, personagem, itens_ruins, tempo_inicial, pedido, tempo_fase_comeca):
        self.numero = numero
        self.concluida = False
        self.perdida = False
        self.personagem = personagem
        self.itens_ruins = itens_ruins
        self.tempo_inicial = tempo_inicial
        self.pedido_coletado = 0
        self.pedido = pedido
        self.tempo_fase_comeca = tempo_fase_comeca

    def concluir(self):
        self.concluida = True
        print(f"Fase {self.numero} concluída!")
        
    def perdeu(self):
        self.perdida = True
        self.concluida = False
        print(f"Fase {self.numero} perdida!")

    def adicionar_pedido_coletado(self):
        self.pedido_coletado += 1

    