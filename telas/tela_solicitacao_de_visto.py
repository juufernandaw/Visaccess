import PySimpleGUI as tela_solicitacao_visto


class TelaSolicitacaoVisto:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_mtela_solicitacao_visto(self, mtela_solicitacao_visto):
        tela_solicitacao_visto.popup_ok(mtela_solicitacao_visto)

    # tela inicial de criar solicitacao de visto
    def componentes_tela_solicitacao_visto_inicial(self, lista_tipos_visto: list):
        global escolha_treino, id
        botoes_tipos_visto = []
        for id, tipo_visto in enumerate(lista_tipos_visto):
            botoes_tipos_visto.append([tela_solicitacao_visto.Radio(tipo_visto.nome, "RD1", key=tipo_visto.nome)])
        layout = [
            [tela_solicitacao_visto.Text("Selecione o tipo de visto e preencha a data e o passaporte.", font=("Helvica", 20))],
            botoes_tipos_visto,
            [tela_solicitacao_visto.Text('Data de validade'), tela_solicitacao_visto.InputText('', key="data")],
            [tela_solicitacao_visto.Text('Passaporte'), tela_solicitacao_visto.InputText('', key="passaporte")],
            [tela_solicitacao_visto.Button('Confirmar'), tela_solicitacao_visto.Cancel('Retornar')]
        ]
        self.__window = tela_solicitacao_visto.Window("Cria solicitacao de visto").Layout(layout)
        button, values = self.__window.Read()

        escolha_tipo_visto = values[id]
        if button in (None, 'Retornar'):
            self.close()
        self.close()
        return escolha_tipo_visto
