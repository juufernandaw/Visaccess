from persistencia.blacklistDAO import BlacklistDAO
from entidades.blacklist import Blacklist
from telas.tela_blacklist import TelaBlacklist
from excecoes.valueErrorException import ValueErrorException


class ControladorBlacklist:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__blacklist_DAO = BlacklistDAO()
        self.__blacklist_tela = TelaBlacklist()

    def validar_estrangeiro_blacklist(self, passaporte: str):
        estrangeiro_na_blacklist = self.__blacklist_DAO.encontra_passaporte(passaporte=passaporte)
        return estrangeiro_na_blacklist    # True ou False

    def abre_tela_blacklist(self):
        try:
            mexer_blacklist_opcoes = {1: self.incluir_blacklist,
                                      2: self.listar_blacklist,
                                      3: self.excluir_blacklist,
                                      0: self.abre_tela_blacklist}
            while True:
                opcao_escolhida = self.__blacklist_tela.tela_blacklist_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = mexer_blacklist_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__blacklist_tela.mostrar_msg(e)
            self.abre_tela_blacklist()

    def incluir_blacklist(self):
        botao, nome, passaporte = self.__blacklist_tela.pegar_dados_blacklist()
        if botao == 'Voltar':
            return self.abre_tela_blacklist()
        for blacklist in self.__blacklist_DAO.get_all_blacklist():
            if passaporte == blacklist.passaporte:
                self.__blacklist_tela.mostrar_msg("Este blacklist já consta no sistema!")
                return self.incluir_blacklist()
        else:
            if nome == "" or passaporte == "":
                self.__blacklist_tela.mostrar_msg("Todos os campos devem ser preenchidos.")
                return self.incluir_blacklist()
            blacklist = Blacklist(nome=nome, passaporte=passaporte)
            if blacklist is not None:
                self.__blacklist_DAO.create_tuple_blacklist(nome=blacklist.nome, passaporte=blacklist.passaporte)
                self.__blacklist_tela.mostrar_msg("Passaporte cadastrado blacklist cadastrado com sucesso!")
                return self.abre_tela_blacklist()

    def excluir_blacklist(self):
        botao, blacklist_excluir = self.__blacklist_tela.componentes_tela_excluir_blacklist()
        if botao == 'Voltar':
            return self.abre_tela_blacklist()
        for blacklist in self.__blacklist_DAO.get_all_blacklist():
            if blacklist_excluir["passaporte"] == blacklist.passaporte:
                self.__blacklist_DAO.delete_blacklist(passaporte=blacklist)
                self.__blacklist_tela.mostrar_msg("blacklist excluído com sucesso!")
                return self.abre_tela_blacklist()
        else:
            self.__blacklist_tela.mostrar_msg("Este blacklist NÃO consta no sistema!")
            return self.abre_tela_blacklist()

    def listar_blacklist(self):
        blacklists = self.__blacklist_DAO.get_all_blacklist()
        botao, values = self.__blacklist_tela.componentes_tela_listar_blacklist(lista_blacklist=blacklists)
        if botao == 'Voltar':
            return self.abre_tela_blacklist()
