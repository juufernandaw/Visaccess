import PySimpleGUI as tela_solicitacao_visto
from datetime import datetime


class TelaSolicitacaoVisto:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_msg_tela(self, mtela_solicitacao_visto):
        tela_solicitacao_visto.popup_ok(mtela_solicitacao_visto)

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
            [tela_solicitacao_visto.Button('Confirmar')]
        ]
        self.__window = tela_solicitacao_visto.Window("Cria solicitacao de visto").Layout(layout)
        button, values = self.__window.Read()

        error = False
        if values["data"] == "" or values["passaporte"] == "" or True not in values.values():
            error = True
            msg_erro = "É necessário preencher todos os campos"

        if not error:
            data = values["data"]

            data_dt_time = datetime.strptime(data, '%Y-%m-%d')
            if data_dt_time < datetime.now():
                error = True
                msg_erro = "Data inválida. A data precisa ser mais futura que a data atual."

        if error:
            self.mostrar_msg_tela(msg_erro)
            self.tela_solicitacao_visto_inicial(lista_tipos_visto=lista_tipos_visto)
        else:
            data = values["data"]
            for k, v in values.items():
                if v:
                    escolha_tipo_visto = k
                    break
            passaporte = values["passaporte"]
            return escolha_tipo_visto, passaporte, data
    
    def tela_selecionar_visto_aprovar(self, lista_solicitacoes_visto: list):
        botoes_solicitacoes_visto = []
        for solicitacoes in lista_solicitacoes_visto:
            botoes_solicitacoes_visto.append([tela_solicitacao_visto.Radio(solicitacoes["estrangeiro"], "RD1", key=solicitacoes["estrangeiro"])])
        layout = [
            [tela_solicitacao_visto.Text("Selecione o tipo de visto e preencha a data e o passaporte.", font=("Helvica", 20))],
            botoes_solicitacoes_visto,
            [tela_solicitacao_visto.Button('Confirmar'), tela_solicitacao_visto.Button('Voltar')]
        ]

        self.__window = tela_solicitacao_visto.Window("Aprova solicitacão de visto").Layout(layout)
        button, data = self.__window.Read()

        self.close()

        if button in (None, 'Voltar'):

            return None

        for solicitacao in data:
            selected = data[solicitacao]

            if selected == True:
                return solicitacao

    def tela_aprovar_visto(self, estrangeiro_solicitando, lista_documentos: list, lista_documentos_necessarios_visto: list):
        if estrangeiro_solicitando['trabalho'] == 0:
            estrangeiro_solicitando['trabalho'] = 'Não'
        else:
            estrangeiro_solicitando['trabalho'] = 'Sim'

        layout = [
            [tela_solicitacao_visto.Text('Informações do Estrangeiro:')],
            [tela_solicitacao_visto.Text('Passaporte:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['passaporte'])],
            [tela_solicitacao_visto.Text('Nome:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['nome'])],
            [tela_solicitacao_visto.Text('Data de Nascimento (dd/mm/aaaa):'), tela_solicitacao_visto.Text(estrangeiro_solicitando['data_nasc'])],
            [tela_solicitacao_visto.Text('Estado civil:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['estado_civil'])],
            [tela_solicitacao_visto.Text('País:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['pais'])],
            [tela_solicitacao_visto.Text('Estado:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['estado'])],
            [tela_solicitacao_visto.Text('Cidade:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['cidade'])],
            [tela_solicitacao_visto.Text('Trabalho:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['trabalho'])],
            [tela_solicitacao_visto.Text('Profissão:'), tela_solicitacao_visto.Text(estrangeiro_solicitando['profissao'])],
            [tela_solicitacao_visto.Text('')],
            [tela_solicitacao_visto.Text('Documentação:')],
        ]

        for documento in lista_documentos_necessarios_visto:
            if documento in lista_documentos:
                layout.append([tela_solicitacao_visto.Checkbox(documento, key=documento, default=True)])
            else:
                layout.append([tela_solicitacao_visto.Checkbox(documento, key=documento, default=False)])
        layout.append([tela_solicitacao_visto.Button('Aprovar'), tela_solicitacao_visto.Button('Reprovar')])
        self.__window = tela_solicitacao_visto.Window("Aprovação de Vistos").Layout(layout)
        button, data = self.__window.Read()

        self.close()

        if button in ('Reprovar'):
            return False
        else:
            return True
