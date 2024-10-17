class Fase:
    """
    Classe responsável por representar o estado geral da fase.
    
    Atributos:
        numero (int): Representa o número da fase
        concluida (bool): Indica se a fase foi concluída
        perdida (bool): Indicia se a fase foi perdida
        personagem (Personagem): Representa o objeto da entidade Personagem
        itens_ruins (Item[]): Representa um vetor com vários objetos da entidade Item
        tempo_inicial (int): Indica o tempo inicial da fase
        pedido_coletado (int): Indica a quantidade de pedidos que foram coletados
        pedido (int): Indica a quantidade de pedido que devem ser atendidos
        tempo_fase_comeca (int): Indica o tempo atual que a fase começou
        
    Métodos:
        concluir(): Método responsável por concluir a fase
        perdeu(): Método responsável por perder a fase
        adicionar_pedido_coletado(): Método responsável por adicionar mais 1 no atributo pedido_coletado
    """
    
    def __init__(self, numero, personagem, itens_ruins, tempo_inicial, pedido, tempo_fase_comeca):
        """
        Inicializa uma nova instância da entidade Fase, configurando os atributos padrão da fase.
        
        Args:
            numero (int): Número da fase atual
            personagem (Personagem): Objeto da entidade Personagem
            itens_ruins (Item[]): Vetor com vários objetos da entidade Item
            tempo_inicial (int): Tempo inicial pré definido
            pedido (int): Quantidade de pedido que devem ser atendidos
            tempo_fase_comeca (int): Tempo atual que a fase começou
            
        Atributos pré-definidos:
            concluida (bool): False
            perdida (bool): False
            pedido_coletado (int): inicia com 0
        """
        self.numero = numero
        self.concluida = False
        self.perdida = False
        self.personagem = personagem
        self.itens_ruins = itens_ruins
        self.tempo_inicial = tempo_inicial
        self.pedido_coletado = 0
        self.pedido = pedido
        self.tempo_fase_comeca = tempo_fase_comeca

    def concluir(self):
        """
        Método responsável por concluir a fase
        
        Returns:
            Atributo concluida como True indicando que a fase atual foi concluída
            Apresenta no console uma mensagem de "Fase x concluída!" onde X é o número da fase atual
        """
        self.concluida = True
        print(f"Fase {self.numero} concluída!")
        
    def perdeu(self):
        """
        Método responsável por perder a fase
        
        Returns:
            Atirbuto "perdida" como True indicando que a fase atual foi perdida
            Atributo "concluida" como False indicando que a fase atual não foi concluída
            Apresenta no console uma mensagem de "Fase x perdida!" onde X é o número da fase atual
        """
        self.perdida = True
        self.concluida = False
        print(f"Fase {self.numero} perdida!")

    def adicionar_pedido_coletado(self):
        """
        Método responsável por adicionar mais 1 ao atributo "pedido_coletado"
        
        Return:
            None
        """
        self.pedido_coletado += 1

    