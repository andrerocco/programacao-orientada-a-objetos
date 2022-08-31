class Livro:
    def __init__(self, titulo, autor, ano, editora, edicao, volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume
    
    # Setters
    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_autor(self, autor):
        self.autor = autor
    def set_ano(self, ano):
        self.ano = ano
    def set_editora(self, editora):
        self.editora = editora
    def set_edicao(self, edicao):
        self.edicao = edicao
    def set_volume(self, volume):
        self.volume = volume

    # Getters
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_ano(self):
        return self.ano
    def get_editora(self):
        return self.editora
    def get_edicao(self):
        return self.edicao
    def get_volume(self):
        return self.volume