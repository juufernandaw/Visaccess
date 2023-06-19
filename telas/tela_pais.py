import PySimpleGUI as tela_pais


class TelaPais:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        tela_pais.popup("", msg)

    def componentes_tela_cadastrar_pais(self):
        layout = [
            [tela_pais.Text('Cadastro de Países', font=("Helvica", 25))],
            [tela_pais.Radio('Adicionar Países', "componentes_tela_cadastro_agentes", key='1')],
            [tela_pais.Radio('Excluir Países', "componentes_tela_cadastro_agentes", key='2')],
            [tela_pais.Radio('Listar Países', "componentes_tela_cadastro_agentes", key='3')],
            [tela_pais.Radio('Alterar Países', "componentes_tela_cadastro_agentes", key='4')],
            [tela_pais.Button('Confirmar'), tela_pais.Button('Voltar')]
        ]
        self.__window = tela_pais.Window('Tela de Cadastro de Estrangeiro').Layout(layout)

    def tela_cadastro_pais(self):
        self.componentes_tela_cadastrar_pais()
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

    def componentes_tela_adicionar_atualizar_pais(self, tipo, lista_paises):
        estado_civil = ["Solteiro", "Casado", "Viuvo(a)", "Namorando"]
        # paises = ['Argentina', 'Paraguai', 'Uruguai']  # vai vim do BD ainda preciso fazer isso
        layout = [
            [tela_pais.Text('País'), tela_pais.InputText('')],
            [tela_pais.Text('Países'), tela_pais.Combo(estado_civil)],
            [tela_pais.Text('Isento'), tela_pais.Combo([True, False])],
            [tela_pais.Button('Confirmar'), tela_pais.Button('Voltar')]
        ]
        self.__window = tela_pais.Window(tipo).Layout(layout)

    def componentes_tela_excluir_modificar_pais(self, tipo):
        layout = [
            [tela_pais.Text('Nome'), tela_pais.InputText('')],
            [tela_pais.Button('Confirmar'), tela_pais.Button('Voltar')]
        ]
        self.__window = tela_pais.Window(tipo).Layout(layout)

    def tela_listar_pais(self, lista_paises):
        layout = [
            [tela_pais.Text('Lista pais', font=("Helvica", 25))],
            [tela_pais.Listbox(values=lista_paises, select_mode='extended', size=(30, 6))],
            [tela_pais.Button('Voltar')]
        ]
        self.__window = tela_pais.Window('Lista de Paises').Layout(layout)
        button = self.__window.Read()
        self.close()
        if button[0] == 'Voltar':
            return 0
        return button

    # lógica para adicionar/excluir/modificar pais
    def logica_tela_pais(self):
        button, values = self.__window.Read()
        self.close()
        if button in (None, 'Voltar'):
            return 0
        return values

    def tela_adicionar_pais(self, lista_paises):
        self.componentes_tela_adicionar_atualizar_pais('Adicionar País', lista_paises)
        return self.logica_tela_pais()

    def tela_excluir_pais(self):
        self.componentes_tela_excluir_modificar_pais('Excluir País')
        return self.logica_tela_pais()

    def tela_modificar_pais(self, lista_paises):
        self.componentes_tela_excluir_modificar_pais('Alterar País', lista_paises)
        return self.logica_tela_pais()

    def tela_atualizar_pais(self):
        self.componentes_tela_adicionar_atualizar_pais('Atualizar País')
        return self.logica_tela_pais()
