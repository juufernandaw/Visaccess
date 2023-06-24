from telas.tela_relatorio import TelaRelatorio
from persistencia.relatorioDAO import RelatorioDAO
from excecoes.valueErrorException import ValueErrorException

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
        self.__relatorio_DAO = RelatorioDAO()

    @property
    def relatorio_DAO(self):
        return self.__relatorio_DAO
    
    def abre_tela_relatorios(self):
        try:
            opcoes_relatorios = {1: self.relatorio_paises,
                                 2: self.relatorio_tipos_de_visto,
                                 0: self.__controlador_sistema.get_controlador_gerente.iniciar_tela_gerente}
            while True:
                opcao_escolhida = self.__tela_relatorio.emissao_relatorios()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueErrorException
                funcao_escolhida = opcoes_relatorios[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_relatorio.mostra_mensagem(e)
            self.abre_tela_relatorios()

    def relatorio_paises(self):
        print('entrou no relatorio de países')
        relatorios = self.__relatorio_DAO.relatorio_paises()
        botao, values = self.__tela_relatorio.relatorio_paises(relatorios)
        if botao == 'Voltar':
            return self.abre_tela_relatorios()

    def relatorio_tipos_de_visto(self):
        print('entrou no relatorio de tipos de visto')
        relatorios = self.__relatorio_DAO.relatorio_tipos_de_visto()
        botao, values = self.__tela_relatorio.relatorio_tipos_de_visto(relatorios)
        if botao == 'Voltar':
            return self.abre_tela_relatorios()


