class CampoVazioException(Exception):
    def __init__(self):
        self.mensagem = "Campos vazios, preencha todos os campos!"
        super().__init__(self.mensagem)
