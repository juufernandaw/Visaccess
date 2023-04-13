from excecoes.valueErrorException import ValueErrorException
from excecoes.loginsenhaException import LoginSenhaException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from telas.telasistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__usuario_logado = None
        self.__controlador_consul = ControladorConsul(self)
        self.__controlador_agente = ControladorAgente(self)
        self.__controlador_gerente = ControladorGerente(self)
        self.__tela_sistema = TelaSistema()

    @property
    def usuario_logado(self): #conseguir saber quem logou
        return self.__usuario_logado

    @property
    def controlador_consul(self):
        return self.__controlador_consul

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    @property
    def controlador_agente(self):
        return self.__controlador_agente

    def iniciar_tela_sistema(self):
        global opcao_escolhida
        try:
            login_com_sucesso = None
            lista_opcoes = {1: self.__controlador_consul.abre_tela_inicial,
                            2: self.__controlador_gerente.abre_tela_inicial,
                            3: self.__controlador_agente.abre_tela_inicial,
                            0: self.encerrar_sistema}
            login = None
            senha = None
            while True:
                opcao_escolhida = self.__tela_sistema.mostrar_menu_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and  opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueErrorException(opcao_escolhida)
                elif opcao_escolhida == 0:
                    self.encerrar_sistema()
                else:
                    login, senha = self.__tela_sistema.logar(opcao_escolhida)  # ele vai entrar no login: consul, gerente e agente
                    if opcao_escolhida == 1:
                        login_com_sucesso, self.__usuario_logado = self.__controlador_consul.verificar_login_senha(login,
                                                                                                                  senha)
                        if self.__usuario_logado is None:
                            raise UsuarioInexistenteException
                    elif opcao_escolhida == 2:
                        login_com_sucesso = self.__controlador_gerente.verificar_login_senha(login, senha)
                        if not login_com_sucesso:
                            raise UsuarioInexistenteException
                    elif opcao_escolhida == 3:
                        login_com_sucesso = self.__controlador_agente.verificar_login_senha(login, senha)
                        if not login_com_sucesso:
                            raise UsuarioInexistenteException
                    if login_com_sucesso is not None:
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                        return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.iniciar_tela_sistema()
        except TypeError:
            self.iniciar_tela_sistema()
        except UsuarioInexistenteException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.iniciar_tela_sistema()
        pass

    def encerrar_sistema(self): #encerrar o sistema
        exit(0)
