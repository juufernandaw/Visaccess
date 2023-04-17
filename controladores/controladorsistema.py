from excecoes.valueErrorException import ValueErrorException
from excecoes.loginsenhaException import LoginSenhaException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from telas.telasistema import TelaSistema
from controladores.controladorconsul import ControladorConsul
from controladores.controladoragente import ControladorAgente
from controladores.controladorgerente import ControladorGerente
from controladores.controlador_consulado import ControladorConsulado


class ControladorSistema:
    def __init__(self):
        self.__usuario_logado = None
        self.__controlador_consul = ControladorConsul(self)
        self.__controlador_agente = ControladorAgente(self)
        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_consulado = ControladorConsulado(self)
        self.__tela_sistema = TelaSistema()

    @property
    def usuario_logado(self):  # conseguir saber quem logou
        return self.__usuario_logado

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

    def iniciar_tela_sistema(self):
        global opcao_escolhida
        try:
            login_com_sucesso = None
            lista_opcoes = {1: self.__controlador_consul.abre_tela_inicial,
                            2: self.__controlador_gerente.abre_tela_inicial_gerente,
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
                        if not login_com_sucesso and opcao_escolhida != 0:
                            raise LoginSenhaException
                    elif opcao_escolhida == 2:#GERENTE
                        login_com_sucesso = self.__controlador_gerente.verificar_login_senha_sqlite(login, senha)
                        if not login_com_sucesso:
                            raise LoginSenhaException
                    elif opcao_escolhida == 3: #Agente
                        login_com_sucesso = self.__controlador_agente.verificar_login_senha_sqlite(login, senha)
                        if not login_com_sucesso:
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
