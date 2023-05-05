from documento_verificado import DocumentoVerificado


class SolicitacaoDeVisto:

    def __init__(self, data_solicitacao: str, documentos_verificados: [DocumentoVerificado]):
        self.data_solicitacao = data_solicitacao
        self.documentos_verificados = documentos_verificados
