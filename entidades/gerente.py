from entidades.usuario import Usuario


class Gerente(Usuario):
    def __init__(self, nome: str, cpf: str, senha: str):
        super().__init__(nome, senha, cpf)
