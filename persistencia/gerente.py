from persistencia.DAO import DAO
from entidades.gerente import Gerente


class GerenteDAO(DAO):
    def __init__(self):
        super().__init__('gerente.pkl')

    def add(self, gerente: Gerente):
        super().add(gerente.cpf, gerente)  # passa a chave e o objeto

    def get(self, cpf_gerente: str):
        return super().get(cpf_gerente)

    def remove(self, gerente: Gerente):
        super().remove(gerente.cpf)
