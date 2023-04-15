import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.layout_mostrar_menu_inicial()
        self.layout_logar_consul()
        self.layout_logar_gerente()
        self.layout_logar_agente()

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado precisa chamar
        # self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de
        # janelas depois de fechadas.
    def close(self):
        self.__window.Close()

    def mostrar_menu_inicial(self):
        self.layout_mostrar_menu_inicial()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        elif button == 'Voltar':
            opcao = 0
        self.close()
        return opcao

    def layout_mostrar_menu_inicial(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem Vindo ao Visaccess!', font=("Helvica", 25))],
            [sg.Text('Selecione com qual tipo de acesso você quer ingressar no sistema', font=("Helvica", 15))],
            [sg.Radio('Cônsul Geral', "RD13", key='1')],
            [sg.Radio('Gerente', "RD13", key='2')],
            [sg.Radio('Agente', "RD13", key='3')],
            [sg.Button('Confirmar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

    def logar(self, opcao_escolhida):
        if opcao_escolhida == 1:
            self.layout_logar_consul()
        elif opcao_escolhida == 2:
            self.layout_logar_gerente()
        elif opcao_escolhida == 3:
            self.layout_logar_agente()
        button, values = self.__window.Read()
        login = values['login']
        senha = values['senha']
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button == 'Voltar':
            self.close()
        self.close()
        return login, senha

    def layout_logar_consul(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem Vindo ao Visaccess, Cônsul!', font=("Helvica", 25))],
            [sg.Text('Digite seu cpf:', font=("Helvica", 15))],
            [sg.InputText('', key='login')],
            [sg.Text('Digite sua senha:', font=("Helvica", 15))],
            [sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

    def layout_logar_gerente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem Vindo ao Visaccess, Gerente!', font=("Helvica", 25))],
            [sg.Text('Digite seu cpf:', font=("Helvica", 15))],
            [sg.InputText('', key='login')],
            [sg.Text('Digite sua senha:', font=("Helvica", 15))],
            [sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

    def layout_logar_agente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem Vindo ao Visaccess, Agente!', font=("Helvica", 25))],
            [sg.Text('Digite seu cpf:', font=("Helvica", 15))],
            [sg.InputText('', key='login')],
            [sg.Text('Digite sua senha:', font=("Helvica", 15))],
            [sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

    def mostrar_msg(self, msg):
        sg.popup("", msg)
