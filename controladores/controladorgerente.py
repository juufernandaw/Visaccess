from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from persistencia.gerente import GerenteDAO
from telas.telasistema import TelaSistema


class ControladorGerente:
    def __init__(self, controlador_sistema):
        self.__gerente_dao = GerenteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_sistema = TelaSistema()

    def verificar_login_senha(self, cpf, senha):  # VERIFICAR o cpf e senha.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
                for agente in self.__gerente_dao.get_all():
                    if (agente.cpf == cpf) and (agente.senha == senha):
                        return True, agente  # agente q achou retornar
                    if agente.cpf != cpf or not agente.senha != senha:
                        raise LoginSenhaException
            except LoginSenhaException as e:
                self.__tela_sistema.mostrar_msg(e)
                self.__controlador_sistema.iniciar_tela_sistema()
            else:
                return False

    def abre_tela_inicial(self):  # abre a tela aluno pós login da tela
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

    def retornar(self):
        return self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial()
