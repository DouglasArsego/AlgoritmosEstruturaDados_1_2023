from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, pontenciaDaFonte=0):
        super().__init__(modelo, cor, preco)
        self.potencia = pontenciaDaFonte
        
    def getInformacoes(self):
        print("========== Desktop ==========")
        super().getInformacoes()
        print("Potencia: " + str(self.potencia) + " W")
        
    def cadastrar(self):
        print("========== Desktop ==========")
        super().getInformacoes()
        print("Potencia: " + str(self.potencia) + " W")