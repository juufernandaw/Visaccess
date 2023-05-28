import PySimpleGUI as tela_documento_verificado


class TelaDocumentoVerificado:
    
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_msg(self, msg):
        tela_documento_verificado.popup_ok(msg)

    def tela_documento_verificado(self, lista_documentos):
        # tela dos documentos verificados com checkbox para preencher ou não
        # layout = [
        #     [tela_documento_verificado.Text('Selecione o que deseja fazer:', font=("Helvica", 25))],
        #     [tela_documento_verificado.Radio('Novo consulado', "componentes_tela_documento_verificado_inicial", key='1')],
        #     [tela_documento_verificado.Radio('Excluir consulado', "componentes_tela_documento_verificado_inicial", key='2')],
        #     [tela_documento_verificado.Radio('Listar consulado', "componentes_tela_documento_verificado_inicial", key='3')],
        #     [tela_documento_verificado.Radio('Alterar consulado', "componentes_tela_documento_verificado_inicial", key='4')],
        #     [tela_documento_verificado.Button('Confirmar'), tela_documento_verificado.Button('Voltar')]
        # ]
        # self.__window = tela_documento_verificado.Window('Tela Documentos Verificados').Layout(layout)
        button, values = self.__window.Read()
        # iterar pelo dicionario values e popular os dicionarios com {nome: nome, id: id, preenchido}
        self.close()
        return values_preenchidos  # é uma lista de dicts