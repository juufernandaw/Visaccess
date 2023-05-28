import PySimpleGUI as sg


class TelaDocumento:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def componentes_cadastro_documentos(self):
        layout = [
            [sg.Text('Selecione o que deseja fazer:', font=("Helvica", 25))],
            [sg.Radio('Novo Documento', "componentes_cadastro_documentos", key='1')],
            [sg.Radio('Excluir Documento', "componentes_cadastro_documentos", key='2')],
            [sg.Radio('Listar Documentos', "componentes_cadastro_documentos", key='3')],
            [sg.Radio('Alterar Documento', "componentes_cadastro_documentos", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Tela de Cadastro de Documentos').Layout(layout)

    def tela_documento_inicial(self):
        self.componentes_cadastro_documentos()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if button in (None, 'Voltar'):
            opcao = 0

        self.close()

        return opcao

    def exibe_mensagem_erro(self, e):
        sg.ChangeLookAndFeel('DarkTeal4')
        sg.popup_ok(e)

    def exibe_mensagem_sucesso(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        sg.popup_ok(msg)

    def mostra_lista_documentos(self, lista_documentos):
        layout = [
            [sg.Text('Listar Documentos', font=("Helvica", 25))],
            [sg.Listbox(values=lista_documentos, select_mode='extended', size=(30, 6))],
            [sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Lista de Documentos para Tipos de Vistos').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def adicionar_documento(self):
        layout = [
            [sg.Text('Novo Documento', font=("Helvica", 25))],
            [sg.Text('Nome'), sg.InputText('', key="nome")],
            [sg.Text('Regra'), sg.InputText('', key="regra")],
            [sg.Button('OK'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Novo Documento').Layout(layout)

    def pegar_dados_documento(self):
        self.adicionar_documento()
        button, values = self.__window.Read()
        self.close()
        return button, values

    def excluir_documento(self):
        layout = [
            [sg.Text('Excluir Documento', font=("Helvica", 25))],
            [sg.Text('Nome'), sg.InputText('', key="nome")],
            [sg.Button('OK'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Excluir Documento').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def alterar_qual_documento(self):
        layout = [
            [sg.Text('Modificar Documento', font=("Helvica", 25))],
            [sg.Text('Nome'), sg.InputText('', key="nome")],
            [sg.Button('OK'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Escolher qual documento alterar').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def alterar_documento(self, documento: str, regra: str):
        layout = [
            [sg.Text('Modificar Documento', font=("Helvica", 25))],
            [sg.Text('Nome'), sg.InputText(documento, key="nome")],
            [sg.Text('Regra'), sg.InputText(regra, key="regra")],
            [sg.Button('OK'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Altere o documento').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values
