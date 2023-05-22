from telas.tela_solicitacao_de_visto import TelaSolicitacaoVisto


class ControladorSolicitacaoVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_solicitacao_visto = TelaSolicitacaoVisto()

    def abre_tela_solicitacao_visto(self):
        # tipos_visto -> vai ter que pegar os tipos de visto cadastrados
        tipo_visto, data, passaporte = self.__tela_solicitacao_visto.componentes_tela_solicitacao_visto_inicial(lista_tipos_visto=tipos_visto)
        solicitacao_valida = self.validar_infos_solicitacao(tipo_visto=tipo_visto, passaporte=passaporte)
        if solicitacao_valida:
            # abrir tela para verificar documentos
            pass

    def validar_infos_solicitacao(self, tipo_visto, passaporte):
        pass
        # validar se o passaporte consta na blacklist
        # validar se o passageiro já possui visto, e se sim, se é do tipo permanente ou se está expirado o visto
        # retorna True se sim e False se não
