class JogoUI:
    def __init__(self, tela_altura, tela_largura, item_servico, personagem_servico):
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.item_servico = item_servico
        self.personagem_servico = personagem_servico
        
        self.personagem_posicao_x_ratio = 0.5
        self.personagem_posicao_y_ratio = 0.8
        self.aceleracao = 0
        self.personagem = self.personagem_servico.criar_personagem(tela_altura, tela_largura, self.personagem_posicao_x_ratio, self.personagem_posicao_y_ratio, self.aceleracao)
        self.itens_ruins = [self.item_servico.criar_item() for _ in range(5)]
        self.is_running = True