

class Consulado:

    def __init__(self, sede: str):
        self.__sede = sede

    @property
    def sede(self):
        return self.__sede
