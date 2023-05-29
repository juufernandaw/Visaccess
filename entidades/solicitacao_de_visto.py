class SolicitacaoDeVisto:

    def __init__(self, data_solicitacao, documentos_verificados,
                 estrangeiro, status, visto):
        self.data_solicitacao = data_solicitacao
        self.documentos_verificados = documentos_verificados
        self.estrangeiro = estrangeiro
        self.status = status
        self.visto = visto
