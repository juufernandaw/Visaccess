
class LoginSenhaException(Exception):
    def __init__(self):
        self.mensagem = "Login e senha inválidos, escreva novamente"
        super().__init__(self.mensagem)
