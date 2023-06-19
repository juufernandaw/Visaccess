class Pais:

    def __init__(self, isento: str, nome: str):
        self.__isento = isento
        self.__nome = nome

    @property
    def isento(self):
        return self.__isento

    @isento.setter
    def isento(self, isento: str):
        self.__isento = isento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
