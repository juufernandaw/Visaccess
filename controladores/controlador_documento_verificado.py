from telas.tela_documento_verificado import TelaDocumentoVerificado
from persistencia.documento_verificadoDAO import DocumentoVerificadoDAO


class ControladorDocumentoVerificado:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_documento_verificado = TelaDocumentoVerificado()
        self.__documento_verificado_DAO = DocumentoVerificadoDAO()

    def abre_tela_documento_verificado(self, documentos, id_solicitacao_visto):
        docs_preenchidos = self.__tela_documento_verificado.tela_documento_verificado(lista_documentos=documentos)
        docs = []
        for k, v in docs_preenchidos.items():
            preenchido = 1 if v else 0
            doc_verificado = self.__documento_verificado_DAO.create_documento_verificado(id_solicitacao_visto=id_solicitacao_visto, preenchido=preenchido,
                                                                        documento=k)
            docs.append(doc_verificado)
        return docs
