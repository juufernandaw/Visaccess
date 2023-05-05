from documento_verificado import DocumentoVerificado
from estrangeiro import Estrangeiro
from tipo_de_visto import TipoDeVisto


class SolicitacaoDeVisto:

    def __init__(self, data_solicitacao: str, documentos_verificados: [DocumentoVerificado],
                 estrangeiro: Estrangeiro, status: bool, visto: TipoDeVisto):
        self.data_solicitacao = data_solicitacao
        self.documentos_verificados = documentos_verificados
        self.estrangeiro = estrangeiro
        self.status = status
        self.visto = visto
