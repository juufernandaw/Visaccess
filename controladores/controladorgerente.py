from excecoes.loginsenhaException import LoginSenhaException
from excecoes.valueErrorException import ValueErrorException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException
from persistencia.gerenteDAO import GerenteDAO
from persistencia.agenteDAO import AgenteDAO
from telas.telagerente import TelaGerente
from entidades.agente import Agente
from entidades.gerente import Gerente
import sqlite3

class ControladorGerente:
    def __init__(self, controlador_sistema):
        self.__gerente_dao = GerenteDAO()
        self.__agente_DAO = AgenteDAO()
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
                self.__controlador_sistema.controlador_agente.abrir_tela_cadastro()
            elif opcao == 4:
                self.__controlador_sistema.controlador_estrangeiro.abre_tela_inicial_estrangeiro()
            elif opcao == 5:
                self.__tela_gerente.mostra_mensagem('Emitir Relatório de Solicitações Aprovadas')
            elif opcao == 0:
                self.__controlador_sistema.iniciar_tela_sistema()

#--------------------- CADASTRO DE GERENTE -----------------------

    def abrir_tela_cadastro_gerente(self):
        try:
            # usuario = self.__controlador_sistema.usuario_logado
            mexer_gerente_opcoes = {1: self.incluir_gerente,
                                    2: self.excluir_gerente,
                                    3: self.listar_gerentes,
                                    4: self.alterar_gerente,
                                    0: self.abrir_tela_cadastro_gerente}
            while True:
                opcao_escolhida = self.__tela_gerente.tela_cadastro_gerentes()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = mexer_gerente_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as erro:
            self.__tela_gerente.mostra_mensagem(erro)
            self.abrir_tela_cadastro_gerente()


    def incluir_gerente(self):
        print("Entrou no incluir gerente controlador")
        evento, valores = self.__tela_gerente.pegar_dados_gerente()
        print(f"valores: {valores}")
        print(f"valores[cpf]: {valores['cpf']}")
        print(f"evento: {evento}")
        if evento == "Voltar":
            return self.abrir_tela_cadastro_gerente()
        
        for gerente in self.__gerente_dao.lista_gerentes():
            print('entro no for lista_gerente controlador')
            print(f"gerente controlador: {gerente}")
            print(f"cpf gerente controlador: {gerente['cpf']}")
            if valores['cpf'] == gerente:
                self.__tela_gerente.mostra_mensagem("Este gerente já consta no sistema!")
                return self.incluir_gerente()
        
        else:
            print('entrou no else')
            if valores['cpf'] == "":
                print('entrou no cpf vazio')
                self.__tela_gerente.mostra_mensagem("O cpf não pode ser vazio!")
                return self.incluir_gerente()
            gerente = Gerente(valores['nome'], valores['senha'], valores['cpf'], valores['consulado'])
            print(f'gerente: {gerente}')
            if gerente is not None:
                print('entrou no gerente is not none')
                self.__gerente_dao.cria_gerente(gerente)
                self.__tela_gerente.mostra_mensagem("Gerente cadastrado com sucesso!")
                return self.abrir_tela_cadastro_gerente()

    def alterar_gerente(self):
        print("Entrou no alterar gerente controlador")
        evento, valores = self.__tela_gerente.escolher_gerente_para_alterar()
        if evento == 'Voltar':
            return self.abrir_tela_cadastro_gerente()
        for gerente in self.__gerente_dao.lista_gerentes():
            print('entrou no for')
            if int(valores["cpf"]) == gerente['cpf']:
                evento, gerente_novo = self.__tela_gerente.alterar_gerente(gerente)
                if evento == 'Voltar':
                    return self.abrir_tela_cadastro_gerente()
                print(f"gerente novo: {gerente_novo}")
                print(f"gerente novo cpf: {gerente_novo['cpf']}")
                if gerente_novo is not None:
                    print('entrou no if')
                    if gerente_novo["cpf"] == "":
                        self.__tela_gerente.mostra_mensagem("O CPF do Gerente não pode ser vazio!")
                        return self.alterar_gerente()
                    self.__gerente_dao.atualizar_gerente(gerente_novo, gerente['cpf'])
                    self.__tela_gerente.mostra_mensagem("Gerente alterado com sucesso!")
                    return self.abrir_tela_cadastro_gerente()
        else:
            self.__tela_gerente.mostra_mensagem("Este gerente NÃO consta no sistema!")
            return self.abrir_tela_cadastro_gerente()

    def excluir_gerente(self):
        print("Entrou no excluir gerente controlador")
        evento, gerente_excluir = self.__tela_gerente.excluir_gerente()
        if evento == "Voltar":
            return self.abrir_tela_cadastro_gerente()
        for gerente in self.__gerente_dao.lista_gerentes():
            print('entrou no for do excluir')
            if gerente['cpf'] == int(gerente_excluir['cpf']):
                print('entrou no if')
                self.__gerente_dao.remover_gerente(gerente)
                self.__tela_gerente.mostra_mensagem("Gerente excluído com sucesso!")
                return self.abrir_tela_cadastro_gerente()
        else:
            print('entrou no else')
            self.__tela_gerente.mostra_mensagem("Este gerente NÃO consta no sistema!")
            return self.abrir_tela_cadastro_gerente()

    def listar_gerentes(self):
        print("Entrou no listar gerente controlador")
        gerentes = self.__gerente_dao.lista_gerentes()
        evento, values = self.__tela_gerente.listar_gerentes(gerentes)



