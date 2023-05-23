import PySimpleGUI as tela_tipo_visto


class TelaTipoVisto:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()
