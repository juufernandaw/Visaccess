class ControladorSistema:
    def __init__(self):
        self.__usuario_logado = None
        self.__controlador_consul = ControladorConsul(self)
        self.__controlador_agente = ControladorAgente(self)
        self.__controlador_gerente = ControladorGerente(self)

    @property
    def usuario_logado(self): #conseguir saber quem logou
        return self.__usuario_logado

    @property
    def controlador_consul(self):
        return self.__controlador_consul

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    @property
    def controlador_agente(self):
        return self.__controlador_agente

    def iniciar_tela_sistema(self):
        global opcao_escolhida
    
        pass

    def encerrar_sistema(self): #encerrar o sistema
        exit(0)
