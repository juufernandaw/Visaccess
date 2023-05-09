import datetime


class Estrangeiro:
    def __init__(self, nome: str, passaporte: str, data_nasc: datetime, estado_civil: str, pais: str, estado: str, cidade: str, trabalho: bool, profissao: str ):
        self.__nome = nome
        self.__passaporte = passaporte
        self.__data_nasc = data_nasc
        self.__estado_civil = estado_civil
        self.__pais = pais
        self.__estado = estado
        self.__cidade = cidade
        self.__trabalho = trabalho
        self.__profissao = profissao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def passaporte(self):
        return self.__passaporte

    @passaporte.setter
    def passaporte(self, passaporte: str):
        self.__passaporte = passaporte

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc: datetime):
        self.__data_nasc = data_nasc

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil: str):
        self.__estado_civil = estado_civil

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais: str):
        self.__pais = pais

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def trabalho(self):
        return self.__trabalho

    @trabalho.setter
    def trabalho(self, trabalho: bool):
        self.__trabalho = trabalho

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao: str):
        self.__profissao = profissao
