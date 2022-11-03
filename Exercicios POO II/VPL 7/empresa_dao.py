import pickle
from empresa import Empresa
from empresa_duplicada_exception import EmpresaDuplicadaException

class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, empresa: Empresa):
        if empresa.cnpj in self.__object_cache.keys():
            raise EmpresaDuplicadaException()
        else:
            self.__object_cache[empresa.cnpj] = empresa
            self.__dump()
    
    def get(self, cnpj: int) -> Empresa:
        if cnpj in self.__object_cache.keys():
            return self.__object_cache[cnpj]
        else:
            raise KeyError()
    
    def remove(self, cnpj: int):
        if cnpj in self.__object_cache.keys():
            del self.__object_cache[cnpj]
            self.__dump()
        else:
            raise KeyError()
    
    def get_all(self) -> list:
        return self.__object_cache.values()
