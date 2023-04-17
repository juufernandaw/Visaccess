from persistencia.DAO import DAO
from entidades.agente import Agente
import sqlite3

class AgenteDAO(DAO):
    def __init__(self):
        super().__init__('agente.pkl')

    def add(self, agente: Agente):
        super().add(agente.cpf, agente)  # passa a chave e o objeto

    def get(self, cpf_agente: str):
        return super().get(cpf_agente)

    def remove(self, agente: Agente):
        super().remove(agente.cpf)

