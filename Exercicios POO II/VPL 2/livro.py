from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autor = [autor]
        self.__capitulo = [Capitulo(numeroCapitulo, tituloCapitulo)]

    #Getters
    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autor
    
    #Setters
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @editora.setter
    def editora(self, editora):
        self.__editora = editora
    

    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and (autor not in self.__autor):
            self.__autor.append(autor)

    def excluirAutor(self, autor: Autor):
        if autor in self.__autor:
            self.__autor.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        if self.findCapituloByTitulo(tituloCapitulo) == None:
            self.__capitulo.append(Capitulo(numeroCapitulo, tituloCapitulo))

    def excluirCapitulo(self, tituloCapitulo: str):
        capitulo = self.findCapituloByTitulo(tituloCapitulo)
        if capitulo != None:
            self.__capitulo.remove(capitulo)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulo:
            if capitulo.titulo == tituloCapitulo:
                return capitulo
        return None

