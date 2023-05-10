import PySimpleGUI as interface_tela_tipos_visto

class TelaTipoVisto:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, interface_tela_tipos_visto):
        interface_tela_tipos_visto.popup(interface_tela_tipos_visto)

# TELAS:

    # TELA INICIAL DE CADASTRAR TIPOS DE VISTO:

    def componentes_tela_cadastro_tipos_visto(self):
        layout = [
            [interface_tela_tipos_visto.Text('Tipos de Visto', font=("Helvica", 25))],
            [interface_tela_tipos_visto.Radio('Novo Tipo de Visto', "componentes_tela_cadastro_tipos_visto", key='1')],
            [interface_tela_tipos_visto.Radio('Excluir Tipo de Visto', "componentes_tela_cadastro_tipos_visto", key='2')],
            [interface_tela_tipos_visto.Radio('Listar Tipos de Visto', "componentes_tela_cadastro_tipos_visto", key='3')],
            [interface_tela_tipos_visto.Radio('Modificar Tipo de Visto', "componentes_tela_cadastro_tipos_visto", key='4')],
            [interface_tela_tipos_visto.Button('Confirmar'), interface_tela_tipos_visto.Button('Voltar')]
        ]
        self.__window = interface_tela_tipos_visto.Window('Cadastro de Tipos de Visto').Layout(layout)

    def tela_cadastro_tipos_visto(self):
        self.componentes_tela_cadastro_tipos_visto()
        button, values = self.__window.Read()
        opcao = None
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if button in (None, 'Voltar'):
            self.close()
            return None
        
        self.close()

        return opcao
    
    # TELAS SECUNDÁRIAS:

    # tela para adicionar/atualizar tipos de visto:
    def componentes_tela_adicionar_atualizar_tipos_visto(self, tipo):
        layout = [
            [interface_tela_tipos_visto.Text('Nome'), interface_tela_tipos_visto.InputText('')],
            [interface_tela_tipos_visto.Text('Validade'), interface_tela_tipos_visto.InputText('')],
            [interface_tela_tipos_visto.Text('Documentos???'), interface_tela_tipos_visto.InputText('')],
            [interface_tela_tipos_visto.Button('Confirmar'), interface_tela_tipos_visto.Button('Voltar')]
        ]
        self.__window = interface_tela_tipos_visto.Window(tipo).Layout(layout)
    
    # tela para excluir/modificar tipos de visto:
    def componentes_tela_excluir_modificar_tipos_visto(self, tipo):
        layout = [
            [interface_tela_tipos_visto.Text('Nome'), interface_tela_tipos_visto.InputText('')],
            [interface_tela_tipos_visto.Button('Confirmar'), interface_tela_tipos_visto.Button('Voltar')]
        ]
        self.__window = interface_tela_tipos_visto.Window(tipo).Layout(layout)
    
    def componentes_tela_listar_tipos_visto(self, lista_tipo_visto):
        layout = [
            [interface_tela_tipos_visto.Text('Lista de Tipo de Visto', font=("Helvica", 25))],
            [interface_tela_tipos_visto.Listbox(values=lista_tipo_visto, select_mode='extended', size=(30, 6))],
            [interface_tela_tipos_visto.Button('Voltar')]
        ]
        self.__window = interface_tela_tipos_visto.Window('Lista de Tipos de Visto').Layout(layout)
        button, values = self.__window.Read()
        self.close()
    
    # lógica para adicionar/excluir/modificar tipos de visto
    def logica_tela_tipos_visto(self):
        button, data = self.__window.Read()

        self.close()

        if button in (None, 'Voltar'):
            self.close()
            return None

        return data
    
    def tela_adicionar_tipos_visto(self):
        self.componentes_tela_adicionar_atualizar_tipos_visto('Adicionar Tipo de Visto')
        return self.logica_tela_tipos_visto()

    def tela_excluir_tipos_visto(self):
        self.componentes_tela_excluir_modificar_tipos_visto('Excluir Tipo de Visto')
        return self.logica_tela_tipos_visto()

    def tela_modificar_tipos_visto(self):
        self.componentes_tela_excluir_modificar_tipos_visto('Modificar Tipo de Visto')
        return self.logica_tela_tipos_visto()
    
    def tela_atualizar_tipos_visto(self):
        self.componentes_tela_adicionar_atualizar_tipos_visto('Atualizar Tipo de Visto')
        return self.logica_tela_tipos_visto()