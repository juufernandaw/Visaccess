from entidades.gerente import Gerente
from entidades.agente import Agente


class Consulado:

    def __init__(self, sede: str):
        self.__sede = sede
        self.__gerente = None
        self.__agentes = list

    def cadastrar_gerente_para_consulado(self, gerente: Gerente):
        if gerente is not None and isinstance(gerente, Gerente):
            self.__gerente = gerente

    def cadastrar_agentes_para_consulado(self, agente: Agente):
        if agente is not None and isinstance(agente, Agente):
            self.__agentes.append(agente)
