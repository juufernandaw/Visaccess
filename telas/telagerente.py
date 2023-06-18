import PySimpleGUI as interface_gerente

class TelaGerente:
    def __init__(self):
        self.__janela = None

    def close(self):
        self.__janela.Close()

    def mostra_mensagem(self, minterface_gerente):
        interface_gerente.popup(minterface_gerente)

    def mensagem(self, texto):
        return print(texto)

    # telas inicias do gerente:
    def componentes_tela_gerente_inicial(self):
        layout = [
            [interface_gerente.Text('Selecione o que deseja fazer', font=("Helvica", 25))],
            [interface_gerente.Radio('Cadastrar Solicitação de Visto', "componentes_tela_gerente_inicial", key='1')],
            [interface_gerente.Radio('Aprovar Solicitação de Visto', "componentes_tela_gerente_inicial", key='2')],
            [interface_gerente.Radio('Cadastrar Agentes', "componentes_tela_gerente_inicial", key='3')],
            [interface_gerente.Radio('Cadastrar Estrangeiros', "componentes_tela_gerente_inicial", key='4')],
            [interface_gerente.Radio('Emitir Relatório de Solicitações Aprovadas', "componentes_tela_gerente_inicial", key='5')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Tela Inicial do Gerente').Layout(layout)

    def tela_gerente_inicial(self):
        self.componentes_tela_gerente_inicial()
        button, values = self.__janela.Read()
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
        if button in (None, 'Voltar'):
            opcao = 0
        
        self.close()

        return opcao
    
    # --------------- CADASTRO DE GERENTE --------------- 
    def componentes_novo_gerente(self):
        interface_gerente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_gerente.Text('Novo Gerente', font=("Helvica", 15))],
            [interface_gerente.Text('Nome'), interface_gerente.Input(key='nome')],
            [interface_gerente.Text('CPF'), interface_gerente.Input(key='cpf')],
            [interface_gerente.Text('Senha'), interface_gerente.Input(key='senha')],
            [interface_gerente.Text('Consulado'), interface_gerente.Input(key='consulado')],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Novo Gerente').Layout(layout)
        
    def pegar_dados_gerente(self):
        self.componentes_novo_gerente()
        button, values = self.__janela.Read()
        self.close()
        return button, values


    def excluir_gerente(self):
        interface_gerente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_gerente.Text('Excluir Gerente', font=("Helvica", 15))],
            [interface_gerente.Text('CPF'), interface_gerente.Input(key='cpf')],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Excluir Gerente').Layout(layout)
        evento, valores = self.__janela.read()
        self.close()
        return evento, valores

    def listar_gerentes(self, lista_gerentes):
        layout = [
            [interface_gerente.Text('Listar Gerentes', font=("Helvica", 25))],
            [interface_gerente.Listbox(values=lista_gerentes, select_mode='extended', size=(30, 6))],
            [interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Lista de Gerentes').Layout(layout)
        
        while True:
            evento, valores = self.__janela.Read()
            if evento == interface_gerente.WIN_CLOSED():
                break
            if evento == 'Voltar':
                self.tela_cadastrar_gerente()

        self.close()

    def escolher_gerente_para_alterar(self):
        layout = [
            [interface_gerente.Text('Modificar dados do Gerente', font=("Helvica", 25))],
            [interface_gerente.Text('CPF'), interface_gerente.Input('', key="cpf")],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Alterar Gerente').Layout(layout)

        evento, valores = self.__janela.read()
        self.close()
        return evento, valores

    def alterar_gerente(self, gerente):
        layout = [
            [interface_gerente.Text('Modificar dados do Gerente', font=("Helvica", 25))],
            [interface_gerente.Text('CPF'), interface_gerente.Input(gerente['cpf'], key="cpf")],
            [interface_gerente.Text('Nome'), interface_gerente.Input(gerente['nome'], key='nome')],
            [interface_gerente.Text('Senha'), interface_gerente.Input(gerente['senha'], key='senha')],
            [interface_gerente.Text('Consulado'), interface_gerente.Input(gerente['consulado'], key='consulado')],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Alterar Gerente').Layout(layout)

        evento, valores = self.__janela.read()
        self.close()
        return evento, valores

    def tela_cadastrar_gerente(self):
        interface_gerente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_gerente.Text('Cadastro de Gerentes', font=("Helvica", 15))],
            [interface_gerente.Radio('Novo Gerente', "RD1", key='1')],
            [interface_gerente.Radio('Excluir Gerente', "RD1", key='2')],
            [interface_gerente.Radio('Listar Gerente', "RD1", key='3')],
            [interface_gerente.Radio('Alterar Gerente', "RD1", key='4')],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Consul').Layout(layout)

        # while True:
        #     eventos, valores = self.__janela.read()
        #     if eventos == interface_gerente.WIN_CLOSED():
        #         break
        #     if eventos == 'Voltar':
        #         self.layout_tela_aba_consul(self)
        #     if eventos == "OK":
        #         if valores['novo']:
        #             self.novo_gerente(self)
        #         if valores['excluir']:
        #             self.excluir_gerente(self)
        #         if valores['listar']:
        #             self.listar_gerentes(self)
        #         if valores['alterar']:
        #             self.alterar_gerente(self)
        
        # self.close()

    def tela_cadastro_gerentes(self):
        self.tela_cadastrar_gerente()
        evento, valores = self.__janela.Read()
        opcao = 0
        if valores['1']:
            opcao = 1
        if valores['2']:
            opcao = 2
        if valores['3']:
            opcao = 3
        if valores['4']:
            opcao = 4
        if evento in (None, 'Voltar'):
            opcao = 0
        
        self.close()

        return opcao

