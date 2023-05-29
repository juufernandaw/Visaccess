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

    @property
    def tela_agente(self):
        return self.__tela_agente
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    #  CADASTRO DE AGENTES ABAIXO ------------------

    def abrir_tela_cadastro(self):
        while True:
            opcao = self.tela_agente.tela_cadastro_agentes()
            if opcao == 1:
                self.adicionar_agente()
            elif opcao == 2:
                self.excluir_agente()
            elif opcao == 3:
                self.listar_agentes()
            elif opcao == 4:
                self.modificar_agente()
            elif opcao == 0:
                self.controlador_sistema.controlador_gerente.iniciar_tela_gerente()

    def adicionar_agente(self):
        data = self.tela_agente.tela_adicionar_agentes()

        if data != None:
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

    def excluir_agente(self):
        cpf = self.tela_agente.tela_excluir_agentes()
        if cpf != None:
            agente = self.agente_dao.buscar_agente_por_cpf(cpf[0])
            if agente != None:
                self.agente_dao.excluir_agente(cpf[0])
                self.tela_agente.mostra_mensagem('Agente Excluído!')
                return self.abrir_tela_cadastro()
            else:
                self.tela_agente.mostra_mensagem('Agente Não está cadastrado!')

    def listar_agentes(self):
        agentes = self.agente_dao.buscar_todos_agentes()
        self.tela_agente.componentes_tela_listar_agentes(agentes)

    def modificar_agente(self):
        cpf = self.tela_agente.tela_modificar_agentes()

        if cpf != None:
            agente = self.agente_dao.buscar_agente_por_cpf(cpf[0])
            if agente != None:
                    dados_novos = self.tela_agente.tela_atualizar_agentes()
                    if dados_novos != None:
                        if dados_novos[0] and dados_novos[1] and dados_novos[2] and dados_novos[3]!= '':
                            teste = self.agente_dao.buscar_agente_por_cpf(dados_novos[1])
                            if teste == None:
                                self.agente_dao.atualizar_agente(
                                    agente['cpf'], 
                                    dados_novos[1], 
                                    dados_novos[0], 
                                    dados_novos[2], 
                                    dados_novos[3]
                                )
                                self.tela_agente.mostra_mensagem('Agente Modificado!')
                                return self.abrir_tela_cadastro()
                            else:
                                self.tela_agente.mostra_mensagem('CPF já consta no sistema!')
                                return self.abrir_tela_cadastro()
                        else:
                            self.tela_agente.mostra_mensagem('Preencha com os dados corretos!')
                            return self.abrir_tela_cadastro()
            else:
                self.tela_agente.mostra_mensagem('Não há agentes com esse cadastro!')

    #  CADASTRO DE AGENTES ACIMA ------------------

    def verificar_login_senha_sqlite(self, cpf, senha):  # VERIFICAR o cpf e senha pelo sqlite.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
                if cpf == '' or senha == '':
                    raise UsuarioInexistenteException
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

    def abre_tela_inicial(self):  # abre a tela
            try:
                mexer_agente_opcoes = {1: self.voltar_tela_sistema,
                                    2: self.__controlador_sistema.controlador_estrangeiro.abre_tela_inicial_estrangeiro, #cadastrar estrangeiro
                                    0: self.voltar_tela_sistema
                                    }
                while True:
                    opcao_escolhida = self.__tela_agente.tela_agente_inicial()
                    if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                        raise ValueErrorException
                    else:
                        funcao_escolhida = mexer_agente_opcoes[opcao_escolhida]
                        if funcao_escolhida == self.__controlador_sistema.controlador_estrangeiro.abre_tela_inicial_estrangeiro:
                            return funcao_escolhida('agente')
                        return funcao_escolhida()
            except ValueErrorException as e:
                self.__tela_sistema.mostrar_msg(e)
                self.abre_tela_inicial()

    def voltar_tela_sistema(self):
        return self.__controlador_sistema.iniciar_tela_sistema()

    def exit(self):
        return exit(0)

