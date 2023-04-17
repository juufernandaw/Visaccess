import PySimpleGUI as interface_gerente

class TelaGerente:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        interface_gerente.popup(msg)

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
        self.__window = interface_gerente.Window('Tela Inicial do Gerente').Layout(layout)

    def tela_gerente_inicial(self):
        self.componentes_tela_gerente_inicial()
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
        if button in (None, 'Voltar'):
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
        self.__window = interface_gerente.Window('Tela de Cadastro de Agente').Layout(layout)

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
            [interface_gerente.Text('Nome'), interface_gerente.InputText('')],
            [interface_gerente.Text('CPF'), interface_gerente.InputText('')],
            [interface_gerente.Text('Senha'), interface_gerente.InputText('')],
            [interface_gerente.Text('Consulado'), interface_gerente.InputText('')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__window = interface_gerente.Window(tipo).Layout(layout)
    
    # tela para excluir/modificar agente:
    def componentes_tela_excluir_modificar_agentes(self, tipo):
        layout = [
            [interface_gerente.Text('CPF'), interface_gerente.InputText('')],
            [interface_gerente.Button('Confirmar'), interface_gerente.Button('Voltar')]
        ]
        self.__window = interface_gerente.Window(tipo).Layout(layout)
    
    def componentes_tela_listar_agentes(self, lista_agentes):
        layout = [
            [interface_gerente.Text('Lista de Agentes', font=("Helvica", 25))],
            [interface_gerente.Listbox(values=lista_agentes, select_mode='extended', size=(30, 6))],
            [interface_gerente.Button('Voltar')]
        ]
        self.__window = interface_gerente.Window('Lista de Agentes').Layout(layout)
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
