from persistencia.paisDAO import PaisDAO
from entidades.pais import Pais
from telas.tela_pais import TelaPais
from excecoes.valueErrorException import ValueErrorException
from excecoes.campovazioexception import CampoVazioException

class pais:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pais_DAO = PaisDAO()
        self.__tela_pais = TelaPais()

    @property
    def pais_dao(self):
        return self.__pais_DAO

    @property
    def tela_pais(self):
        return self.__tela_pais
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def abre_tela_inicial_pais(self, gerente_agente:str):  # abre a tela para cadastrar pais
        try:
            mexer_agente_opcoes = {1: self.adicionar_pais,
                                  2: self.excluir_pais,
                                  3: self.listar_pais,
                                  4: self.modificar_pais,
                                  0: self.voltar_tela
                                  }
            while True:
                self.__gerente_agente = gerente_agente
                opcao_escolhida = self.__tela_estrangeiro.tela_cadastro_estrangeiro()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                else:
                    funcao_escolhida = mexer_agente_opcoes[opcao_escolhida]
                    if gerente_agente == 'agente' and opcao_escolhida == 0:
                        return self.voltar_tela('agente')
                    elif gerente_agente == 'gerente' and opcao_escolhida == 0:
                        return self.voltar_tela('gerente')
                    return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_pais.mostra_mensagem("Tente novamente")
            self.abre_tela_inicial_pais()

    def voltar_tela(self, escolha:str):
        if escolha == 'agente':
            return self.__controlador_sistema.controlador_agente.abre_tela_inicial()
        elif escolha == 'gerente':
            return self.__controlador_sistema.controlador_gerente.iniciar_tela_gerente()

    def adicionar_pais(self):
        try:
            #IR PARA TELA
            informacoes = self.tela_estrangeiro.tela_adicionar_estrangeiro()
            if informacoes != None:
                if informacoes[0] != '' and informacoes[1] != '' and informacoes[2] != '' and informacoes[3] != '' and informacoes[4] != '' and informacoes[5] != '' and informacoes[6] != '' and informacoes[7] != '' and informacoes[8] != '':
                    if informacoes[0] == '' or informacoes[1] == '' or informacoes[2] == '' or informacoes[3] == '' or informacoes[4] == '' or informacoes[5] =='' or informacoes[6] == '' or informacoes[7] =='' or informacoes[8] == '':
                        raise CampoVazioException
                    #buscar estrangeiro por passporte. Primeira opcao do dict
                    agente = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(informacoes[0])
                    if agente != None:
                        self.tela_estrangeiro.mostra_mensagem('Este estrangeiro já está cadastrado!')
                        return self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
                    else:
                        #CRIAR ENTIDADE
                        estrangeiro = Estrangeiro(informacoes[0], informacoes[1], informacoes[2],informacoes[2],informacoes[4],informacoes[5],informacoes[6],informacoes[7],informacoes[8])
                        #BANCO DE DADOS
                        self.estrangeiro_dao.cadastrar_estrangeiro(estrangeiro.passaporte, estrangeiro.nome, estrangeiro.data_nasc, estrangeiro.estado_civil, estrangeiro.pais, estrangeiro.estado, estrangeiro.cidade, estrangeiro.trabalho, estrangeiro.profissao)
                        self.tela_estrangeiro.mostra_mensagem('Estrangeiro cadastrado!')
                else:
                    self.tela_estrangeiro.mostra_mensagem('Dados Incorretos, preencha corretamente os campos!')
        except ValueErrorException as e:
            self.tela_estrangeiro.mostra_mensagem(e)
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
        except CampoVazioException as e:
            self.tela_estrangeiro.mostra_mensagem(e)
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)             

    def excluir_pais(self):
        exclui_pais = self.tela_pais.tela_excluir_pais()
        if exclui_pais != None:
            pais = self.pais_dao.buscar_pais_por_nome(exclui_pais[0])
            if pais != None:
                self.pais_dao.excluir_pais(pais[0])
                self.tela_pais.mostra_mensagem('País Excluído!')
                return self.abre_tela_inicial_pais()
            else:
                self.tela_pais.mostra_mensagem('País não está cadastrado!')
                return self.excluir_pais()

    def listar_pais(self):
        pais = self.pais_dao.buscar_todos_paises()
        opcao = self.tela_pais.tela_listar_pais(pais)
        if opcao == 'Voltar':
            return self.abre_tela_inicial_pais(self.__gerente_agente)
        
    def modificar_pais(self):
        passaporte = self.tela_estrangeiro.tela_modificar_estrangeiro()
        try:
            if passaporte != None:
                estrangeiro = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(passaporte[0])
                if estrangeiro != None:
                        dados_novos = self.tela_estrangeiro.tela_atualizar_estrangeiro()
                        if dados_novos != None:
                            if dados_novos[0]!= '' and dados_novos[1]!= '' and dados_novos[2]!= '' and dados_novos[3]!= '' and dados_novos[4]!= '' and dados_novos[5]!= '' and dados_novos[6]!= '' and dados_novos[7]!= '' and dados_novos[8] != '':
                                passaporte = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(dados_novos[0])
                                if passaporte != None:
                                    self.estrangeiro_dao.atualizar_estrangeiro(
                                        estrangeiro['passaporte'], 
                                        dados_novos[0], 
                                        dados_novos[1], 
                                        dados_novos[2], 
                                        dados_novos[3],
                                        dados_novos[4],
                                        dados_novos[5],
                                        dados_novos[6],
                                        dados_novos[7],
                                        dados_novos[8],
                                    )
                                    self.tela_estrangeiro.mostra_mensagem('Estrangeiro Modificado!')
                                    return self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
                            else:
                                self.tela_estrangeiro.mostra_mensagem('Preencha todos os campos!')
                                return self.modificar_estrangeiro()
            else:
                self.tela_estrangeiro.mostra_mensagem('Passaporte não encontrado!')
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente) 
        except:
            self.modificar_estrangeiro()

