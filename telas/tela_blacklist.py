import PySimpleGUI as tela_blacklist


class TelaBlacklist:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_msg(self, msg):
        tela_blacklist.popup_ok(msg)

    def componentes_tela_blacklist_inicial(self):
        layout = [
            [tela_blacklist.Text('Selecione o que deseja fazer:', font=("Helvica", 25))],
            [tela_blacklist.Radio('Adicionar', "componentes_tela_blacklist_inicial", key='1')],
            [tela_blacklist.Radio('Listar', "componentes_tela_blacklist_inicial", key='2')],
            [tela_blacklist.Radio('Excluir blacklist', "componentes_tela_blacklist_inicial", key='3')],
            [tela_blacklist.Button('Confirmar'), tela_blacklist.Button('Voltar')]
        ]
        self.__window = tela_blacklist.Window('Tela Blacklist').Layout(layout)

    def tela_blacklist_inicial(self):
        self.componentes_tela_blacklist_inicial()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if button in (None, 'Voltar'):
            opcao = 0

        self.close()
        return opcao

    def componentes_tela_adicionar_blacklist(self):
        layout = [
            [tela_blacklist.Text('Adicionar Blacklist', font=("Helvica", 25))],
            [tela_blacklist.Text('Nome'), tela_blacklist.InputText('', key="nome")],
            [tela_blacklist.Text('Passaporte'), tela_blacklist.InputText('', key="passaporte")],
            [tela_blacklist.Button('OK'), tela_blacklist.Button('Voltar')]
        ]
        self.__window = tela_blacklist.Window('Adicionar Blacklist').Layout(layout)

    def componentes_tela_excluir_blacklist(self):
        layout = [
            [tela_blacklist.Text('Excluir da blacklist', font=("Helvica", 25))],
            [tela_blacklist.Text('Passaporte'), tela_blacklist.InputText('', key="passaporte")],
            [tela_blacklist.Button('OK'), tela_blacklist.Button('Voltar')]
        ]
        self.__window = tela_blacklist.Window('Excluir blacklist').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def componentes_tela_listar_blacklist(self, lista_blacklist):
        layout = [
            [tela_blacklist.Text('Lista de blacklists', font=("Helvica", 25))],
            [tela_blacklist.Listbox(values=lista_blacklist, select_mode='extended', size=(30, 6))],
            [tela_blacklist.Button('Voltar')]
        ]
        self.__window = tela_blacklist.Window('Lista de blacklists').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def pegar_dados_blacklist(self):
        self.componentes_tela_adicionar_blacklist()
        button, values = self.__window.Read()
        nome = values['nome']
        passaporte = values['passaporte']
        self.close()
        return button, nome, passaporte
