import PySimpleGUI as tela_solicitacao_visto


class TelaSolicitacaoVisto:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_mtela_solicitacao_visto(self, mtela_solicitacao_visto):
        tela_solicitacao_visto.popup_ok(mtela_solicitacao_visto)

    # tela inicial de criar solicitacao de visto
    def tela_solicitacao_visto_inicial(self, lista_tipos_visto: list):
        global id
        botoes_tipos_visto = []
        for id, tipo_visto in enumerate(lista_tipos_visto):
            botoes_tipos_visto.append([tela_solicitacao_visto.Radio(tipo_visto["nome"], "RD1", key=tipo_visto["nome"])])
        layout = [
            [tela_solicitacao_visto.Text("Selecione o tipo de visto e preencha a data e o passaporte.", font=("Helvica", 20))],
            botoes_tipos_visto,
            [tela_solicitacao_visto.Input(key='data', enable_events=False, readonly=True),
             tela_solicitacao_visto.CalendarButton('Choose', target='data', format='%Y-%m-%d')],
            [tela_solicitacao_visto.Text('Passaporte'), tela_solicitacao_visto.InputText('', key="passaporte")],
            [tela_solicitacao_visto.Button('Confirmar'), tela_solicitacao_visto.Cancel('Retornar')]
        ]
        self.__window = tela_solicitacao_visto.Window("Cria solicitacao de visto").Layout(layout)
        button, values = self.__window.Read()

        algum_erro = False
        # validar se a data é valida (formato date e data > q a data atual)
        # validar se algum campo não está preenchido
        # se sim algum_erro = True
        msg_erro = "" # especifica p cada erro
        if algum_erro:
            self.mostrar_mtela_solicitacao_visto(msg_erro)
            self.tela_solicitacao_visto_inicial(lista_tipos_visto=lista_tipos_visto)
        else:
            escolha_tipo_visto = list(values.keys())[0]
            data = values["data"]
            passaporte = values["passaporte"]
            if button in (None, 'Retornar'):
                self.close()
            return escolha_tipo_visto, passaporte, data
