from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)
        self.__matricula = None
        self.presensas = 0
        
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, valor):
        self.__matricula = valor
    
    def marcarPresensa(self, valor):
        self.presensas = valor
        
    def matricular(self, valor):
        self.__matricula = valor
        
    
    def imprimir(self):
        super().imprimir()
        print("Matricula: " + str(self.__matricula))
        print("Presensas: " + str(self.presensas))
