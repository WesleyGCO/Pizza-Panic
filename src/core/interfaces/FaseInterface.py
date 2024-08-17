from abc import ABC, abstractmethod

class FaseInterface(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def lidar_entrada(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass
    
    @abstractmethod
    def contar_pedido(self):
        pass