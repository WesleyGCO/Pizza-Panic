from abc import ABC, abstractmethod

class PersonagemInterface(ABC):
    @abstractmethod
    def criar_personagem():
        pass

    @abstractmethod
    def desenhar_personagem():
        pass

    @abstractmethod
    def coletar_item():
        pass

    @abstractmethod
    def pegar_itens_coletados():
        pass