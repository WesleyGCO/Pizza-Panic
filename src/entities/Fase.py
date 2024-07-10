class Fase:
    def __init__(self, numero, tela, jogo_servico):
        self.numero = numero
        self.concluida = False
        self.tela = tela
        self.jogo_servico = jogo_servico

    def iniciar(self):
        print("Iniciando fase {self.numero}")
        self.is_running = True

    def concluir(self):
        self.concluida = True
        print("Fase concluída!")

    def resetar(self):
        self.concluida = False
        print("Fase resetada")

    