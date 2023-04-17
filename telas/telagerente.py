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
    def novo_gerente(self):
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
        
        while True:
            evento, valores = self.__janela.read()
            if evento == interface_gerente.WIN_CLOSED():
                break
            if evento == 'Voltar':
                self.tela_cadastrar_gerente()
            if evento == "OK":
                return valores


    def excluir_gerente(self):
        interface_gerente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_gerente.Text('Excluir Gerente', font=("Helvica", 15))],
            [interface_gerente.Text('CPF'), interface_gerente.Input(key='cpf')],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Excluir Gerente').Layout(layout)
        while True:
            evento, valores = self.__janela.read()
            if evento == interface_gerente.WIN_CLOSED():
                break
            if evento == 'Voltar':
                self.tela_cadastrar_gerente()
            if evento == "OK":
                return valores

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
            [interface_gerente.Text('CPF'), interface_gerente.InputText('', key="cpf")],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Alterar Gerente').Layout(layout)

        while True:
            evento, valores = self.__janela.read()
            if evento == interface_gerente.WIN_CLOSED():
                break
            if evento == 'Voltar':
                self.tela_cadastrar_gerente()
            if evento == "OK":
                return valores
        
        self.close()

    def alterar_agente(self, gerente):
        layout = [
            [interface_gerente.Text('Modificar dados do Gerente', font=("Helvica", 25))],
            [interface_gerente.Text('CPF'), interface_gerente.InputText(gerente, key="cpf")],
            [interface_gerente.Button('OK'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Alterar Gerente').Layout(layout)

        while True:
            evento, valores = self.__janela.read()
            if evento == interface_gerente.WIN_CLOSED():
                break
            if evento == 'Voltar':
                self.tela_cadastrar_gerente()
            if evento == "OK":
                return valores
        
        self.close()

    def tela_cadastrar_gerente(self):
        interface_gerente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_gerente.Text('Cadastro de Gerentes', font=("Helvica", 15))],
            [interface_gerente.Radio('Novo Gerente', "RD1", key='novo')],
            [interface_gerente.Radio('Excluir Gerente', "RD1", key='excluir')],
            [interface_gerente.Radio('Listar Gerente', "RD1", key='listar')],
            [interface_gerente.Radio('Alterar Gerente', "RD1", key='alterar')],
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
    
    # tela inicial do cadastro de agente:
    def componentes_tela_cadastro_agentes(self):
        layout = [
            [interface_gerente.Text('Cadastros de Agentes', font=("Helvica", 25))],
            [interface_gerente.Radio('Adicionar Agente', "componentes_tela_cadastro_agentes", key='1')],
            [interface_gerente.Radio('Excluir Agente', "componentes_tela_cadastro_agentes", key='2')],
            [interface_gerente.Radio('Listar Agentes', "componentes_tela_cadastro_agentes", key='3')],
            [interface_gerente.Radio('Modificar dados de Agente', "componentes_tela_cadastro_agentes", key='4')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Tela de Cadastro de Agente').Layout(layout)

    def tela_cadastro_agentes(self):
        self.componentes_tela_cadastro_agentes()
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
        if button in (None, 'Voltar'):
            opcao = 0
        
        self.close()

        return opcao

    # tela para adicionar/atualizar agente:
    def componentes_tela_adicionar_atualizar_agentes(self, tipo):
        layout = [
            [interface_gerente.Text('Nome'), interface_gerente.InputText('')],
            [interface_gerente.Text('CPF'), interface_gerente.InputText('')],
            [interface_gerente.Text('Senha'), interface_gerente.InputText('')],
            [interface_gerente.Text('Consulado'), interface_gerente.InputText('')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window(tipo).Layout(layout)
    
    # tela para excluir/modificar agente:
    def componentes_tela_excluir_modificar_agentes(self, tipo):
        layout = [
            [interface_gerente.Text('CPF'), interface_gerente.InputText('')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window(tipo).Layout(layout)
    
    def componentes_tela_listar_agentes(self, lista_agentes):
        layout = [
            [interface_gerente.Text('Lista de Agentes', font=("Helvica", 25))],
            [interface_gerente.Listbox(values=lista_agentes, select_mode='extended', size=(30, 6))],
            [interface_gerente.Button('Voltar')]
        ]
        self.__janela = interface_gerente.Window('Lista de Agentes').Layout(layout)
        button, values = self.__janela.Read()
        self.close()
    
    # lógica para adicionar/excluir/modificar agentes
    def logica_tela_agentes(self):
        button, data = self.__janela.Read()

        self.close()

        if button in (None, 'Voltar'):
            return None

        return data
    
    def tela_adicionar_agentes(self):
        self.componentes_tela_adicionar_atualizar_agentes('Adicionar Agente')
        return self.logica_tela_agentes()

    def tela_excluir_agentes(self):
        self.componentes_tela_excluir_modificar_agentes('Excluir Agente')
        return self.logica_tela_agentes()

    def tela_modificar_agentes(self):
        self.componentes_tela_excluir_modificar_agentes('Modificar Agente')
        return self.logica_tela_agentes()
    
    def tela_atualizar_agentes(self):
        self.componentes_tela_adicionar_atualizar_agentes('Atualizar Agente')
        return self.logica_tela_agentes()
