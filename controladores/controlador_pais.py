from persistencia.paisDAO import PaisDAO
from entidades.pais import Pais
from telas.tela_pais import TelaPais
from excecoes.valueErrorException import ValueErrorException
from excecoes.campovazioexception import CampoVazioException

class ControladorPais:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pais_DAO = PaisDAO()
        self.__tela_pais = TelaPais()

    @property
    def get_pais_dao(self):
        return self.__pais_DAO

    @property
    def get_tela_pais(self):
        return self.__tela_pais
    
    @property
    def get_controlador_sistema(self):
        return self.__controlador_sistema

    def abre_tela_inicial_pais(self):  # abre a tela para cadastrar pais
        try:
            mexer_pais_opcoes = {1: self.adicionar_pais,
                                  2: self.excluir_pais,
                                  3: self.listar_pais,
                                  4: self.modificar_pais,
                                  0: self.voltar_tela
                                  }
            while True:
                opcao_escolhida = self.__tela_pais.tela_cadastro_pais()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                else:
                    if opcao_escolhida == 0:
                        return self.voltar_tela()
                    funcao_escolhida = mexer_pais_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_pais.mostra_mensagem("Tente Novamente uma opção válida")
            self.abre_tela_inicial_pais()

    def voltar_tela(self):
            return self.__controlador_sistema.get_controlador_consul.abre_tela_inicial()

    def adicionar_pais(self):
        try:
            #IR PARA TELA
            informacoes = self.get_tela_pais.tela_adicionar_pais()
            if informacoes == 0:
                self.abre_tela_inicial_pais()
            if informacoes != None:
                if informacoes[0] != '' and informacoes[1] != '':
                    if informacoes[0] == '' or informacoes[1] == '':
                        raise CampoVazioException
                    pais = self.get_pais_dao.buscar_pais_por_nome(informacoes[0])
                    if pais != None:
                        self.get_tela_pais.mostra_mensagem('Este País já está cadastrado!')
                        return self.abre_tela_inicial_pais()
                    else:
                        #CRIAR ENTIDADE
                        pais = Pais(informacoes[0], informacoes[1])
                        #BANCO DE DADOS
                        self.get_pais_dao.cadastrar_pais(pais.nome, pais.isento)
                        self.get_tela_pais.mostra_mensagem('País cadastrado!')
                        self.abre_tela_inicial_pais()
                else:
                    self.get_tela_pais.mostra_mensagem('Dados Incorretos, preencha corretamente os campos pais e isento!')
                    self.adicionar_pais()

        except CampoVazioException as e:
            self.get_tela_pais.mostra_mensagem(e)
            self.abre_tela_inicial_pais()             

    def excluir_pais(self):
        exclui_pais = self.get_tela_pais.tela_excluir_pais()
        if exclui_pais == 0 or exclui_pais == 'Voltar':
            return self.abre_tela_inicial_pais()
        if exclui_pais != None:
            pais = self.get_pais_dao.buscar_pais_por_nome(exclui_pais[0])
            if pais != None:
                self.get_pais_dao.excluir_pais(pais['nome'])
                self.get_tela_pais.mostra_mensagem('País Excluído!')
                return self.abre_tela_inicial_pais()
            else:
                self.get_tela_pais.mostra_mensagem('País não está cadastrado!')
                return self.excluir_pais()
        

    def listar_pais(self):
        pais = self.get_pais_dao.buscar_todos_paises()
        opcao = self.get_tela_pais.tela_listar_pais(pais)
        if opcao == 0:
            return self.abre_tela_inicial_pais()

    def listar_paises_cadastrados(self):
        return self.get_pais_dao.listar_todos_paises_cadastrados()
     
    def modificar_pais(self):
        nome_pais = self.get_tela_pais.tela_modificar_pais()
        if nome_pais == 0:
            self.abre_tela_inicial_pais()
        try:
            if nome_pais != None:
                pais = self.get_pais_dao.buscar_pais_por_nome(nome_pais[0])
                if pais != None:
                        dados_novos = self.get_tela_pais.tela_atualizar_pais()
                        if dados_novos != None:
                            if dados_novos[0]!= '' and dados_novos[1]!= '':
                                nome_pais_teste = self.get_pais_dao.buscar_pais_por_nome(dados_novos[0])
                                if nome_pais_teste == None:
                                    self.get_pais_dao.atualizar_pais(
                                        dados_novos[0], 
                                        dados_novos[1],
                                        pais['nome'] 
                                    )
                                    self.get_tela_pais.mostra_mensagem('País Modificado!')
                                    return self.abre_tela_inicial_pais()
                            else:
                                self.get_tela_pais.mostra_mensagem('Preencha todos os campos!')
                                return self.modificar_pais()
                        else:
                            self.get_tela_pais.mostra_mensagem('Preencha novamente')
                            self.modificar_pais()
                if pais == None:
                    self.get_tela_pais.mostra_mensagem('País não encontrado!')
                    self.abre_tela_inicial_pais()
            else:
                self.get_tela_pais.mostra_mensagem('País não encontrado!')
                self.abre_tela_inicial_pais() 
        except:
            self.modificar_pais()

