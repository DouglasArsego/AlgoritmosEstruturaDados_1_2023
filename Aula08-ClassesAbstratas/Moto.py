from Veiculo import Veiculo
    
class Moto(Veiculo):
    def __init__(self, modelo=None, ano=None, cilindradas=0):
        super().__init__(modelo, ano)
        self.cilidradas = cilindradas
    
    def imprimir(self):
        print("Motocicleta: ")
        super().imprimir()
    
    def imprimirEspecifico(self):
        super().imprimir()
        print("Cilindradas: " + str(self.cilidradas))