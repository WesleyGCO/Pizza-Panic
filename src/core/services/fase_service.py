from application.models.Personagem import Personagem

from core.interfaces.FaseInterface import FaseInterface
from core.services.item_service import ItemService
from core.services.personagem_service import PersonagemService

from adapters.primary import pygame_output_adapter, pygame_input_adapter
from adapters.primary.use_cases import gerenciar_fase
from core.services.tempo_service import TempoService

class FaseService(FaseInterface):
    
    def __init__(self, fase_model, fase_ui, item_service, personagem_service):
        self.fase_model = fase_model
        self.fase_ui = fase_ui
        self.item_service = item_service
        self.personagem_service = personagem_service
        self.tempo_service = TempoService()
        self.is_running = False
        
        self.tempo = 0
        self.relogio = pygame_output_adapter.criar_relogio()
        self.FPS = 120        
    
    def iniciar(self):
        print(f"Iniciando fase {self.fase_model.numero}")
        self.is_running = True
        
        self.tempo_decorrido_ms = self.relogio.tick(self.FPS)
        self.tempo_decorrido_seg = self.tempo_decorrido_ms / 1000

        while self.is_running:
            self.fase_model.personagem.processamento_fisica(self.tempo_decorrido_seg)
            map(lambda item: item.processamento_fisica(self.tempo_decorrido_seg), self.fase_model.itens_ruins)
            self.fase_ui.renderizar(self.fase_model, self.personagem_service, self.tempo_service, self.item_service, self.tempo_decorrido_seg)
            self.lidar_entrada()
            self.atualizar()
    
    def lidar_entrada(self):
        for evento in pygame_input_adapter.capturar_eventos():
            if pygame_input_adapter.eh_sair(evento):
                self.is_running = False
                quit()
                
        tecla_pressionada = pygame_input_adapter.capturar_tecla()
        
        if (tecla_pressionada['esquerda']):
            if isinstance(self.fase_model.personagem, Personagem):
                if(self.fase_model.personagem.posicao.x >= 0):
                    self.fase_model.personagem.velocidade.x = -500
                else:
                    self.fase_model.personagem.velocidade.x = 0
        elif (tecla_pressionada['direita']):
            if isinstance(self.fase_model.personagem, Personagem):
                if(self.fase_model.personagem.posicao.x <= 700):
                    self.fase_model.personagem.velocidade.x = +500
                else:
                    self.fase_model.personagem.velocidade.x = 0
        else:
            if isinstance(self.fase_model.personagem, Personagem):
                self.fase_model.personagem.velocidade.x = 0
    
    def atualizar(self):
        gerenciar_fase.verificar_conclusao_fase(self.fase_model)

        if(self.fase_model.concluida == True):
            self.is_running = False

        for item in self.fase_model.itens_ruins:
            if self.item_service.checa_colisao(self.fase_model.personagem, item):
                self.personagem_service.coletar_item(self.fase_model.personagem, item)
                self.contar_pedido(self.fase_model, item)
                novo_item = self.item_service.reinicia_item(item)
                self.fase_model.itens_ruins.remove(item)
                self.fase_model.itens_ruins.append(novo_item)
        
    def contar_pedido(self, fase_model, item):
        if item.tipo == "pizza":
            return fase_model.adicionar_pedido_coletado()