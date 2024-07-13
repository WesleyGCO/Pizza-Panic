class FaseModel:
    def __init__(self, numero, personagem, itens_ruins, tempo_inicial):
        self.numero = numero
        self.concluida = False
        self.personagem = personagem
        self.itens_ruins = itens_ruins
        self.tempo_inicial = tempo_inicial

    def concluir(self):
        self.concluida = True
        print(f"Fase {self.numero} concluída!")

    def resetar(self):
        self.concluida = False
        print(f"Fase {self.numero} resetada")
