from telas.tela_solicitacao_de_visto import TelaSolicitacaoVisto
from persistencia.solicitacaodevistoDAO import SolicitacaoDeVistoDAO


class ControladorSolicitacaoVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_solicitacao_visto = TelaSolicitacaoVisto()
        self.__solicitacao_de_visto_DAO = SolicitacaoDeVistoDAO()

    def abrir_tela_solicitacao(self):
        lista_tipos_visto = self.__controlador_sistema.get_controlador_tipos_visto.tipos_vistoDAO.buscar_todos_tipos_visto()
        nome_tipo_visto, passaporte, data = self.__tela_solicitacao_visto.tela_solicitacao_visto_inicial\
            (lista_tipos_visto=lista_tipos_visto)

        solicitacao_valida = self.validar_infos_solicitacao(passaporte=passaporte)
        if solicitacao_valida:
            # abrir tela para verificar documentos
            lista_documentos = self.__controlador_sistema.controlador_tipo_visto.tipo_vistoDAO.get_documentos_from_tipo_visto(tipo_visto=id_tipo_visto)

            solicitacao_visto = self.__solicitacao_de_visto_DAO.\
                create_solicitacao_visto(data_solicitacao=data, passaporte_estrangeiro=passaporte,
                                         status="aprovacao_pendente")
            # aqui retorna a instancia da classe solicitação de visto
            # mudar de composição p/ agregação
            # aqui embaixo vai instanciar e salvar no BD o documentopreenchido e vai vincular o id da solicitacao de visto com os documentos verificados
            self.__controlador_sistema.controlador_documento_verificado.\
                abre_tela_documento_verificado(documentos=lista_documentos, id_solicitacao=id_solicitacao_visto)

    def validar_infos_solicitacao(self, passaporte: str):
        # validar se o passaporte consta na blacklist
        estrangeiro_na_blacklist = self.__controlador_sistema.controlador_blacklist.validar_estrangeiro_blacklist(passaporte=passaporte)
        if estrangeiro_na_blacklist:
            return False
        # validar se o estrangeiro está cadastrado no sistema já. Retorna um dict se sim; senão retorna None
        estrangeiro_cadastrado = self.__controlador_sistema.controlador_estrangeiro.estrangeiroDAO.buscar_estrangeiro_por_passaporte(passaporte=passaporte)
        if not estrangeiro_cadastrado:   # retorna None se não tiver estrangeiro cadastrado
            return False
        # validar se o estrangeiro já possui visto, e se sim, se é do tipo permanente ou se está expirado o visto
        lista_solicitacoes_visto = self.__solicitacao_de_visto_DAO.find_solicitacao_para_passaporte(passaporte=passaporte)
        if lista_solicitacoes_visto == []:
            return True
        else:
            for solicitacao in lista_solicitacoes_visto:
                if solicitacao["visto"] == "permanente":
                    return False
                # reformular esse if
                if solicitacao["status"] == "expirado":
                    return True



