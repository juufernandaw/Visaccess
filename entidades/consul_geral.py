from entidades.usuario import Usuario


class Consul:
    def __init__(self, nome: str, cpf: str, senha:str):
        super().__init__(nome, senha, cpf)
