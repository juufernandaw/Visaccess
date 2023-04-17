from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from persistencia.gerenteDAO import GerenteDAO
from telas.telagerente import TelaGerente
import sqlite3

class ControladorGerente:
    def __init__(self, controlador_sistema):
        self.__gerente_dao = GerenteDAO()
        self.__controlador_sistema = controlador_sistema
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
                # AQUI TEM QUE VOLTAR PARA A TELA LOGIN (ARRUMADO)!
                self.__controlador_sistema.iniciar_tela_sistema()


    def abrir_tela_cadastro(self):
        while True:
            opcao = self.__tela_gerente.tela_cadastro_agentes()
            if opcao == 1:
                self.adicionar_agente()
            elif opcao == 2:
                self.excluir_agente()
            elif opcao == 3:
                self.__tela_gerente.mostra_mensagem('Listar Agentes')
            elif opcao == 4:
                self.modificar_agente()
            elif opcao == 0:
                # AQUI TEM QUE VOLTAR PARA A TELA INICIAL DO GERENTE!
                self.iniciar_tela_gerente()

    def adicionar_agente(self):
        data = self.__tela_gerente.tela_adicionar_agentes()
        print(data)
        # *pega os dados, testa e joga no BD (fazer ainda).
        if data != None:
            # aqui tem que mandar o objeto 'data' para o BD.
            pass
    
    def excluir_agente(self):
        data = self.__tela_gerente.tela_excluir_agentes()
        print(data)

        if data != None:
            # aqui tem que comparar o objeto 'data', que contém apenas um cpf, com os cpf do BD.
            # caso há algum igual, exclui.
            # caso contrário, pop-up de erro.
            pass

    def modificar_agente(self):
        data = self.__tela_gerente.tela_modificar_agentes()
        print(data)

        if data != None:
            # aqui tem que comparar o objeto 'data', que contém apenas um cpf, com os cpf do BD.
            # caso há algum igual, exclui.
            # caso contrário, pop-up de erro.
            pass

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

    def verificar_login_senha_sqlite(self, cpf, senha):  # VERIFICAR o cpf e senha pelo sqlite.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
              conn = sqlite3.connect('visaccess.bd') # Cria uma conexão com o banco de dados
              cursor = conn.cursor() # Cria um objeto cursor
              cursor.execute("SELECT * FROM gerente WHERE cpf=?", (cpf,))
              resultado = cursor.fetchone()
              if resultado and resultado[2] == senha:
                  return True
            except LoginSenhaException as e:
                self.__tela_sistema.mostrar_msg(e)
                self.__controlador_sistema.iniciar_tela_sistema()
            else:
                return False

    def abre_tela_inicial(self):  # abre a tela gerente pos login
        try:
            usuario = self.__controlador_sistema.usuario_logado
            mexer_gerente_opcoes = {1: self.voltar_tela_sistema(),
                                  2: self.voltar_tela_sistema(),
                                  0: self.voltar_tela_sistema
                                  }
            while True:
                opcao_escolhida = self.__tela_gerente.tela_gerente_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 5 and opcao_escolhida != 0:
                    raise ValueErrorException
                else:
                    funcao_escolhida = mexer_gerente_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_aluno.mostrar_msg(e)
            self.abre_tela_inicial()

    def voltar_tela_sistema(self):
        return self.__controlador_sistema.iniciar_tela_sistema()


