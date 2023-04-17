import PySimpleGUI as tela_consulado


class TelaConsulado:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_msg(self, msg):
        # tela_consulado.popup(msg)
        return print(msg)

    def mensagem(self, texto):
        return print(texto)

    def componentes_tela_consulado_inicial(self):
        layout = [
            [tela_consulado.Text('Selecione o que deseja fazer:', font=("Helvica", 25))],
            [tela_consulado.Radio('Novo consulado', "componentes_tela_consulado_inicial", key='1')],
            [tela_consulado.Radio('Excluir consulado', "componentes_tela_consulado_inicial", key='2')],
            [tela_consulado.Radio('Listar consulado', "componentes_tela_consulado_inicial", key='3')],
            [tela_consulado.Radio('Alterar consulado', "componentes_tela_consulado_inicial", key='4')],
            [tela_consulado.Button('Confirmar'), tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Tela Consulados').Layout(layout)

    def tela_consulado_inicial(self):
        self.componentes_tela_consulado_inicial()
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

    def componentes_tela_adicionar_consulado(self):
        layout = [
            [tela_consulado.Text('Novo consulado', font=("Helvica", 25))],
            [tela_consulado.Text('Sede'), tela_consulado.InputText('', key="sede")],
            [tela_consulado.Button('OK'), tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Adicionar Consulado').Layout(layout)

    def componentes_tela_alterar_consulado(self, consulado):
        layout = [
            [tela_consulado.Text('Alterar consulado', font=("Helvica", 25))],
            [tela_consulado.Text('Sede'), tela_consulado.InputText(consulado.sede, key="sede")],
            [tela_consulado.Button('OK'), tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Alterar Consulado').Layout(layout)

    def componentes_tela_excluir_consulado(self):
        layout = [
            [tela_consulado.Text('Excluir consulado', font=("Helvica", 25))],
            [tela_consulado.Text('Sede'), tela_consulado.InputText('', key="sede")],
            [tela_consulado.Button('OK'), tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Excluir Consulado').Layout(layout)

    def componentes_tela_alterar_qual_consulado(self):
        layout = [
            [tela_consulado.Text('Qual consulado você quer alterar?', font=("Helvica", 25))],
            [tela_consulado.Text('Sede'), tela_consulado.InputText('', key="sede")],
            [tela_consulado.Button('OK'), tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Escolher qual Consulado alterar').Layout(layout)

    def componentes_tela_listar_consulados(self, lista_consulados):
        layout = [
            [tela_consulado.Text('Lista de Consulados', font=("Helvica", 25))],
            [tela_consulado.Listbox(values=lista_consulados, select_mode='extended', size=(30, 6))],
            [tela_consulado.Button('Voltar')]
        ]
        self.__window = tela_consulado.Window('Lista de Consulados').Layout(layout)
        button, values = self.__window.Read()
        self.close()

    def pegar_dados_consulado(self):
        self.componentes_tela_adicionar_consulado()
        button, values = self.__window.Read()
        sede = values['sede']
        self.close()
        return sede
