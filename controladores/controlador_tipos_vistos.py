from entidades.tipo_de_visto import TipoDeVisto
from telas.tela_tipos_vistos import TelaTipoVisto

class ControladorTiposVisto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipos_vistos = TelaTipoVisto()

# PROPERTY:
    @property
    def tela_tipos_vistos(self):
        return self.__tela_tipos_vistos
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

# ABRIR TELA PRINCIPAL:

    def abrir_tela_cadastro(self):
        while True:
            opcao = self.tela_tipos_vistos.tela_cadastro_tipos_visto()
            if opcao == 1:
                self.novo_tipos_visto()
            elif opcao == 2:
                self.excluir_tipos_visto()
            elif opcao == 3:
                self.listar_tipos_visto()
            elif opcao == 4:
                self.modificar_tipos_visto()
            elif opcao == 0 or opcao == None:
                self.controlador_sistema.controlador_consul.abre_tela_inicial()

    def novo_tipos_visto(self):
        self.tela_tipos_vistos.tela_adicionar_tipos_visto()

    def excluir_tipos_visto(self):
        self.tela_tipos_vistos.tela_excluir_tipos_visto()


    def listar_tipos_visto(self):
        # requer SQLite!!!
        pass

    def modificar_tipos_visto(self):
        self.tela_tipos_vistos.tela_modificar_tipos_visto()
        # depois vai chamar self.tela_tipos_vistos.tela_atualizar_tipos_visto()

