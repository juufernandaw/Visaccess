from entidades.agente import Agente
from persistencia.agenteDAO import AgenteDAO
from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from telas.telasistema import TelaSistema
from telas.telaagente import TelaAgente
import sqlite3


class ControladorEstrangeiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__estrangeiro_dao = AgenteDAO()
        self.__tela_estrangeiro = TelaEstrangeiro()

    @property
    def agente_dao(self):
        return self.__agente_dao

    @property
    def tela_agente(self):
        return self.__tela_agente
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
