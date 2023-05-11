from entidades.estrangeiro import Estrangeiro
from persistencia.estrangeiroDAO import EstrangeiroDAO
from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from telas.tela_estrangeiro import TelaEstrangeiro
import sqlite3


class ControladorEstrangeiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__estrangeiro_dao = EstrangeiroDAO()
        self.__tela_estrangeiro = TelaEstrangeiro()

    @property
    def estrangeiro_dao(self):
        return self.__estrangeiro_dao

    @property
    def tela_estrangeiro(self):
        return self.__tela_estrangeiro
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
