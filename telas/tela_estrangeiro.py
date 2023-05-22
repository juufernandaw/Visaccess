import PySimpleGUI as tela_estrangeiro

class TelaEstrangeiro:
    def __init__(self):
        self.__window = None
        self.layout_tela_cadastro_agentes()
        self.layout_tela_adicionar_atualizar_agentes()

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        tela_estrangeiro.popup("", msg)

    def componentes_tela_cadastrar_estrangeiro(self):
        layout = [
            [tela_estrangeiro.Text('Cadastro de Estrangeiro', font=("Helvica", 25))],
            [tela_estrangeiro.Radio('Cadastrar Estrangeiro', "componentes_tela_cadastro_agentes", key='1')],
            [tela_estrangeiro.Radio('Excluir Estrangeiro', "componentes_tela_cadastro_agentes", key='2')],
            [tela_estrangeiro.Radio('Listar Estrangeiros', "componentes_tela_cadastro_agentes", key='3')],
            [tela_estrangeiro.Radio('Modificar dados do Estrangeiro', "componentes_tela_cadastro_agentes", key='4')],
            [tela_estrangeiro.Button('Confirmar'), tela_estrangeiro.Button('Voltar')]
        ]
        self.__window = tela_estrangeiro.Window('Tela de Cadastro de Estrangeiro').Layout(layout)

    def tela_cadastro_estrangeiro(self):
        self.componentes_tela_cadastrar_estrangeiro()
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

    def componentes_tela_adicionar_atualizar_estrangeiro(self, tipo):
        estado_civil = ["Solteiro", "Casado", "Viuvo(a)", "Namorando"]
        paises = ['Afeganistão', 'África do Sul', 'Albânia', 'Alemanha', 'Andorra', 'Angola', 'Antígua e Barbuda', 'Arábia Saudita', 'Argélia', 'Argentina', 'Armênia', 'Austrália', 'Áustria', 'Azerbaijão','Aruba', 'Bahamas', 'Bahrein', 'Bangladesh', 'Barbados', 'Belarus', 'Bélgica', 'Belize', 'Benin', 'Bhutan', 'Bolívia', 'Bósnia e Herzegovina', 'Botswana', 'Brasil', 'Brunei', 'Bulgária', 'Burkina Faso', 'Burundi', 'Butão', 'Cabo Verde', 'Camarões', 'Camboja', 'Canadá', 'Catar', 'Cazaquistão', 'Chade', 'Chile', 'China', 'Chipre', 'Colômbia', 'Comores', 'Congo', 'Coreia do Norte', 'Coreia do Sul', 'Costa do Marfim', 'Costa Rica', 'Croácia', 'Cuba', 'Dinamarca', 'Djibouti', 'Dominica', 'Egito', 'El Salvador', 'Emirados Árabes Unidos', 'Equador', 'Eritreia', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estados Unidos da América', 'Estônia', 'Etiópia', 'Fiji', 'Filipinas', 'Finlândia', 'França', 'Gabão', 'Gâmbia', 'Gana', 'Geórgia', 'Granada', 'Grécia', 'Guatemala', 'Guiana', 'Guiné', 'Guiné Equatorial', 'Guiné-Bissau', 'Haiti', 'Honduras', 'Hungria', 'Iêmen', 'Ilhas Marshall', 'Ilhas Maurício', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Irlanda', 'Islândia', 'Israel', 'Itália', 'Jamaica', 'Japão', 'Jordânia', 'Kiribati', 'Kosovo', 'Kuwait', 'Laos', 'Lesoto', 'Letônia', 'Líbano', 'Libéria', 'Líbia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Macedônia', 'Madagascar', 'Malásia', 'Malawi', 'Maldivas', 'Mali', 'Malta', 'Marrocos', 'Mauritânia', 'México', 'Micronésia', 'Moçambique', 'Moldávia', 'Mônaco', 'Mongólia', 'Montenegro', 'Namíbia', 'Nauru', 'Nepal', 'Nicarágua', 'Níger', 'Nigéria', 'Noruega', 'Nova Zelândia', 'Omã', 'Holanda', 'Peru', 'Palestina', 'Panamá', 'Papua Nova Guiné', 'Paquistão', 'Paraguai', 'Peru', 'Polônia', 'Venezuela','Tailândia','Suriname','Uruguai']
        layout = [
            [tela_estrangeiro.Text('Passaporte'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Nome'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Data de Nascimento'), tela_estrangeiro.CalendarButton(target='data_nasc')],
            [tela_estrangeiro.Text('Estado civil'), tela_estrangeiro.Combo(estado_civil)],
            [tela_estrangeiro.Text('País'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Estado'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Cidade'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Trabalho'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Text('Profissão'), tela_estrangeiro.Combo(['Sim', 'Não'])],
            [tela_estrangeiro.Button('Confirmar'), tela_estrangeiro.Button('Voltar')]
        ]
        self.__window = tela_estrangeiro.Window(tipo).Layout(layout)

    def componentes_tela_excluir_modificar_estrangeiro(self, tipo):
        layout = [
            [tela_estrangeiro.Text('Passaporte'), tela_estrangeiro.InputText('')],
            [tela_estrangeiro.Button('Confirmar'), tela_estrangeiro.Button('Voltar')]
        ]
        self.__window = tela_estrangeiro.Window(tipo).Layout(layout)

    def componentes_tela_listar_estrangeiro(self, lista_estrangeiros):
        layout = [
            [tela_estrangeiro.Text('Lista Estrangeiros', font=("Helvica", 25))],
            [tela_estrangeiro.Listbox(values=lista_estrangeiros, select_mode='extended', size=(30, 6))],
            [tela_estrangeiro.Button('Voltar')]
        ]
        self.__window = tela_estrangeiro.Window('Lista de Estrangeiro').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        return button, values

    # lógica para adicionar/excluir/modificar estrangeiro
    def logica_tela_estrangeiro(self):
        button, values = self.__window.Read()
        self.close()
        if button in (None, 'Voltar'):
            return 0
        return values
    
    def tela_adicionar_estrangeiro(self):
        self.componentes_tela_adicionar_atualizar_estrangeiro('Adicionar Estrangeiro')
        return self.logica_tela_estrangeiro()

    def tela_excluir_estrangeiro(self):
        self.componentes_tela_excluir_modificar_estrangeiro('Excluir Estrangeiro')
        return self.logica_tela_estrangeiro()

    def tela_modificar_estrangeiro(self):
        self.componentes_tela_excluir_modificar_estrangeiro('Modificar Estrangeiro')
        return self.logica_tela_estrangeiro()
    
    def tela_atualizar_estrangeiro(self):
        self.componentes_tela_adicionar_atualizar_estrangeiro('Atualizar Estrangeiro')
        return self.logica_tela_estrangeiro()