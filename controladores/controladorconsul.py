from entidades.consul_geral import Consul
from entidades.documento import Documento
from excecoes.valueErrorException import ValueErrorException
from telas.telasistema import TelaSistema
from telas.telaconsul import TelaConsul
from controladores.controladorgerente import ControladorGerente
import sqlite3


class ControladorConsul:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__consul = Consul("Sung D. Ego", "1", "1")
        self.__documento = Documento()
        self.__tela_sistema = TelaSistema()
        self.__tela_consul = TelaConsul()
        self.__controlador_gerente = ControladorGerente(controlador_sistema)
        self.banco = sqlite3.connect('documentos_tipo_de_visto.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos_tipo_de_visto (
                nome TEXT NOT NULL,
                regra TEXT NOT NULL
        );
        """)


    def verificar_login_senha(self, cpf, senha):
        if isinstance(cpf, str) and isinstance(senha, str):
            if self.__consul.cpf == cpf and self.__consul.senha == senha:
                return True
            
    def abre_tela_cadastro_documentos(self):
        try:
            # usuario = self.__controlador_sistema.usuario_logado
            opcoes_documentos = {1: self.registra_novo_documento,
                                2: self.exclui_documento,
                                3: self.lista_documentos,
                                4: self.altera_documento,
                                0: self.abre_tela_inicial}
            while True:
                opcao_escolhida = self.__tela_consul.tela_documento_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = opcoes_documentos[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_consul.exibe_mensagem_erro()
            self.abre_tela_cadastro_documentos()

    def abre_tela_inicial(self):  # abre a tela consul pos login da tela do sistema
        try:
            mexer_consul_opcoes = {1: self.__controlador_sistema.controlador_consulado.abre_tela_consulados,
                                   2: self.__controlador_gerente.abrir_tela_cadastro_gerente,
                                   3: self.abre_tela_inicial,
                                   4: self.abre_tela_inicial,
                                   5: self.abre_tela_cadastro_documentos,
                                   6: self.abre_tela_inicial,
                                   0: self.__controlador_sistema.iniciar_tela_sistema
                                   }
            while True:
                opcao_escolhida = self.__tela_consul.tela_consul_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4\
                        and opcao_escolhida != 5 and opcao_escolhida != 6 and opcao_escolhida != 0:
                    raise ValueErrorException
                print(opcao_escolhida)
                funcao_escolhida = mexer_consul_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_sistema.mostrar_msg(e)
            self.abre_tela_inicial()

    def voltar(self):
        return self.abre_tela_inicial()
    
    #---------------- CADASTRO DE DOCUMENTOS ------------------
    
    def get_all_documentos(self):
        print('Entrou no get_all_documentos - controller')
        self.cursor.execute("SELECT * FROM documentos_tipo_de_visto")
        rows = self.cursor.fetchall()
        documentos = []
        for row in rows:
            documento = {'nome': row[0], 'regra': row[1]}
            documentos.append(documento)
        return documentos
        
    def lista_documentos(self):
        documentos = self.get_all_documentos()
        botao, values = self.__tela_consul.mostra_lista_documentos(documentos)
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
    
    def verifica_informacoes_preenchidas(self, nome: str, regra: str):
        if nome != "" and regra != "":
            print('dados do documento preenchidos')
            return True
        else:
            print('dados do documento NÃO preenchidos')
            return False
    
    def registra_novo_documento(self):
        print('entrou no registra_novo_documento')
        botao, dados_documento = self.__tela_consul.pegar_dados_documento()
        print(dados_documento)
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
        
        for documento in self.get_all_documentos():
            print(documento)
            if dados_documento['nome'] == documento['nome']:
                self.__tela_consul.exibe_mensagem_erro('Documento já consta no sistema')
                return self.registra_novo_documento()
            
        else:
            if self.verifica_informacoes_preenchidas(dados_documento['nome'], dados_documento['regra']):
                self.__documento.registra_documento(dados_documento['nome'], dados_documento['regra'])
                # self.__tela_consul.exibe_mensagem_sucesso('Documento Cadastrado com Sucesso!')
                return self.abre_tela_cadastro_documentos()
            else:
                self.__tela_consul.exibe_mensagem_erro('As informações não podem estar vazias')
                return self.registra_novo_documento()                
    

    def altera_documento(self):
        botao, documento_alterado = self.__tela_consul.alterar_qual_documento()
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
        for documento in self.get_all_documentos():
            if self.__documento.localiza_documento_pelo_nome(documento_alterado['nome']):
                # regra precisa ser a mesma que tem o documento_altera['nome']
                if documento_alterado['nome'] == documento['nome']:
                    botao, documento_novo = self.__tela_consul.alterar_documento(documento_alterado['nome'], documento['regra'])
                    if botao == 'Voltar':
                        return self.abre_tela_cadastro_documentos()
                    if self.verifica_informacoes_preenchidas(documento_novo['nome'], documento_novo['regra']):
                        if self.__documento.localiza_documento_pelo_nome(documento_novo['nome']) and documento_novo['nome'] != documento_alterado['nome']:
                            self.__tela_consul.exibe_mensagem_erro('Já existe um documento com este nome')
                            return self.altera_documento() 
                        else:
                            print(f'documento_novo', documento_novo['nome'])
                            print(f'documento', documento['nome'])
                            self.__documento.altera_documento(documento_novo['nome'], documento_novo['regra'], documento_alterado['nome'])
                            self.__tela_consul.exibe_mensagem_sucesso('Documento alterado com sucesso!')
                            return self.abre_tela_cadastro_documentos()
                    else:
                        self.__tela_consul.exibe_mensagem_erro('As informações não podem estar vazias')
                        return self.altera_documento()         
            else:
                self.__tela_consul.exibe_mensagem_erro("Este documento NÃO consta no sistema!")
                return self.abre_tela_cadastro_documentos()

        
    def exclui_documento(self):
        botao, nome_documento = self.__tela_consul.excluir_documento()
        if botao == 'Voltar':
            return self.abre_tela_cadastro_documentos()
        for documento in self.get_all_documentos():
            if self.__documento.localiza_documento_pelo_nome(nome_documento['nome']):
                # self.__consulado_tela.mostrar_msg("Este consulado consta no sistema! Podemos excluir!")
                self.__documento.remove_documento(nome_documento['nome'])
                self.__tela_consul.exibe_mensagem_sucesso('Documento removido com sucesso')
                return self.abre_tela_cadastro_documentos()
            else:
                self.__tela_consul.exibe_mensagem_erro("Este documento NÃO consta no sistema!")
                return self.abre_tela_cadastro_documentos()


