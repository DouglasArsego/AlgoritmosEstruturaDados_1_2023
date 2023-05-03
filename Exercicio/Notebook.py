from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempoDeBateria=0):
        super().__init__(modelo, cor, preco)
        self.__bateria = tempoDeBateria
        
    def getInformacoes(self):
        print("========== Notebook ==========")
        super().getInformacoes()
        print("Tempo de Bateria: " + str(self.__bateria) + " Horas ")
        
    def cadastrar(self):
        print("========== Notebook ==========")
        super().getInformacoes()
        print("Tempo de Bateria: " + str(self.__bateria) + " Horas ")