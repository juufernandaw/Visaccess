from telas.tela_solicitacao_de_visto import TelaSolicitacaoVisto
from persistencia.solicitacaodevistoDAO import SolicitacaoDeVistoDAO


class ControladorSolicitacaoVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_solicitacao_visto = TelaSolicitacaoVisto()
        self.__solicitacao_de_visto_DAO = SolicitacaoDeVistoDAO()

    def abrir_tela_solicitacao(self):
        lista_tipos_visto = self.__controlador_sistema.get_controlador_tipos_visto.get_tipos_vistoDAO.buscar_todos_tipos_visto()
        nome_tipo_visto, passaporte, data = self.__tela_solicitacao_visto.tela_solicitacao_visto_inicial\
            (lista_tipos_visto=lista_tipos_visto)
        valid_visa = self.validar_infos_solicitacao(passaporte=passaporte)
        if valid_visa:
            lista_documentos = self.__controlador_sistema.get_controlador_tipos_visto.get_tipos_vistoDAO.\
                buscar_documentos_por_visto(visa_name=nome_tipo_visto)
            solicitacao_visto, id_solicitacao_visto = self.__solicitacao_de_visto_DAO.\
                create_solicitacao_visto(data_solicitacao=data, passaporte_estrangeiro=passaporte,
                                         status="aprovacao_pendente", nome_visto=nome_tipo_visto)
            docs_verificados = self.__controlador_sistema.get_controlador_documento_verificado.\
                abre_tela_documento_verificado(documentos=lista_documentos, id_solicitacao_visto=id_solicitacao_visto)
            print(docs_verificados)
            solicitacao_visto.documentos_verificados = docs_verificados
            self.__tela_solicitacao_visto.mostrar_msg_tela("Solicitação de visto enviada para aprovação!")
            return
        else:
            self.abrir_tela_solicitacao()

    def validar_infos_solicitacao(self, passaporte: str):
        estrangeiro_na_blacklist = self.__controlador_sistema.get_controlador_blacklist.\
            validar_estrangeiro_blacklist(passaporte=passaporte)
        if estrangeiro_na_blacklist:
            self.__controlador_sistema.get_controlador_estrangeiro.tela_estrangeiro.mostra_mensagem\
                ("Não é possível solicitar visto para tal passaporte, pois o mesmo encontra-se presente na blacklist")
            return False
        estrangeiro_cadastrado = self.__controlador_sistema.get_controlador_estrangeiro.estrangeiro_dao.\
            buscar_estrangeiro_por_passaporte(passaporte=passaporte)
        if not estrangeiro_cadastrado:
            self.__controlador_sistema.get_controlador_estrangeiro.tela_estrangeiro.\
                mostra_mensagem("Passaporte não cadastrado no sistema."
                                "Favor cadastrar o estrangeiro antes de solicitar o visto")
            return False
        lista_solicitacoes_visto = self.__solicitacao_de_visto_DAO.\
            find_solicitacao_para_passaporte(passaporte=passaporte)
        if lista_solicitacoes_visto == []:
            return True
        else:
            for id, passageiro, visto, status in lista_solicitacoes_visto:
                if visto.upper() == "PERMANENTE":
                    self.__tela_solicitacao_visto.mostrar_msg_tela(
                        "Não é possível cadastrar outra solicitação de visto para esse passaporte,"
                        " pois o mesmo já possui um visto do tipo permanente")
                    return False
                if status != "expirado":
                    self.__tela_solicitacao_visto.mostrar_msg_tela(
                        "Não é possível cadastrar outra solicitação de visto para esse passaporte, "
                        "pois o mesmo já possui outro visto com status válido")
                    return False

    def aprovar_solicitacao_visto(self):
        lista_solicitacoes_visto = self.__solicitacao_de_visto_DAO.buscar_todas_solicitacoes_visto()
        solicitacao_escolhida = self.__tela_solicitacao_visto.tela_selecionar_visto_aprovar(lista_solicitacoes_visto=lista_solicitacoes_visto)

        if not solicitacao_escolhida:
            return

        # get estrangeiro
        estrangeiro_solicitando = self.__controlador_sistema.get_controlador_estrangeiro.estrangeiro_dao.buscar_estrangeiro_por_passaporte(solicitacao_escolhida)

        # get solicitação
        solicitacao_completa = self.__solicitacao_de_visto_DAO.find_solicitacao_para_passaporte(solicitacao_escolhida)

        # get documentos do visto
        lista_documentos_necessarios_visto = self.__controlador_sistema.get_controlador_tipos_visto.get_tipos_vistoDAO.buscar_documentos_por_visto(solicitacao_completa[0][2])

        # get documentos da solicitação
        documentos_aprovados = self.__controlador_sistema.get_controlador_documento_verificado.get_documento_verificadoDAO.buscar_documentos_por_solicitacao(solicitacao_completa[0][0])
        lista_documentos = []
        for doc in documentos_aprovados:
            if doc[1] == 1:
                lista_documentos.append(doc[0])

        decisao = self.__tela_solicitacao_visto.tela_aprovar_visto(estrangeiro_solicitando, lista_documentos, lista_documentos_necessarios_visto)
        print(decisao)
        print(solicitacao_completa)
        if decisao == True:
            self.__solicitacao_de_visto_DAO.alterar_status_solicitacao(solicitacao_completa[0][0], 'aprovado')
        else:
            self.__solicitacao_de_visto_DAO.alterar_status_solicitacao(solicitacao_completa[0][0], 'recusado')
