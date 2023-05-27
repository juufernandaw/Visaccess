
class CampoVazioException(Exception):
    def __init__(self):
        self.mensagem = "Existe campos vazios, preencha todos os campos"
        super().__init__(self.mensagem)
