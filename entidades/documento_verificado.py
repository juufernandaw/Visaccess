from documento import Documento


class DocumentoVerificado:

    def __init__(self, documento: Documento, verificado: bool):
        self.documento = documento
        self.verificado = verificado
