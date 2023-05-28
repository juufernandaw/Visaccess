from telas.tela_documento_verificado import TelaDocumentoVerificado
from persistencia.documento_verificadoDAO import DocumentoVerificadoDAO


class ControladorDocumentoVerificado:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_documento_verificado = TelaDocumentoVerificado()
        self.__documento_verificado_DAO = DocumentoVerificadoDAO()

    def abre_tela_documento_verificado(self, documentos, id_solicitacao_visto):
        docs_preenchidos = self.__tela_documento_verificado.tela_documento_verificado(lista_documentos=documentos)
        for doc in docs_preenchidos:
            self.__documento_verificado_DAO.create_documento_verificado(id_solicitacao_visto=id_solicitacao_visto, preenchido=doc.preenchido)
            # instanciar aqui a classe documento verificado para cada documento verificado e salvar no BD
        return
