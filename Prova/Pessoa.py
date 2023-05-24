from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, telefone):
        self.id = None
        self.nome = nome
        self._telefone = telefone
        
    def imprimir(self):
        print("Nome: " + self.nome)    
        print("Telefone: " + self._telefone)    
        
    @abstractmethod  
    def marcarPresensa(self):
        pass
    
    @abstractmethod
    def matricular(self):
        pass
    