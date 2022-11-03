from controlador_sistema_empresas import ControladorSistemaEmpresas
from empresa import Empresa

controlador = ControladorSistemaEmpresas()

controlador.busca_empresa_pelo_cnpj(120123)

""" empresa1 = Empresa(120123, 'Empresa 1')

controlador.inclui_empresa(empresa1) """


