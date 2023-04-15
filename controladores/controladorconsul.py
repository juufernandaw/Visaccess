from entidades.consul_geral import Consul
from excecoes.valueErrorException import ValueErrorException
from telas.telasistema import TelaSistema
from telas.telaconsul import TelaConsul


class ControladorConsul:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__consul = Consul("Sung D. Ego", "09661640408", "1234")
        self.__tela_sistema = TelaSistema()
        self.__tela_consul = TelaConsul()

    def verificar_login_senha(self, cpf, senha):
        if isinstance(cpf, str) and isinstance(senha, str):
            if self.__consul.cpf == cpf and self.__consul.senha == senha:
                return True

    def abre_tela_inicial(self):  # abre a tela vconsul pos login da tela do sistema
        try:
            mexer_consul_opcoes = {1: self.__tela_sistema.mostrar_menu_inicial(),
                                   2: self.__tela_sistema.mostrar_menu_inicial(),
                                   3: self.__tela_sistema.mostrar_menu_inicial(),
                                   4: self.__tela_sistema.mostrar_menu_inicial(),
                                   5: self.__tela_sistema.mostrar_menu_inicial(),
                                   6: self.__tela_sistema.mostrar_menu_inicial(),
                                   0: self.__controlador_sistema.iniciar_tela_sistema
                                   }
            while True:
                opcao_escolhida = self.__tela_sistema.tela_consul_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4\
                        and opcao_escolhida != 5 and opcao_escolhida != 6 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = mexer_consul_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.abre_tela_inicial()

    def voltar(self):
        return self.abre_tela_inicial()
