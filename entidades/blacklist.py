class Blacklist:

    def __init__(self, nome: str, passaporte: str):
        self.__nome = nome
        self.__passaporte = passaporte

    def get_nome(self):
        return self.__nome

    def get_passaporte(self):
        return self.__passaporte
