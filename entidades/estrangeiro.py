import datetime


class Estrangeiro:
    def __init__(self, passaporte: str, nome: str, data_nasc: datetime, estado_civil: str, pais: str, estado: str, cidade: str, trabalho: bool, profissao: str ):
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
    def get_nome(self):
        return self.__nome

    @get_nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def get_passaporte(self):
        return self.__passaporte

    @get_passaporte.setter
    def passaporte(self, passaporte: str):
        self.__passaporte = passaporte

    @property
    def get_data_nasc(self):
        return self.__data_nasc

    @get_data_nasc.setter
    def data_nasc(self, data_nasc: datetime):
        self.__data_nasc = data_nasc

    @property
    def get_estado_civil(self):
        return self.__estado_civil

    @get_estado_civil.setter
    def estado_civil(self, estado_civil: str):
        self.__estado_civil = estado_civil

    @property
    def get_pais(self):
        return self.__pais

    @get_pais.setter
    def pais(self, pais: str):
        self.__pais = pais

    @property
    def get_estado(self):
        return self.__estado

    @get_estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def get_cidade(self):
        return self.__cidade

    @get_cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def get_trabalho(self):
        return self.__trabalho

    @get_trabalho.setter
    def trabalho(self, trabalho: bool):
        self.__trabalho = trabalho

    @property
    def get_profissao(self):
        return self.__profissao

    @get_profissao.setter
    def profissao(self, profissao: str):
        self.__profissao = profissao
