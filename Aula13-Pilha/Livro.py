class Livro:
    def __init__(self, titulo, autor, pag):
        self.titulo = titulo
        self.autor = autor
        self.paginas = pag
        self.anterior = None
        self.proximo = None


    def __str__(self):
        texto = "\n-----------------------"
        texto += "\nTitulo: " + self.titulo
        texto += "\nAutor: " + self.autor
        texto += "\nPaginas: " + str(self.paginas)
        return texto

        