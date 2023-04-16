import PySimpleGUI as interface_sistema

class TelaGerente:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        interface_sistema.popup(msg)

    def mensagem(self, texto):
        return print(texto)

    # telas inicias do gerente:
    def componentes_tela_gerente_inicial(self):
        layout = [
            [interface_sistema.Text('Selecione o que deseja fazer', font=("Helvica", 25))],
            [interface_sistema.Radio('Cadastrar Solicitação de Visto', "componentes_tela_gerente_inicial", key='1')],
            [interface_sistema.Radio('Aprovar Solicitação de Visto', "componentes_tela_gerente_inicial", key='2')],
            [interface_sistema.Radio('Cadastrar Agentes', "componentes_tela_gerente_inicial", key='3')],
            [interface_sistema.Radio('Cadastrar Estrangeiros', "componentes_tela_gerente_inicial", key='4')],
            [interface_sistema.Radio('Emitir Relatório de Solicitações Aprovadas', "componentes_tela_gerente_inicial", key='5')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Button('Voltar')]
        ]
        self.__window = interface_sistema.Window('Tela Inicial do Gerente').Layout(layout)

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
            [interface_sistema.Text('Cadastros de Agentes', font=("Helvica", 25))],
            [interface_sistema.Radio('Adicionar Agente', "componentes_tela_cadastro_agentes", key='1')],
            [interface_sistema.Radio('Excluir Agente', "componentes_tela_cadastro_agentes", key='2')],
            [interface_sistema.Radio('Listar Agentes', "componentes_tela_cadastro_agentes", key='3')],
            [interface_sistema.Radio('Modificar dados de Agente', "componentes_tela_cadastro_agentes", key='4')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Button('Voltar')]
        ]
        self.__window = interface_sistema.Window('Tela de Cadastro de Agente').Layout(layout)

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

    # tela para adicionar agente:
    def componentes_tela_adicionar_agentes(self):
        layout = [
            [interface_sistema.Text('Nome'), interface_sistema.InputText('')],
            [interface_sistema.Text('CPF'), interface_sistema.InputText('')],
            [interface_sistema.Text('Senha'), interface_sistema.InputText('')],
            [interface_sistema.Text('Consulado'), interface_sistema.InputText('')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Button('Voltar')]
        ]
        self.__window = interface_sistema.Window('Adicionar Agente').Layout(layout)

        # tela para excluir/modificar agente:
    def componentes_tela_excluir_modificar_agentes(self, tipo):
        layout = [
            [interface_sistema.Text('CPF'), interface_sistema.InputText('')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Button('Voltar')]
        ]
        self.__window = interface_sistema.Window(tipo).Layout(layout)
    
    # lógica para adicionar/excluir/modificar agentes
    def logica_tela_agentes(self):
        button, data = self.__window.Read()

        self.close()

        if button in (None, 'Voltar'):
            return None

        return data
    
    def tela_adicionar_agentes(self):
        self.componentes_tela_adicionar_agentes()
        return self.logica_tela_agentes()

    def tela_excluir_agentes(self):
        self.componentes_tela_excluir_modificar_agentes('Excluir Agente')
        return self.logica_tela_agentes()

    def tela_modificar_agentes(self):
        self.componentes_tela_excluir_modificar_agentes('Modificar Agente')
        return self.logica_tela_agentes()
