from Visaccess.persistencia.consuladoDAO import ConsuladoDAO
from Visaccess.entidades.consulado import Consulado
from Visaccess.telas.tela_consulado import TelaConsulado

class ControladorConsulado:

    def __init__(self):
        self.__consulado_DAO = ConsuladoDAO()
        self.__consulado_tela = TelaConsulado()

    def incluir_consulado(self):
        pass

    def alterar_consulado(self):
        pass

    def excluir_consulado(self):
        pass

    def listar_consulados(self):
        pass
