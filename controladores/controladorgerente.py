from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from persistencia.gerente import GerenteDAO
from telas.telasistema import TelaSistema
from telas.telagerente import TelaGerente


class ControladorGerente:
    def __init__(self, controlador_sistema):
        self.__gerente_dao = GerenteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_sistema = TelaSistema()
        self.__tela_gerente = TelaGerente()

# ---------- TELA GERENTE ABAIXO -----------------------

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

#--------------------- TELA GERENTE ACIMA -----------------------

    def verificar_login_senha(self, cpf, senha):  # VERIFICAR o cpf e senha.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
                for gerente in self.__gerente_dao.get_all():
                    if (gerente.cpf == cpf) and (gerente.senha == senha):
                        return True, gerente  # gerente q achou retornar
                    if gerente.cpf != cpf or not gerente.senha != senha:
                        raise LoginSenhaException
            except LoginSenhaException as e: #exception para login e senha errada
                self.__tela_sistema.mostrar_msg(e)
                self.__controlador_sistema.iniciar_tela_sistema() #voltar para a inicial do sistema
            else:
                return False

    def abre_tela_inicial(self):  # abre a tela gerente pos login
        try:
            usuario = self.__controlador_sistema.usuario_logado
            mexer_aluno_opcoes = {1: self.voltar_tela_sistema(),
                                  2: self.voltar_tela_sistema(),
                                  0: self.voltar_tela_sistema
                                  }
            while True:
                opcao_escolhida = self.__tela_aluno.abre_tela_inicial_tela_aluno()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueErrorException
                if opcao_escolhida == 1:
                    return self.consultar_treino_aluno(usuario.treinos)
                else:
                    funcao_escolhida = mexer_aluno_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_aluno.mostrar_msg(e)
            #  self.__tela_aluno.mostrar_msg("Digite uma das opções sugeridas, por favor")
            self.abre_tela_inicial()

    def voltar_tela_sistema(self):
        return self.__controlador_sistema.iniciar_tela_sistema()


