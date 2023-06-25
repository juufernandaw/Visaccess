class Pais:

    def __init__(self, nome: str, isento: str):
        self.__isento = isento
        self.__nome = nome

    @property
    def get_isento(self):
        return self.__isento

    @get_isento.setter
    def isento(self, isento: str):
        self.__isento = isento

    @property
    def get_nome(self):
        return self.__nome

    @get_nome.setter
    def nome(self, nome: str):
        self.__nome = nome
