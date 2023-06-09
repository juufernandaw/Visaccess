from entidades.estrangeiro import Estrangeiro
from persistencia.estrangeiroDAO import EstrangeiroDAO
from excecoes.valueErrorException import ValueErrorException
from excecoes.campovazioexception import CampoVazioException
from telas.tela_estrangeiro import TelaEstrangeiro
from datetime import datetime


class ControladorEstrangeiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__estrangeiro_dao = EstrangeiroDAO()
        self.__tela_estrangeiro = TelaEstrangeiro()
        self.__gerente_agente = None

    @property
    def estrangeiro_dao(self):
        return self.__estrangeiro_dao

    @property
    def tela_estrangeiro(self):
        return self.__tela_estrangeiro

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def gerente_agente(self):
        return self.__gerente_agente

    def abre_tela_inicial_estrangeiro(self,
                                      gerente_agente: str):  # abre a tela para cadastrar estrangeiro
        try:
            mexer_agente_opcoes = {1: self.adicionar_estrangeiro,
                                   2: self.excluir_estrangeiro,
                                   3: self.listar_estrangeiro,
                                   4: self.modificar_estrangeiro,
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
        except ValueErrorException:
            self.__tela_estrangeiro.mostra_mensagem("Tente novamente")
            self.abre_tela_inicial_estrangeiro()
        except ValueError:
            self.abre_tela_inicial_estrangeiro()
        except TypeError:
            self.abre_tela_inicial_estrangeiro() 

    def voltar_tela(self, escolha: str):
        if escolha == 'agente':
            return self.__controlador_sistema.get_controlador_agente.abre_tela_inicial()
        elif escolha == 'gerente':
            return self.__controlador_sistema.get_controlador_gerente.iniciar_tela_gerente()

    def adicionar_estrangeiro(self):
        try:
            # IR PARA TELA
            paises_sistema = self.controlador_sistema.get_controlador_pais.listar_paises_cadastrados()
            informacoes = self.tela_estrangeiro.tela_adicionar_estrangeiro(paises_sistema)
            if informacoes == 0:
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
            if informacoes != None:
                if informacoes[0] != '' and informacoes[1] != '' and informacoes[2] != '' and informacoes[3] != '' and \
                        informacoes[4] != '' and informacoes[5] != '' and informacoes[6] != '' and informacoes[
                    7] != '' and informacoes[8] != '':
                    if informacoes[0] == '' or informacoes[1] == '' or informacoes[2] == '' or informacoes[3] == '' or \
                            informacoes[4] == '' or informacoes[5] == '' or informacoes[6] == '' or informacoes[
                        7] == '' or informacoes[8] == '':
                        raise CampoVazioException
                    #converte data str --> date
                    data_nascimento_string = informacoes[2] 
                    informacoes[2] =  datetime.strptime(data_nascimento_string, '%d/%m/%Y').date()
                    # buscar estrangeiro por passporte. Primeira opcao do dict
                    estrangeiro = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(informacoes[0])
                    if estrangeiro != None:
                        self.tela_estrangeiro.mostra_mensagem('Este estrangeiro já está cadastrado!')
                        return self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
                    else:
                        # CRIAR ENTIDADE
                        estrangeiro = Estrangeiro(informacoes[0], informacoes[1], informacoes[2], informacoes[3],
                                                  informacoes[4], informacoes[5], informacoes[6], informacoes[7],
                                                  informacoes[8])
                        # BANCO DE DADOS
                        self.estrangeiro_dao.cadastrar_estrangeiro(estrangeiro.passaporte, estrangeiro.nome, estrangeiro.data_nasc,
                                                                   estrangeiro.estado_civil, estrangeiro.pais, estrangeiro.estado,
                                                                   estrangeiro.cidade, estrangeiro.trabalho, estrangeiro.profissao)
                        self.tela_estrangeiro.mostra_mensagem('Estrangeiro cadastrado!')
                else:
                    self.tela_estrangeiro.mostra_mensagem('Campos vazios, preencha todos os campos!')
                    self.adicionar_estrangeiro()
            elif informacoes == 0:
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
        except ValueErrorException as e:
            self.tela_estrangeiro.mostra_mensagem(e)
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
        except CampoVazioException as e:
            self.tela_estrangeiro.mostra_mensagem(e)
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)

    def excluir_estrangeiro(self):
        passaporte = self.tela_estrangeiro.tela_excluir_estrangeiro()
        if passaporte != None or passaporte != 0:
            estrangeiro = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(passaporte[0])
            if estrangeiro != None:
                self.estrangeiro_dao.excluir_estrangeiro(passaporte[0])
                self.tela_estrangeiro.mostra_mensagem('Estrangeiro Excluído!')
                return self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
            else:
                self.tela_estrangeiro.mostra_mensagem('Estrangeiro Não está cadastrado!')
                return self.excluir_estrangeiro()
        

    def listar_estrangeiro(self):
        estrangeiro = self.estrangeiro_dao.buscar_todos_estrangeiros()
        opcao = self.tela_estrangeiro.tela_listar_estrangeiro(estrangeiro)
        if opcao == 0:
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)

    def modificar_estrangeiro(self):
        paises_sistema = self.controlador_sistema.get_controlador_pais.listar_paises_cadastrados()
        passaporte = self.tela_estrangeiro.tela_modificar_estrangeiro()
        if passaporte == '':
            self.__tela_estrangeiro.mostra_mensagem('Passaporte não localizado')
            self.abre_tela_inicial_estrangeiro()
        try:
            if passaporte == 0:
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
            if passaporte != None:
                estrangeiro = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(passaporte[0])
                if estrangeiro != None:
                    dados_novos = self.tela_estrangeiro.tela_atualizar_estrangeiro(paises_sistema)
                    if dados_novos != None:
                        if dados_novos[0] != '' and dados_novos[1] != '' and dados_novos[2] != '' and dados_novos[
                            3] != '' and dados_novos[4] != '' and dados_novos[5] != '' and dados_novos[6] != '' and \
                                dados_novos[7] != '' and dados_novos[8] != '':
                                    #busca pelo passaporte o estrangeiro
                            passaporte = self.estrangeiro_dao.buscar_estrangeiro_por_passaporte(dados_novos[0])
                            if passaporte == None:
                                self.estrangeiro_dao.atualizar_estrangeiro(
                                    dados_novos[0],
                                    dados_novos[1],
                                    dados_novos[2],
                                    dados_novos[3],
                                    dados_novos[4],
                                    dados_novos[5],
                                    dados_novos[6],
                                    dados_novos[7],
                                    dados_novos[8],
                                    estrangeiro['passaporte'],
                                )
                                self.tela_estrangeiro.mostra_mensagem('Estrangeiro Modificado!')
                                return self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
                            else:
                                self.tela_estrangeiro.mostra_mensagem('Passaporte já consta no sistema!')
                                self.modificar_estrangeiro()
                        else:
                            self.tela_estrangeiro.mostra_mensagem('Campos vazios, preencha todos os campos!')
                            return self.modificar_estrangeiro()
                else:
                    self.tela_estrangeiro.mostra_mensagem("Estrangeiro não localizado")
                    self.modificar_estrangeiro()
            elif passaporte == 0:
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
            else:
                self.tela_estrangeiro.mostra_mensagem('Passaporte não encontrado!')
                self.abre_tela_inicial_estrangeiro(self.__gerente_agente)
        except:
            self.abre_tela_inicial_estrangeiro(self.__gerente_agente)

    def encontra_passageiro(self, passaporte: str):
        passageiro_encontrado = self.__estrangeiro_dao.get_estrangeiro_by_passaporte(passaporte=passaporte)
        return bool