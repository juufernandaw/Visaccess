import PySimpleGUI as tela_blacklist


class TelaBlacklist:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()
