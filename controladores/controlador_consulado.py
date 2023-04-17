from excecoes.valueErrorException import ValueErrorException
from persistencia.consuladoDAO import ConsuladoDAO
from entidades.consulado import Consulado
from telas.tela_consulado import TelaConsulado


class ControladorConsulado:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__consulado_DAO = ConsuladoDAO()
        self.__consulado_tela = TelaConsulado()

    def abre_tela_consulados(self):
        try:
            # usuario = self.__controlador_sistema.usuario_logado
            mexer_consulado_opcoes = {1: self.incluir_consulado,
                                      2: self.excluir_consulado,
                                      3: self.listar_consulados,
                                      4: self.alterar_consulado
                                      }
            while True:
                opcao_escolhida = self.__consulado_tela.tela_consulado_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 4:
                    raise ValueErrorException
                funcao_escolhida = mexer_consulado_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__consulado_tela.mostrar_msg(e)
            self.abre_tela_consulados()

    def incluir_consulado(self):
        dados_consulado = self.__consulado_tela.pegar_dados_consulado()
        for consulado in self.__consulado_DAO.get_all_consulados():
            if dados_consulado == consulado.sede:
                self.__consulado_tela.mostrar_msg("Este consulado já consta no sistema!")
                return self.incluir_consulado()
        else:
            consulado = Consulado(dados_consulado)
            self.__consulado_DAO.create_consulado(sede=consulado.sede)
            if consulado is not None:
                self.__consulado_tela.mostrar_msg("Consulado cadastrado com sucesso!")
                return self.abre_tela_consulados()

    def alterar_consulado(self):
        consulado = self.__consulado_tela.componentes_tela_alterar_qual_consulado()
        consulado_novo = self.__consulado_tela.componentes_tela_alterar_consulado(consulado)
        # consulado.sede = consulado["sede"]
        if consulado_novo is not None:
            self.__consulado_tela.mostrar_msg("Consulado alterado com sucesso!")
        self.__consulado_DAO.update_consulado(velha_sede=consulado.sede, nova_sede=consulado_novo["sede"])
        return self.abre_tela_consulados()

    def excluir_consulado(self):
        consulado = self.__consulado_tela.componentes_tela_excluir_consulado()
        # consulado.sede = consulado["sede"]
        # if consulado is not None:
        #     self.__consulado_tela.mostrar_msg("Consulado alterado com sucesso!")
        self.__consulado_DAO.delete_consulado(sede=consulado.sede)
        return self.abre_tela_consulados()

    def listar_consulados(self):
        consulados = self.__consulado_DAO.get_all_consulados()
        self.__consulado_tela.componentes_tela_listar_consulados(lista_consulados=consulados)
