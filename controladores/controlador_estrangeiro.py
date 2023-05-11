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


    def adicionar_estrangeiro(self):
        try:
            informacoes = self.tela_estrangeiro.tela_adicionar_estrangeiro()
            if informacoes[]
            if informacoes != None:
                if data[0] and data[1] and data[2] and data[3] != '':
                    agente = self.agente_dao.buscar_agente_por_cpf(data[1])
                    if agente != None:
                        self.tela_agente.mostra_mensagem('Este agente já está cadastrado!')
                        return self.abrir_tela_cadastro()
                    else:
                        agente = Agente(data[0], data[1], data[2])
                        self.agente_dao.cadastrar_agente(data[1], data[0], data[2], data[3])
                        self.tela_agente.mostra_mensagem('Agente cadastrado!')
                else:
                    self.tela_agente.mostra_mensagem('Dados Incorretos, preencha corretamente os campos!')
        except ValueErrorException as e:
            self.__controlador_sistema.tela_sistema()           
