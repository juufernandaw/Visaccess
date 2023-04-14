from entidades.consul_geral import Consul


class ControladorConsul:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__consul = Consul("Sung D. Ego", "09661640408", "1234")

    def verificar_login_senha(self, cpf, senha):
        if isinstance(cpf, str) and isinstance(senha, str):
            if self.__consul.cpf == cpf and self.__consul.senha == senha:
                return True
