class Documento:

    def __init__(self, nome: str, regra: str):
        self.__nome = nome
        self.__regra = regra

    @property
    def nome(self):
        return self.__nome

    @property
    def regra(self):
        return self.__regra
