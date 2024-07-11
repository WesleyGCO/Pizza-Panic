import pygame
from servicos.item_servico import Item_Servico
from servicos.jogo_servico import Jogo_Servico
from servicos.personagem_servico import Personagem_Servico
from servicos.tempo_servico import Tempo_Servico

class Fase:
    def __init__(self, numero, tela, tela_altura, tela_largura, personagem, 
                 itens_ruins, tempo_inicial, posicao_x_texto, posicao_y_texto, fonte, gravidade, relogio):
        self.numero = numero
        self.concluida = False
        self.tela = tela
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.personagem = personagem
        self.itens_ruins = itens_ruins
        self.tempo_inicial = tempo_inicial
        self.item_servico = Item_Servico()
        self.personagem_servico = Personagem_Servico()
        self.tempo_servico = Tempo_Servico()
        self.jogo_servico = Jogo_Servico()
        self.is_running = False
        self.posicao_x_texto = posicao_x_texto
        self.posicao_y_texto = posicao_y_texto
        self.fonte = fonte
        self.gravidade = gravidade
        self.relogio = relogio

    def iniciar(self):
        print("Iniciando fase {self.numero}")
        self.is_running = True
        while self.is_running:
            self.tela.fill((0, 0, 0))
            self.handle_input()
            self.update()
            self.render()

    def concluir(self):
        self.concluida = True
        print("Fase concluída!")

    def resetar(self):
        self.concluida = False
        print("Fase resetada")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                quit()

        # Verificar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.personagem_servico.andar_esquerda(self.personagem)
        if teclas[pygame.K_RIGHT]:
            self.personagem_servico.andar_direita(self.personagem, self.tela_altura)

    def update(self):
        # Verificar colisão entre personagem e item
        for item in self.itens_ruins:
            if self.item_servico.checa_colisao(self.personagem, item):
                self.personagem_servico.coletar_item(self.personagem, item)
                self.item_servico.reinicia_item_coletou(item)

    def render(self):
        self.tela.fill((147, 158, 150))

        self.jogo_servico.menu_borda(self.tela, self.tela_altura, self.tela_largura)

        self.personagem_servico.desenhar_personagem(self.personagem, self.tela)
        
        self.tempo_servico.atualizar_contador(self.tela, self.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)
        self.tempo_servico.contagem_regressiva(self.tela, self.tempo_inicial, self.tela_altura, self.fonte)
        
        # Desenha, movimenta e reinicia os itens
        for item in self.itens_ruins:
            self.item_servico.desenhar_item(item, self.tela)
            self.item_servico.movimento_item(item, self.gravidade)
            self.item_servico.reinicia_item_sumiu(item)

        pygame.display.flip()
        self.relogio.tick(60)