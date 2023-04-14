from entidades.agente import Agente
from persistencia.agente import AgenteDAO
from excecoes.loginsenhaException import LoginSenhaException
from telas.telasistema import TelaSistema

class ControladorAgente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__agente_dao = AgenteDAO()
        self.__tela_sistema = TelaSistema()

    @property
    def agente_dao(self):
        return self.__agente_dao

    @property
    def agente_dao(self):
        return self.__agente_dao

    def verificar_login_senha(self, cpf, senha):  # VERIFICAR o cpf e senha.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
                for agente in self.__agente_dao.get_all():
                    if (agente.cpf == cpf) and (agente.senha == senha):
                        return True, agente  # agente q achou retornar
                    if agente.cpf != cpf or not agente.senha != senha:
                        raise LoginSenhaException
            except LoginSenhaException as e:
                self.__tela_sistema.mostrar_msg(e)
                self.__controlador_sistema.iniciar_tela_sistema()
            else:
                return False
