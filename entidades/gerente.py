from entidades.agente import Agente


class Gerente(Agente):
    def __init__(self, nome: str, cpf: str, senha: str, consulado):
        super().__init__(nome, senha, cpf)
        self.consulado = consulado

