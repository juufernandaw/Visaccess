from entidades.consul_geral import Consul
from excecoes.valueErrorException import ValueErrorException
from telas.telasistema import TelaSistema


class ControladorConsul:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__consul = Consul("Sung D. Ego", "09661640408", "1234")
        self.__tela_sistema = TelaSistema()

    def verificar_login_senha(self, cpf, senha):
        if isinstance(cpf, str) and isinstance(senha, str):
            if self.__consul.cpf == cpf and self.__consul.senha == senha:
                return True

    def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema AS ABAS
        try:
            mexer_personal_opcoes = {1: self.__tela_sistema.mostrar_menu_inicial(),
                                     2: self.__tela_sistema.mostrar_menu_inicial(),
                                     3: self.__tela_sistema.mostrar_menu_inicial(),
                                     0: self.__controlador_sistema.iniciar_tela_sistema
                                     }
            while True:
                opcao_escolhida = self.__tela_sistema.layout_logar_consul()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.abre_tela_inicial()

    def voltar(self):
        return self.abre_tela_inicial()
