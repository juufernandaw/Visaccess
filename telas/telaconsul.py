import PySimpleGUI as sg
from telas.telagerente import TelaGerente


class TelaConsul:
    def __init__(self):
        self.__window = None
        self.layout_tela_aba_consul()

    def close(self):
        self.__window.Close()

    def layout_tela_aba_consul(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("----- Consul -----", font=("Helvica", 20))],
            [sg.Text('Selecione o que deseja fazer', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Consulados', "RD1", key='1')],
            [sg.Radio('Cadastrar Gerentes', "RD1", key='2')],
            [sg.Radio('Cadastrar Países', "RD1", key='3')],
            [sg.Radio('Cadastrar Blacklist', "RD1", key='4')],
            [sg.Radio('Cadastrar Documentos', "RD1", key='5')],
            [sg.Radio('Cadastrar Tipos de Visto', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Consul').Layout(layout)

    def tela_consul_inicial(self):
        self.layout_tela_aba_consul()
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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if button == 'Voltar':
            opcao = 0
        self.close()
        return opcao
    
    