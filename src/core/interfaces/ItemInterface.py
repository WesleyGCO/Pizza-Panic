from abc import ABC, abstractmethod

class ItemInterface(ABC):
    @abstractmethod
    def criar_item():
        pass

    @abstractmethod
    def desenhar_item():
        pass

    @abstractmethod
    def movimento_item():
        pass

    @abstractmethod
    def reinicia_item():
        pass

    @abstractmethod
    def checa_colisao():
        pass