from Lista import Lista
from Livro import Livro

lista = Lista()


livro1 = Livro("Lago", "Jonas", "100")
livro2 = Livro("Mar", "Maria", "300")


lista.imprimir()

lista.addNoTopo(livro1)
lista.addNoTopo(livro2)
lista.removerDoFim()
lista.removerDoFim()
