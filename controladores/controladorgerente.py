from telas.telagerente import TelaGerente

class ControladorGerente:
    def __init__(self):
        self.__tela_gerente = TelaGerente()

    @property
    def tela_sistema(self):
        return self.__tela_gerente

    def iniciar_tela_gerente(self):
        while True:
            opcao = self.__tela_gerente.tela_gerente_inicial()
            if opcao == 1:
                self.__tela_gerente.mostra_mensagem('Cadastrar Solicitação de Visto')
            elif opcao == 2:
                self.__tela_gerente.mostra_mensagem('Aprovar Solicitação de Visto')
            elif opcao == 3:
                self.abrir_tela_cadastro()
            elif opcao == 4:
                self.__tela_gerente.mostra_mensagem('Cadastrar Estrangeiros')
            elif opcao == 5:
                self.__tela_gerente.mostra_mensagem('Emitir Relatório de Solicitações Aprovadas')
            elif opcao == 0:
                # AQUI TEM QUE VOLTAR PARA A 1 TELA!
                exit()

    def abrir_tela_cadastro(self):
        while True:
            opcao = self.__tela_gerente.tela_cadastro_agentes()
            if opcao == 1:
                self.adicionar_agente()
            elif opcao == 2:
                self.__tela_gerente.mostra_mensagem('Excluir Agente')
            elif opcao == 3:
                self.__tela_gerente.mostra_mensagem('Listar Agentes')
            elif opcao == 4:
                self.__tela_gerente.mostra_mensagem('Modificar dados de Agente')
            elif opcao == 0:
                # AQUI TEM QUE VOLTAR PARA A TELA INICIAL DO GERENTE!
                self.iniciar_tela_gerente()

    def adicionar_agente(self):
        opcao, name = self.__tela_gerente.tela_adicionar_agentes()
        if opcao == 1:
            print(name)
            self.abrir_tela_cadastro()
            # *pega os dados, testa e joga no BD.
        elif opcao == 2:
            self.__tela_gerente.close()
            self.abrir_tela_cadastro()
            # só volta e da uma mensagem de erro.
