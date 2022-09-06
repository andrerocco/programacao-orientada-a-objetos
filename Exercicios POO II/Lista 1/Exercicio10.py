class Turma:
    def __init__(self, disciplina, professor, alunos = []):
        self.__disciplina = disciplina
        self.__professor = professor
        self.__alunos = alunos
    
    # Getters
    def get_disciplina(self):
        return self.__disciplina
    def get_professor(self):
        return self.__professor
    def get_alunos(self):
        return self.__alunos
    
    # Setters
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    def set_professor(self, professor):
        self.__professor = professor
    def set_alunos(self, alunos):
        self.__alunos = alunos

class Professor:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
    
    # Getters
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_cpf(self):
        return self.__cpf
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome
    def set_idade(self, idade):
        self.__idade = idade
    def set_cpf(self, cpf):
        self.__cpf = cpf

class Alunos:
    def __init__(self, nome, idade, cpf, iaa, presencas, notas = []):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__iaa = iaa
        self.__presencas = presencas
        self.__notas = notas
    
    # Getters
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_cpf(self):
        return self.__cpf
    def get_iaa(self):
        return self.__iaa
    def get_presencas(self):
        return self.__presencas
    def get_notas(self):
        return self.__notas
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome
    def set_idade(self, idade):
        self.__idade = idade
    def set_cpf(self, cpf):
        self.__cpf = cpf
    def set_iaa(self, iaa):
        self.__iaa = iaa
    def set_presencas(self, presencas):
        self.__presencas = presencas
    def adicionar_nota(self, nota):
        self.__notas.append(nota)
    
    