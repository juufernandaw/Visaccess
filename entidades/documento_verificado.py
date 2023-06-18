from entidades.documento import Documento


class DocumentoVerificado:

    def __init__(self, documento: Documento, preenchido: bool):
        self.documento = documento
        self.preenchido = preenchido
