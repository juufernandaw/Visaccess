from entidades.tipo_de_visto import TipoDeVisto
from telas.tela_tipos_visto import TelaTipoVisto
from persistencia.tipos_vistoDAO import Tipos_VistoDAO


class ControladorTiposVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipos_vistos = TelaTipoVisto()
        self.__tipos_vistoDAO = Tipos_VistoDAO()

    # PROPERTY:
    @property
    def tela_tipos_vistos(self):
        return self.__tela_tipos_vistos

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def get_tipos_vistoDAO(self):
        return self.__tipos_vistoDAO

    # ABRIR TELA PRINCIPAL:

    def abrir_tela_cadastro(self):
        while True:
            opcao = self.tela_tipos_vistos.tela_cadastro_tipos_visto()
            if opcao == 1:
                self.novo_tipos_visto()
            elif opcao == 2:
                self.excluir_tipos_visto()
            elif opcao == 3:
                self.listar_tipos_visto()
            elif opcao == 4:
                self.modificar_tipos_visto()
            elif opcao == 0 or opcao == None:
                self.controlador_sistema.get_controlador_consul.abre_tela_inicial()

    def novo_tipos_visto(self):
        docs = self.controlador_sistema.get_controlador_documento.documento_DAO.get_all_documentos()
        data = self.tela_tipos_vistos.tela_adicionar_tipos_visto(docs)
        try:
            data[1] = int(data[1])
        except:
            data[1] = ''

        if data != None:
            if data[0] and data[1] != '' and data[1] and data['-DOCUMENTOS-'] != []:
                check = self.get_tipos_vistoDAO.buscar_visto_por_nome(data[0])
                if check != None:
                    self.tela_tipos_vistos.mostra_mensagem('Já há um tipo de visto com esse nome!')
                else:
                    tipo_visto = TipoDeVisto(data[0], data[1], data['-DOCUMENTOS-'])
                    self.get_tipos_vistoDAO.cadastrar_tipos_visto(data[0], data[1])
                    self.get_tipos_vistoDAO.cadastrar_documentos_para_visto(data['-DOCUMENTOS-'], data[0])
                    self.tela_tipos_vistos.mostra_mensagem('Tipo de visto criado com sucesso!')
            else:
                self.tela_tipos_vistos.mostra_mensagem('Todos os Campos devem ser preenchidos corretamente')

    def excluir_tipos_visto(self):
        visto_nome = self.tela_tipos_vistos.tela_excluir_tipos_visto()
        if visto_nome != None:
            visto = self.get_tipos_vistoDAO.buscar_visto_por_nome(visto_nome[0])
            if visto != None:
                self.get_tipos_vistoDAO.excluir_visto(visto_nome[0])
                self.get_tipos_vistoDAO.excluir_relacao_visto_documento(visto_nome[0])
                self.tela_tipos_vistos.mostra_mensagem('Tipo de visto excluído com sucesso!')
                return self.abrir_tela_cadastro()
            else:
                self.tela_tipos_vistos.mostra_mensagem('Tipo de visto não consta no sistema!')

    def listar_tipos_visto(self):
        tipos_visto = self.get_tipos_vistoDAO.buscar_todos_tipos_visto()
        self.tela_tipos_vistos.componentes_tela_listar_tipos_visto(tipos_visto)

    def modificar_tipos_visto(self):
        visa_nome = self.tela_tipos_vistos.tela_modificar_tipos_visto()

        if visa_nome != None:
            docs = self.controlador_sistema.get_controlador_documento.documento_DAO.get_all_documentos()
            visa = self.get_tipos_vistoDAO.buscar_visto_por_nome(visa_nome[0])
            if visa != None:
                dados_novos = self.tela_tipos_vistos.tela_atualizar_tipos_visto(docs)
                try:
                    dados_novos[1] = int(dados_novos[1])
                except:
                    dados_novos[1] = ''

                if dados_novos != None:
                    if dados_novos[0] and dados_novos[1] != '' and dados_novos['-DOCUMENTOS-'] != []:
                        teste = self.get_tipos_vistoDAO.buscar_visto_por_nome(dados_novos[0])
                        if teste == None or teste['nome'] == dados_novos[0]:
                            self.get_tipos_vistoDAO.atualizar_visto(
                                visa['nome'],
                                dados_novos[0],
                                dados_novos[1],
                            )
                            self.get_tipos_vistoDAO.excluir_relacao_visto_documento(visa_nome[0])
                            self.get_tipos_vistoDAO.cadastrar_documentos_para_visto(dados_novos['-DOCUMENTOS-'],
                                                                                dados_novos[0])

                            self.tela_tipos_vistos.mostra_mensagem('Tipo de Visto alterado com sucesso!')
                            return self.abrir_tela_cadastro()
                        else:
                            self.tela_tipos_vistos.mostra_mensagem('Tipo de visto já existe nos registros')
                            return self.abrir_tela_cadastro()
                    else:
                        self.tela_tipos_vistos.mostra_mensagem('Campos preenchidos incorretamente!')
                        return self.abrir_tela_cadastro()
            else:
                self.tela_tipos_vistos.mostra_mensagem('Este Tipo de Visto não consta no sistema')
