
class UsuarioInexistenteException(Exception):
    def __init__(self):
        self.mensagem = f"ATENÇAO: Usuário não existente. Favor escolher um usuário existente."
        super().__init__(self.mensagem)
