import PySimpleGUI as tela_documento_verificado


class TelaDocumentoVerificado:
    
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_msg(self, msg):
        tela_documento_verificado.popup_ok(msg)

    def tela_documento_verificado(self, lista_documentos: list):
        layout = [
            [tela_documento_verificado.Text('Selecione os documentos desejados:')],
        ]

        for documento in lista_documentos:
            layout.append([tela_documento_verificado.Checkbox(documento, key=documento)])
        layout.append([tela_documento_verificado.Button('Confirmar'), tela_documento_verificado.Cancel('Retornar')])
        self.__window = tela_documento_verificado.Window('Tela Documentos Verificados').Layout(layout)
        button, values = self.__window.Read()
        return values
