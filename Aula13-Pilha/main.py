from Lista import Lista
from Livro import Livro

lista = Lista()


livro1 = Livro("Lago", "Jonas", "100")
livro2 = Livro("Mar", "Maria", "300")
livro3 = Livro("Oceano", "Carlos", "200")


lista.imprimir()

lista.addNoTopo(livro1)
lista.addNoTopo(livro2)
lista.addNoTopo(livro3)

lista.removerDoFim()
lista.removerDoFim()
lista.removerDoFim()
