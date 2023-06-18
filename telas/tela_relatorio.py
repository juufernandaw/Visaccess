import PySimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        self.__janela = None

    def close(self):
        self.__janela.Close()

    def mostra_mensagem(self, texto):
        sg.popup(texto)

    def mensagem(self, texto):
        return print(texto)

    # --------------- EMISSÃO DE RELATÓRIO --------------- 
    def tela_emissao_relatorio(self):
        layout = [
            [sg.Text('Qual relatório você gostaria de emitir?', font=("Helvica", 25))],
            [sg.Radio('Países com mais vistos aprovados', "componentes_tela_gerente_inicial", key='1')],
            [sg.Radio('Tipos de visto mais expedidos', "componentes_tela_gerente_inicial", key='2')],
            [sg.Button('OK'), sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Tela Emissão de Relatório').Layout(layout)

    def emissao_relatorios(self):
        self.tela_emissao_relatorio()
        evento, valores = self.__janela.Read()
        opcao = 0
        if valores['1']:
            opcao = 1
        if valores['2']:
            opcao = 2
        if evento in (None, 'Voltar'):
            opcao = 0
        
        self.close()

        return opcao
    
    def relatorio_paises(self, lista_relatorios):
        header = ['país', 'qtde_vistos']
        layout = [
            [sg.Text('Relatório', font=("Helvica", 25))],
            [sg.Text("Ranking de Países com Mais Vistos Aprovados", font=("Helvica", 25))],
            [sg.Table(values=lista_relatorios, headings=header, auto_size_columns=True,
                display_row_numbers=False,
                justification='center', key='-TABLE-',
                selected_row_colors='red on yellow',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                enable_click_events=False,
                header_text_color='purple')],
            [sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Relatórios').Layout(layout)
        evento, valores = self.__janela.Read()

        self.close()
        return evento, valores
    
    def relatorio_tipos_de_visto(self, lista_relatorios):
        header = ['Visto', 'Nº de Solicitações']
        layout = [
            [sg.Text('Relatório', font=("Helvica", 25))],
            [sg.Text("Ranking de Tipos de Visto Mais Solicitados", font=("Helvica", 25))],
            [sg.Table(values=lista_relatorios, headings=header, auto_size_columns=True,
                display_row_numbers=False,
                justification='center', key='-TABLE-',
                selected_row_colors='red on yellow',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                enable_click_events=False,
                header_text_color='purple')],
            [sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Relatórios').Layout(layout)
        evento, valores = self.__janela.Read()

        self.close()
        return evento, valores