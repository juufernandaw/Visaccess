class Blacklist:

    def __init__(self, nome: str, passaporte: str):
        self.__nome = nome
        self.__passaporte = passaporte

    def nome(self):
        return self.__nome

    def passaporte(self):
        return self.__passaporte
