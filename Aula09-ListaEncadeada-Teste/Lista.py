from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    #Teste
    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio # Proximo nó aponta para o inicio
            self.inicio = nodo # Inicio é atualizado para o novo nó
        self.tamanho += 1
        self.imprimir()
    
    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo :
                aux = aux.proximo
            aux.proximo = nodo
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))
    
    #Teste
    def imprimirInverso(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista vazia!")
        else:
            lista_inversa = [] # Cria lista inversa
            aux = self.inicio
            while aux:
                lista_inversa.append(aux.dado) # Manda no para a lista
                aux = aux.proximo
            lista_inversa.reverse() # Inverte a lista ao contrario
            print("Lista ao contrário:")
            for x in lista_inversa: # Percore a lista e imprime
                print(x)
            print("Tamanho:", self.tamanho)

   #Teste 
    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista vazia!")
        else:
            self.inicio = self.inicio.proximo # proximo nó passa ser o inicio
            self.tamanho -= 1 # removo nó do inicio
            self.imprimir()
            
    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho = 0
        else:
            anterior = self.inicio 
            aux = self.inicio.proximo
            while aux.proximo:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None  
            self.tamanho -= 1
            self.imprimir()   