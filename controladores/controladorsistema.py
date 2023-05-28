from excecoes.valueErrorException import ValueErrorException
from excecoes.loginsenhaException import LoginSenhaException
from telas.telasistema import TelaSistema
from controladores.controladorconsul import ControladorConsul
from controladores.controladoragente import ControladorAgente
from controladores.controladorgerente import ControladorGerente
from controladores.controlador_consulado import ControladorConsulado
from controladores.controlador_solicitacao_de_visto import ControladorSolicitacaoVisto
from controladores.controlador_blacklist import ControladorBlacklist
from controladores.controlador_documento_verificado import ControladorDocumentoVerificado
from controladores.controlador_tipo_visto import ControladorTiposVisto
from controladores.controladorEstrangeiro import ControladorEstrangeiro
from controladores.controlador_documento import ControladorDocumento


class ControladorSistema:
    def __init__(self):
        self.__usuario_logado = None
        self.__controlador_consul = ControladorConsul(self)
        self.__controlador_agente = ControladorAgente(self)
        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_consulado = ControladorConsulado(self)
        self.__controlador_tipo_visto = ControladorTiposVisto(self)
        self.__controlador_solicitacao_visto = ControladorSolicitacaoVisto(self)
        self.__controlador_blacklist = ControladorBlacklist(self)
        self.__controlador_estrangeiro = ControladorEstrangeiro(self)
        self.__controlador_documento_verificado = ControladorDocumentoVerificado(self)
        self.__controlador_documento = ControladorDocumento(self)
        self.__tela_sistema = TelaSistema()

    @property
    def usuario_logado(self):  # conseguir saber quem logou
        return self.__usuario_logado

    @property
    def get_controlador_tipos_visto(self):
        return self.__controlador_tipo_visto

    @property
    def controlador_estrangeiro(self):
        return self.__controlador_estrangeiro

    @property
    def controlador_documento_verificado(self):
        return self.__controlador_documento_verificado

    @property
    def controlador_documento(self):
        return self.__controlador_documento

    @property
    def controlador_consul(self):
        return self.__controlador_consul

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    @property
    def controlador_consulado(self):
        return self.__controlador_consulado

    @property
    def controlador_agente(self):
        return self.__controlador_agente

    @property
    def controlador_solicitacao_visto(self):
        return self.__controlador_solicitacao_visto

    @property
    def controlador_blacklist(self):
        return self.__controlador_blacklist

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    def iniciar_tela_sistema(self):
        global opcao_escolhida
        try:
            login_com_sucesso = None
            lista_opcoes = {1: self.__controlador_consul.abre_tela_inicial,
                            2: self.__controlador_gerente.iniciar_tela_gerente,
                            3: self.__controlador_agente.abre_tela_inicial,
                            0: self.encerrar_sistema}
            login = None
            senha = None
            while True:
                opcao_escolhida = self.__tela_sistema.mostrar_menu_inicial() #aqui tela inicial
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueErrorException()
                elif opcao_escolhida == 0:
                    self.encerrar_sistema()
                else:
                    login, senha = self.__tela_sistema.logar(
                        opcao_escolhida)  # ele vai entrar no login: consul, gerente e agente
                    if opcao_escolhida == 1:#CONSUL
                        login_com_sucesso = self.__controlador_consul.verificar_login_senha(
                            login,
                            senha)
                        if not login_com_sucesso and opcao_escolhida != 0 or login == '' or senha == '':
                            raise LoginSenhaException
                    elif opcao_escolhida == 2:#GERENTE
                        login_com_sucesso = self.__controlador_gerente.verificar_login_senha_sqlite(login, senha)
                        if not login_com_sucesso or login == '' or senha == '':
                            raise LoginSenhaException
                    elif opcao_escolhida == 3: #Agente
                        login_com_sucesso = self.__controlador_agente.verificar_login_senha_sqlite(login, senha)
                        if not login_com_sucesso or login == '' or senha == '':
                            raise LoginSenhaException
                    elif login == None and senha == None:
                        raise LoginSenhaException
                    if login_com_sucesso:
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                        return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.iniciar_tela_sistema()
        except TypeError:
            self.iniciar_tela_sistema()
        except LoginSenhaException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.iniciar_tela_sistema()

    def encerrar_sistema(self):  # encerrar o sistema
        exit(0)
