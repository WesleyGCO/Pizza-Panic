import pygame # type: ignore

from adapters.implementations.ItemServiceImpl import ItemServiceImpl
from adapters.implementations.PersonagemServiceImpl import PersonagemServiceImpl
from adapters.implementations.TempoServiceImpl import TempoServiceImpl

from core.interfaces.FaseInterface import FaseInterface


class FaseServiceImpl(FaseInterface):
    def __init__(self, fase_model, fase_ui, jogo_servico, jogo_ui):
        self.fase_model = fase_model
        self.fase_ui = fase_ui
        self.jogo_ui = jogo_ui
        self.item_controller = ItemServiceImpl()
        self.personagem_servico = PersonagemServiceImpl()
        self.tempo_servico = TempoServiceImpl()
        self.jogo_servico = jogo_servico
        self.is_running = False

        self.clock = pygame.time.Clock()
        self.FPS = 120

    def iniciar(self):
        print(f"Iniciando fase {self.fase_model.numero}")
        self.is_running = True

        self.tempo_decorrido_ms = self.clock.tick(self.FPS)
        self.tempo_decorrido_segundos = self.tempo_decorrido_ms / 30

        while self.is_running:
            self.fase_ui.renderizar(self.fase_model, self.personagem_servico, self.tempo_servico, self.item_controller, self.tempo_decorrido_segundos)
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
            self.personagem_servico.andar_esquerda(self.fase_model.personagem, self.tempo_decorrido_segundos, self.jogo_ui.aceleracao)
        if teclas[pygame.K_RIGHT]:
            self.personagem_servico.andar_direita(self.fase_model.personagem, self.tempo_decorrido_segundos, self.jogo_ui.aceleracao, self.fase_ui.tela_largura)

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