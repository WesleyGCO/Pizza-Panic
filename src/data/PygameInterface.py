from abc import ABC, abstractmethod

class PygameInterface(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def criar_tela(self, altura, largura):
        pass

    @abstractmethod
    def define_titulo(self, titulo):
        pass

    @abstractmethod
    def carregar_imagem(self, caminho):
        pass

    @abstractmethod
    def capturar_evento(self):
        pass

    @abstractmethod
    def sair(self):
        pass