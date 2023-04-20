import PySimpleGUI as interface_agente

class TelaAgente:
    def __init__(self):
        self.__window = None
        self.layout_tela_aba_agente()

    def close(self):
        self.__window.Close()
    
    def mostra_mensagem(self, minterface_agente):
        interface_agente.popup(minterface_agente)

# TELAS CADASTRO DE AGENTE(CRUD) ABAIXO -----------------------

    def componentes_tela_cadastro_agentes(self):
        layout = [
            [interface_agente.Text('Cadastros de Agentes', font=("Helvica", 25))],
            [interface_agente.Radio('Adicionar Agente', "componentes_tela_cadastro_agentes", key='1')],
            [interface_agente.Radio('Excluir Agente', "componentes_tela_cadastro_agentes", key='2')],
            [interface_agente.Radio('Listar Agentes', "componentes_tela_cadastro_agentes", key='3')],
            [interface_agente.Radio('Modificar dados de Agente', "componentes_tela_cadastro_agentes", key='4')],
            [interface_agente.Button('Confirmar'), interface_agente.Button('Voltar')]
        ]
        self.__window = interface_agente.Window('Tela de Cadastro de Agente').Layout(layout)

    def tela_cadastro_agentes(self):
        self.componentes_tela_cadastro_agentes()
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
        if button in (None, 'Voltar'):
            opcao = 0
        
        self.close()

        return opcao

    # tela para adicionar/atualizar agente:
    def componentes_tela_adicionar_atualizar_agentes(self, tipo):
        layout = [
            [interface_agente.Text('Nome'), interface_agente.InputText('')],
            [interface_agente.Text('CPF'), interface_agente.InputText('')],
            [interface_agente.Text('Senha'), interface_agente.InputText('')],
            [interface_agente.Text('Consulado'), interface_agente.InputText('')],
            [interface_agente.Button('Confirmar'), interface_agente.Button('Voltar')]
        ]
        self.__window = interface_agente.Window(tipo).Layout(layout)
    
    # tela para excluir/modificar agente:
    def componentes_tela_excluir_modificar_agentes(self, tipo):
        layout = [
            [interface_agente.Text('CPF'), interface_agente.InputText('')],
            [interface_agente.Button('Confirmar'), interface_agente.Button('Voltar')]
        ]
        self.__window = interface_agente.Window(tipo).Layout(layout)
    
    def componentes_tela_listar_agentes(self, lista_agentes):
        layout = [
            [interface_agente.Text('Lista de Agentes', font=("Helvica", 25))],
            [interface_agente.Listbox(values=lista_agentes, select_mode='extended', size=(30, 6))],
            [interface_agente.Button('Voltar')]
        ]
        self.__window = interface_agente.Window('Lista de Agentes').Layout(layout)
        button, values = self.__window.Read()
        self.close()
    
    # lógica para adicionar/excluir/modificar agentes
    def logica_tela_agentes(self):
        button, data = self.__window.Read()

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


# TELAS CADASTRO DE AGENTE(CRUD) ACIMA -----------------------


    def layout_tela_aba_agente(self):
        interface_agente.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [interface_agente.Text("----- Agente -----", font=("Helvica", 20))],
            [interface_agente.Text('Selecione o que deseja fazer', font=("Helvica", 15))],
            [interface_agente.Radio('Cadastrar Solicitação de Visto', "RD1", key='1')],
            [interface_agente.Radio('Cadastrar Estrangeiros', "RD1", key='2')],
            [interface_agente.Button('Confirmar'), interface_agente.Button('Sair')]
        ]
        self.__window = interface_agente.Window('Agente').Layout(layout)

    def tela_agente_inicial(self):
        self.layout_tela_aba_agente()
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