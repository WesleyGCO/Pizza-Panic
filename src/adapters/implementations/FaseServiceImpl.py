import pygame # type: ignore

from adapters.implementations.ItemServiceImpl import ItemServiceImpl
from adapters.implementations.PersonagemServiceImpl import PersonagemServiceImpl
from adapters.implementations.TempoServiceImpl import TempoServiceImpl

from core.interfaces.FaseInterface import FaseInterface


class FaseServiceImpl(FaseInterface):
    def __init__(self, fase_model, fase_view, jogo_servico):
        self.fase_model = fase_model
        self.fase_view = fase_view
        self.item_controller = ItemServiceImpl()
        self.personagem_servico = PersonagemServiceImpl()
        self.tempo_servico = TempoServiceImpl()
        self.jogo_servico = jogo_servico
        self.is_running = False

    def iniciar(self):
        print(f"Iniciando fase {self.fase_model.numero}")
        self.is_running = True
        while self.is_running:
            self.fase_view.renderizar(self.fase_model, self.personagem_servico, self.tempo_servico, self.item_controller)
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
        if (self.fase_model.concluida == True):
            self.is_running = False     
        
        novos_itens = []
        # Verificar colisão entre personagem e item
        for item in self.fase_model.itens_ruins:
            if self.item_controller.checa_colisao(self.fase_model.personagem, item):
                self.personagem_servico.coletar_item(self.fase_model.personagem, item)
                self.personagem_servico.contar_pedido(self.fase_model, item)
                novo_item = self.item_controller.reinicia_item_coletou(item)
                novos_itens.append(novo_item)
                self.fase_model.itens_ruins = novos_itens
            else:
                novos_itens.append(item)
                self.fase_model.itens_ruins = novos_itens