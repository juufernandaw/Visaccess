from entidades.agente import Agente
from persistencia.agenteDAO import AgenteDAO
from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from telas.telasistema import TelaSistema
from telas.telaagente import TelaAgente
import sqlite3


class ControladorAgente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__agente_dao = AgenteDAO()
        self.__tela_sistema = TelaSistema()
        self.__tela_agente = TelaAgente()

    @property
    def agente_dao(self):
        return self.__agente_dao

    # def verificar_login_senha(self, cpf, senha):  # VERIFICAR o cpf e senha.
    #     if isinstance(cpf, str) and isinstance(senha, str):
    #         try:
    #             for agente in self.__agente_dao.get_all():
    #                 if (agente.cpf == cpf) and (agente.senha == senha):
    #                     return True, agente  # agente q achou retornar
    #                 if agente.cpf != cpf or not agente.senha != senha:
    #                     raise LoginSenhaException
    #         except LoginSenhaException as e:
    #             self.__tela_sistema.mostrar_msg(e)
    #             self.__controlador_sistema.iniciar_tela_sistema()
    #         else:
    #             return False

    def verificar_login_senha_sqlite(self, cpf, senha):  # VERIFICAR o cpf e senha pelo sqlite.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
              agente = self.__agente_dao.buscar_agente_por_cpf(cpf)
              senha_digitada = senha
              senha_conferir = str(agente['senha'])
              if agente is not None and senha_conferir == senha_digitada:
                  return True
              elif agente is None:
                  raise UsuarioInexistenteException
              elif agente['senha'] != senha:
                  raise LoginSenhaException
            except LoginSenhaException as e:
                self.__tela_sistema.mostrar_msg(e)
            except UsuarioInexistenteException as e:
                self.__tela_sistema.mostrar_msg(e)
            else:
                return False

    def abre_tela_inicial(self):  # abre a tela aluno pós login da tela
        try:
            mexer_agente_opcoes = {1: self.voltar_tela_sistema,
                                  2: self.voltar_tela_sistema,
                                  0: self.voltar_tela_sistema
                                  }
            while True:
                opcao_escolhida = self.__tela_agente.tela_agente_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueErrorException
                # if opcao_escolhida == 1:
                #     return self.voltar_tela_sistema()
                else:
                    funcao_escolhida = mexer_agente_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.abre_tela_inicial()

    def voltar_tela_sistema(self):
        return self.__controlador_sistema.iniciar_tela_sistema()

    def exit(self):
        return exit(0)

