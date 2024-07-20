from abc import ABC, abstractmethod

class FaseInterface(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def update(self):
        pass