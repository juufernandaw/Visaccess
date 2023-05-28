from telas.tela_documento import TelaDocumento
from entidades.documento import Documento
from persistencia.documentoDAO import DocumentoDAO
from excecoes.valueErrorException import ValueErrorException


class ControladorDocumento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_documento = TelaDocumento()
        self.__documento_DAO = DocumentoDAO()

    @property
    def documento_DAO(self):
        return self.__documento_DAO

    def abre_tela_cadastro_documentos(self):
        try:
            opcoes_documentos = {1: self.registra_novo_documento,
                                 2: self.exclui_documento,
                                 3: self.lista_documentos,
                                 4: self.altera_documento,
                                 0: self.abre_tela_cadastro_documentos}
            while True:
                opcao_escolhida = self.__tela_documento.tela_documento_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = opcoes_documentos[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_documento.exibe_mensagem_erro()
            self.abre_tela_cadastro_documentos()

    def lista_documentos(self):
        print('entrou no lista_documentos')
        documentos = self.__documento_DAO.get_all_documentos()
        botao, values = self.__tela_documento.mostra_lista_documentos(documentos)
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()

    def verifica_informacoes_preenchidas(self, nome: str, regra: str):
        if nome != "" and regra != "":
            print('dados do documento preenchidos')
            return True
        else:
            print('dados do documento NÃO preenchidos')
            return False

    def localiza_documento_pelo_nome(self, nome: str):
        for documento in self.__documento_DAO.get_all_documentos():
            if nome == documento['nome']:
                print('entrou no true')
                return True
        else:
            print('entrou no false')
            return False

    def registra_novo_documento(self):
        print('entrou no registra_novo_documento')
        botao, dados_documento = self.__tela_documento.pegar_dados_documento()
        print(dados_documento)
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()

        for documento in self.__documento_DAO.get_all_documentos():
            print(documento)
            if dados_documento['nome'] == documento['nome']:
                self.__tela_documento.exibe_mensagem_erro('Documento já consta no sistema')
                return self.registra_novo_documento()

        else:
            if self.verifica_informacoes_preenchidas(dados_documento['nome'], dados_documento['regra']):
                self.__documento_DAO.registra_documento(dados_documento['nome'], dados_documento['regra'])
                self.__tela_documento.exibe_mensagem_sucesso('Documento Cadastrado com Sucesso!')
                return self.abre_tela_cadastro_documentos()
            else:
                self.__tela_documento.exibe_mensagem_erro('As informações não podem estar vazias')
                return self.registra_novo_documento()

    def altera_documento(self):
        botao, documento_alterado = self.__tela_documento.alterar_qual_documento()
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
        for documento in self.__documento_DAO.get_all_documentos():
            if self.localiza_documento_pelo_nome(documento_alterado['nome']):
                # regra precisa ser a mesma que tem o documento_altera['nome']
                if documento_alterado['nome'] == documento['nome']:
                    botao, documento_novo = self.__tela_documento.alterar_documento(documento_alterado['nome'],
                                                                                    documento['regra'])
                    if botao == 'Voltar':
                        return self.abre_tela_cadastro_documentos()
                    if self.verifica_informacoes_preenchidas(documento_novo['nome'], documento_novo['regra']):
                        if self.localiza_documento_pelo_nome(documento_novo['nome']) and documento_novo['nome'] != \
                                documento_alterado['nome']:
                            self.__tela_documento.exibe_mensagem_erro('Já existe um documento com este nome')
                            return self.altera_documento()
                        else:
                            print(f'documento_novo', documento_novo['nome'])
                            print(f'documento', documento['nome'])
                            self.__documento_DAO.altera_documento(documento_novo['nome'], documento_novo['regra'],
                                                                  documento_alterado['nome'])
                            self.__tela_documento.exibe_mensagem_sucesso('Documento alterado com sucesso!')
                            return self.abre_tela_cadastro_documentos()
                    else:
                        self.__tela_documento.exibe_mensagem_erro('As informações não podem estar vazias')
                        return self.altera_documento()
            else:
                self.__tela_documento.exibe_mensagem_erro("Este documento NÃO consta no sistema!")
                return self.abre_tela_cadastro_documentos()

    def exclui_documento(self):
        botao, nome_documento = self.__tela_documento.excluir_documento()
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
        for documento in self.__documento_DAO.get_all_documentos():
            if self.localiza_documento_pelo_nome(nome_documento['nome']):
                # self.__consulado_tela.mostrar_msg("Este consulado consta no sistema! Podemos excluir!")
                self.__documento_DAO.remove_documento(nome_documento['nome'])
                self.__tela_documento.exibe_mensagem_sucesso('Documento removido com sucesso')
                return self.abre_tela_cadastro_documentos()
            else:
                self.__tela_documento.exibe_mensagem_erro("Este documento NÃO consta no sistema!")
                return self.abre_tela_cadastro_documentos()
