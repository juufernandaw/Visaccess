from abc import ABC, abstractmethod
import pickle


class DAO(ABC):
    @abstractmethod
    def __init__(self, nome_arquivo=""):
        self.__nome_arquivo = nome_arquivo
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):  # exclui o que tem na memória
        self.__object_cache = pickle.load(open(self.__nome_arquivo, 'rb'))

    def __dump(self):  # pega o que tava na cache e manda pro arquivo
        pickle.dump(self.__object_cache, open(self.__nome_arquivo, 'wb'))

    def add(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()  # grava no arquivo

    def get(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__object_cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):  # lista completa
        return list(self.__object_cache.values())

    def update(self):
        self.__dump()
