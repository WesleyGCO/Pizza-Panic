class Vetor:
    def __init_Personagem__(self, cor, tamanho_x, tamanho_y, velocidade, posicao_x, posicao_y):
        self.cor = cor
        self.tamanho_x = tamanho_x
        self.tamanho_y = tamanho_y
        self.velocidade = velocidade
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def __init_ItemRuim__(self, x, y):
        self.x = x
        self.y = y
    
    def andar_esquerda(self):
        pass

    def andar_direita(self):
        pass

    def desenhar(self, screen):
        pass

    def atualiza(self, vx, vy):
        self.x += vx
        self.y += vy