from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


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
				raise ValueError("Chamado duplicado já cadastrado")

		return Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)

	def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
		for tipo in self.__tipo_chamados:
			if tipo.codigo == codigo:
				raise ValueError("Código de chamado já cadastrado")
			elif tipo.nome == nome:
				raise ValueError("Nome de chamado já cadastrado")
			elif tipo.descricao == descricao:
				raise ValueError("Descrição de chamado já cadastrada")
		
		return TipoChamado(codigo, nome, descricao)
	
	@property	
	def tipoChamados(self):
		return self.__tipo_chamados