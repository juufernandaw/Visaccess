from persistencia.blacklistDAO import BlacklistDAO
from entidades.blacklist import Blacklist
from telas.tela_blacklist import TelaBlacklist


class ControladorBlacklist:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__blacklist_DAO = BlacklistDAO()
        self.__blacklist_tela = TelaBlacklist()

    def validar_estrangeiro_blacklist(self, passaporte: str):
        self.inserir_na_blacklist()     # para teste
        estrangeiro_na_blacklist = self.__blacklist_DAO.encontra_passaporte(passaporte=passaporte)
        return estrangeiro_na_blacklist    # True ou False

    def inserir_na_blacklist(self):
        # para teste
        self.__blacklist_DAO.create_tuple_blacklist(passaporte='123456', nome='HENRIQUE SOUZA')
        self.__blacklist_DAO.create_tuple_blacklist(passaporte='1234', nome='LUIZA FERNANDES')
        self.__blacklist_DAO.create_tuple_blacklist(passaporte='1111', nome='HENRIQUE SOUZA')
