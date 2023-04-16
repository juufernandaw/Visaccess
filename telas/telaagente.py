import PySimpleGUI as sg


class TelaAgente:
    def __init__(self):
        self.__window = None
        self.layout_tela_aba_agente()

    def close(self):
        self.__window.Close()

    def layout_tela_aba_agente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("----- Agente -----", font=("Helvica", 20))],
            [sg.Text('Selecione o que deseja fazer', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Solicitação de Visto', "RD1", key='1')],
            [sg.Radio('Cadastrar Estrangeiros', "RD1", key='2')],
            [sg.Button('Confirmar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Agente').Layout(layout)

    def tela_agente_inicial(self):
        self.layout_tela_aba_consul()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif button == 'Sair':
            opcao = 0
        self.close()
        return opcao