class Pessoa:
    idade = 0
    def __init__(self, name, idade):
        print("Objeto instanciado!")
        # self.nome = "Maria"
        self.nome = name
        self.idade = idade
        self.fone = input("Digite seu fone: ")
    
    def imprimir(self):
        print("Nome: " , self.nome )
        print("Idade: " , self.idade )
        print("Telefone: " , self.fone )
