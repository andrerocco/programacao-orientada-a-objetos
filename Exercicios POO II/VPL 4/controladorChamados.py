from distutils.log import error
from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
	def __init__(self):
		self.__chamados = []
		self.__tipo_chamados = []

	def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
		total = 0
		for chamado in self.__chamados:
			if chamado.tipo == tipo:
				total += 1
		
		return total

	def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
		for chamado in self.__chamados:
			if chamado.data == data and chamado.cliente == cliente and chamado.tecnico == tecnico and chamado.tipo == tipo:
				return "Chamado duplicado já cadastrado"

		if not isinstance(data, Date):
			return "Data inválida"
		elif not isinstance(cliente, Cliente) or not isinstance(tecnico, Tecnico):
			return "Cliente ou técnico inválido"
		elif not isinstance(tipo, TipoChamado):
			return "Tipo de chamado inválido"
		
		chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
		self.__chamados.append(chamado)
		
		return chamado

	def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
		for tipo in self.__tipo_chamados:
			if tipo.codigo == codigo:
				return "Código de chamado já cadastrado"
			elif tipo.nome == nome:
				return "Nome de chamado já cadastrado"
			elif tipo.descricao == descricao:
				return "Descrição de chamado já cadastrada"
		
		tipo = TipoChamado(codigo, nome, descricao)
		self.__tipo_chamados.append(tipo)
		
		return tipo
	
	@property	
	def tipoChamados(self):
		return self.__tipo_chamados
