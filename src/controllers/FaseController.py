import pygame # type: ignore
from servicos.item_servico import Item_Servico
from servicos.jogo_servico import Jogo_Servico
from servicos.personagem_servico import Personagem_Servico
from servicos.tempo_servico import Tempo_Servico

class FaseController:
    def __init__(self, fase_model, fase_view):
        self.fase_model = fase_model
        self.fase_view = fase_view
        self.item_servico = Item_Servico()
        self.personagem_servico = Personagem_Servico()
        self.tempo_servico = Tempo_Servico()
        self.jogo_servico = Jogo_Servico()
        self.is_running = False

    def iniciar(self):
        print(f"Iniciando fase {self.fase_model.numero}")
        self.is_running = True
        while self.is_running:
            self.fase_view.renderizar(self.fase_model, self.personagem_servico, self.tempo_servico, self.item_servico, self.jogo_servico)
            self.handle_input()
            self.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                quit()

        # Verificar teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.personagem_servico.andar_esquerda(self.fase_model.personagem)
        if teclas[pygame.K_RIGHT]:
            self.personagem_servico.andar_direita(self.fase_model.personagem, self.fase_view.tela_altura)

    def update(self):
        # Verificar colisão entre personagem e item
        for item in self.fase_model.itens_ruins:
            if self.item_servico.checa_colisao(self.fase_model.personagem, item):
                self.personagem_servico.coletar_item(self.fase_model.personagem, item)
                self.item_servico.reinicia_item_coletou(item)
