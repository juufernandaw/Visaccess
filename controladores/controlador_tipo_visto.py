from telas.tela_tipo_visto import TelaTipoVisto
from persistencia.tipo_vistoDAO import TipoVistoDAO


class ControladorTipoVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_solicitacao_visto = TelaTipoVisto()
        self.__solicitacao_de_visto_DAO = TipoVistoDAO()
