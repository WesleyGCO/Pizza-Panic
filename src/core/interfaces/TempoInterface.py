from abc import ABC, abstractmethod

class TempoInterface(ABC):
    @abstractmethod
    def atualizar_contador():
        pass

    @abstractmethod
    def contagem_regressiva():
        pass