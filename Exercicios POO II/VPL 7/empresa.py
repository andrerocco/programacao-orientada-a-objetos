from imposto import Imposto
from incidencia_imposto import IncidenciaImposto
from empresa_duplicada_exception import EmpresaDuplicadaException

class Empresa:
    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cpnj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.0
        self.__faturamento_producao = 0.0
        self.__faturamento_vendas = 0.0

    '''
    Retorna a lista de impostos da empresa
    @return Lista de impostos da empresa
    '''
    @property
    def impostos(self) -> list:
        return self.__impostos

    '''
    Inclui um imposto na lista de impostos da empresa
    Verifica se o imposto ja esta cadastrado antes de inserir um novo
    @param imposto imposto a ser incluido
    '''
    def inclui_imposto(self, imposto: Imposto):
        if imposto not in self.__impostos:
            self.__impostos.append(imposto)
        else:
            raise EmpresaDuplicadaException()

    '''
    Exclui um imposto cadastrado
    @param imposto imposto a ser excluido da lista de impostos da empresa
    '''
    def remove_imposto(self, imposto: Imposto):
        try:
            self.__impostos.remove(imposto)
        except ValueError:
            print('Imposto não cadastrado')

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    '''
    Calcula o total dos faturamentos da empresa,
    somando: faturamento_producao,
        faturamento_servicos e faturamento_vendas
    @return Somatorio dos faturamentos
    '''
    def faturamento_total(self) -> float:
        return self.__faturamento_servicos + self.__faturamento_producao + self.__faturamento_vendas
        
    '''
    Calcula o total de todos os impostos da empresa
    Percorre a lista de impostos da empresa,
    aplicando a aliquota de cada imposto.
    Leva em conta o tipo de cada imposto (IncidenciaImposto) para aplicar
    a aliquota ao faturamento de Producao, Vendas, Servicos ou sobre o Total
    @return
    '''
    def total_impostos(self) -> float:
        total = 0

        for imposto in self.__impostos:
            if imposto.incidencia_imposto == IncidenciaImposto.PRODUCAO:
                total += self.__faturamento_producao * (imposto.calcula_aliquota()/100)
            elif imposto.incidencia_imposto == IncidenciaImposto.SERVICOS:
                total += self.__faturamento_servicos * (imposto.calcula_aliquota()/100)
            elif imposto.incidencia_imposto == IncidenciaImposto.VENDAS:
                total += self.__faturamento_vendas * (imposto.calcula_aliquota()/100)
            elif imposto.incidencia_imposto == IncidenciaImposto.TODOS:
                total += self.faturamento_total() * (imposto.calcula_aliquota()/100)
        
        return total

    @property
    def cnpj(self):
        return self.__cpnj

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia: str):
        self.__nome_de_fantasia = nome_de_fantasia

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        self.__faturamento_servicos = fat_servicos
        self.__faturamento_producao = fat_producao
        self.__faturamento_vendas = fat_vendas