#--------------------- VERIFICAÇÃO LOGIN -----------------------

    # def verificar_login_senha(self, cpf, senha):  # VERIFICAR o cpf e senha.
    #     if isinstance(cpf, str) and isinstance(senha, str):
    #         try:
    #             for gerente in self.__gerente_dao.get_all():
    #                 if (gerente.cpf == cpf) and (gerente.senha == senha):
    #                     return True, gerente  # gerente q achou retornar
    #                 if gerente.cpf != cpf or not gerente.senha != senha:
    #                     raise LoginSenhaException
    #         except LoginSenhaException as e: #exception para login e senha errada
    #             self.__tela_sistema.mostrar_msg(e)
    #             self.__controlador_sistema.iniciar_tela_sistema() #voltar para a inicial do sistema
    #         else:
    #             return False

    def verificar_login_senha_sqlite(self, cpf, senha):  # VERIFICAR o cpf e senha pelo sqlite.
        if isinstance(cpf, str) and isinstance(senha, str):
            try:
              gerente = self.__gerente_dao.buscar_gerente_por_cpf(cpf)
              senha_digitada = senha
              senha_conferir = str(gerente.senha)
              if gerente is not None and senha_conferir == senha_digitada:
                  return True
              elif gerente is None:
                  raise UsuarioInexistenteException
            except LoginSenhaException as e:
                self.__tela_sistema.mostrar_msg(e)
            except UsuarioInexistenteException as e:
                self.__tela_sistema.mostrar_msg(e)
            else:
                return False


    # def abre_tela_inicial_gerente(self):  # abre a tela gerente pos login
    #     try:
    #         mexer_gerente_opcoes = {1: self.voltar_tela_sistema(),
    #                               2: self.voltar_tela_sistema(),
    #                               0: self.voltar_tela_sistema
    #                               }
    #         while True:
    #             opcao_escolhida = self.__tela_gerente.tela_gerente_inicial()
    #             if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 5 and opcao_escolhida != 0:
    #                 raise ValueErrorException
    #             else:
    #                 funcao_escolhida = mexer_gerente_opcoes[opcao_escolhida]
    #                 return funcao_escolhida()
    #     except ValueErrorException as e:
    #         self.__tela_aluno.mostrar_msg(e)
    #         self.abre_tela_inicial()

    def voltar_tela_sistema(self):
        return self.__controlador_sistema.iniciar_tela_sistema()


