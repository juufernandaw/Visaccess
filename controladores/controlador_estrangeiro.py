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

    def abre_tela_inicial_estrangeiro(self):  # abre a tela para cadastrar estrangeiro
        try:
            mexer_agente_opcoes = {1: self.__tela_estrangeiro.tela_adicionar_estrangeiro,
                                  2: self.__tela_estrangeiro.tela_atualizar_estrangeiro,
                                  3: self.__tela_estrangeiro.tela_excluir_estrangeiro,
                                  4: self.__tela_estrangeiro.tela_modificar_estrangeiro,
                                  0: self.voltar_tela_gerente
                                  }
            while True:
                opcao_escolhida = self.__tela_estrangeiro.tela_cadastro_estrangeiro()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                else:
                    funcao_escolhida = mexer_agente_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_estrangeiro.mostra_mensagem("Tente novamente")
            self.abre_tela_inicial_estrangeiro()

    def voltar_tela_gerente(self):
        return self.__controlador_sistema.controlador_gerente.iniciar_tela_gerente()

    def adicionar_estrangeiro(self):
        try:
            #IR PARA TELA
            informacoes = self.tela_estrangeiro.tela_adicionar_estrangeiro()
            if informacoes != None:
                if informacoes[0] and informacoes[1] and informacoes[2] and informacoes[3] != '':
                    agente = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(informacoes[1])
                    if agente != None:
                        self.tela_estrangeiro.mostra_mensagem('Este estrangeiro já está cadastrado!')
                        return self.adicionar_estrangeiro()
                    else:
                        #CRIAR ENTIDADE
                        estrangeiro = Estrangeiro(informacoes[0], informacoes[1], informacoes[2])
                        #BANCO DE DADOS
                        self.estrangeiro_dao.cadastrar_estrangeiro(informacoes[1], informacoes[0], informacoes[2], informacoes[3])
                        self.tela_estrangeiro.mostra_mensagem('Estrangeiro cadastrado!')
                else:
                    self.tela_estrangeiro.mostra_mensagem('Dados Incorretos, preencha corretamente os campos!')
        except ValueErrorException as e:
            self.abre_tela_inicial_estrangeiro()           

    def excluir_estrangeiro(self):
        pass

    def listar_estrangeiro(self):
        pass

    def modificar_estrangeiro(self):
        pass
