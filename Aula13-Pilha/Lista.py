from Livro import Livro

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
        
    def addNoTopo(self, livro):
        if self.inicio == None:
            self.inicio = livro
            self.fim = livro
        else:
            livro.proximo = self.inicio
            self.inicio.anterior = livro
            self.inicio = livro
        self.tamanho += 1
        self.imprimir()
    
                              
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print(aux) 
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))

                        
            
    def removerDoFim(self):
        if self.inicio == None:
            print("Fila Vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.inicio = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        self.imprimir()       