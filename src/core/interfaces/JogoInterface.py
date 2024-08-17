from abc import ABC, abstractmethod

class JogoInterface(ABC):
    @abstractmethod
    def iniciar_jogo():
        pass

    @abstractmethod
    def encerrar_jogo():
        pass