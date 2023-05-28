from persistencia.blacklistDAO import BlacklistDAO
from entidades.blacklist import Blacklist
from telas.tela_blacklist import TelaBlacklist


class ControladorBlacklist:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__blacklist_DAO = BlacklistDAO()
        self.__blacklist_tela = TelaBlacklist()

    def validar_estrangeiro_blacklist(self, passaporte: str):
        estrangeiro_na_blacklist = self.__blacklist_DAO.encontra_passaporte(passaporte=passaporte)
        return estrangeiro_na_blacklist    # True ou False
