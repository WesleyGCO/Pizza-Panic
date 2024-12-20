from application.models.Personagem import Personagem
from application.models.Sprites import Sprites

from core.interfaces.FaseInterface import FaseInterface

from adapters.primary import pygame_output_adapter, pygame_input_adapter
from adapters.primary.use_cases import gerenciar_fase, gerenciar_jogo

class FaseService(FaseInterface):
    
    def __init__(self, fase_model, fase_ui, item_servico, personagem_servico, tempo_servico, jogo_model, tamanho_tela_largura, tamanho_tela_altura):
        self.fase_model = fase_model
        self.fase_ui = fase_ui
        self.item_servico = item_servico
        self.personagem_servico = personagem_servico
        self.tempo_servico = tempo_servico
        self.is_running = False
        self.jogo_model = jogo_model
        
        self.tela_largura = tamanho_tela_largura
        self.tela_altura = tamanho_tela_altura

        self.fase_model.personagem.velocidade.x = 0
        self.fase_model.personagem.posicao.x = 100
        
        self.tempo = 0
        self.relogio = pygame_output_adapter.criar_relogio()
        self.FPS = 120

        self.sprites = Sprites()  
        self.sprite_atual =  self.sprites.get_personagem_sprite_esquerda()

        self.ultima_posicao = ""

    
    def iniciar(self):
        print(f"Iniciando fase {self.fase_model.numero}")
        self.is_running = True
        
        self.tempo_decorrido_ms = self.relogio.tick(self.FPS)
        self.tempo_decorrido_seg = self.tempo_decorrido_ms / 1000

        while self.is_running:
            self.fase_model.personagem.processamento_fisica(self.tempo_decorrido_seg)
            map(lambda item: item.processamento_fisica(self.tempo_decorrido_seg), self.fase_model.itens_ruins)
            self.fase_ui.renderizar(self.fase_model, self.personagem_servico, self.tempo_servico, self.item_servico, self.tempo_decorrido_seg, self.sprite_atual)
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
                self.sprite_atual =  self.sprites.animar_personagem_esquerda()
                self.ultima_posicao = 'esquerda'
                if(self.fase_model.personagem.posicao.x >= 0):
                    self.fase_model.personagem.velocidade.x = -500
                else:
                    self.fase_model.personagem.velocidade.x = 0
        elif (tecla_pressionada['direita']):
            if isinstance(self.fase_model.personagem, Personagem):
                self.sprite_atual =  self.sprites.animar_personagem_direita()
                self.ultima_posicao = 'direita'
                if(self.fase_model.personagem.posicao.x <= 700):
                    self.fase_model.personagem.velocidade.x = +500
                else:
                    self.fase_model.personagem.velocidade.x = 0
        elif (tecla_pressionada['esc']):
            gerenciar_jogo.iniciar_jogo(self.tela_largura, self.tela_altura)
        else:
            if isinstance(self.fase_model.personagem, Personagem):
                self.fase_model.personagem.velocidade.x = 0
                if(self.ultima_posicao == 'esquerda'):
                    self.sprite_atual =  self.sprites.get_personagem_sprite_esquerda_parado()
                else:
                    self.sprite_atual =  self.sprites.get_personagem_sprite_direita_parado()
    
    def atualizar(self):
        gerenciar_fase.verificar_conclusao_fase(self.fase_model)

        if (self.fase_model.concluida == True):
            self.is_running = False
        elif (self.fase_model.perdida == True):
            self.is_running = False

        for item in self.fase_model.itens_ruins:
            if self.item_servico.checa_colisao(self.fase_model.personagem, item):
                self.personagem_servico.adicionar_pontuacao(self.fase_model.personagem, item)
                self.contar_pedido(self.fase_model, item)
                novo_item = self.item_servico.reinicia_item(item)
                self.fase_model.itens_ruins.remove(item)
                self.fase_model.itens_ruins.append(novo_item)
        
    def contar_pedido(self, fase_model, item):
        if item.tipo == "pizza":
            return fase_model.adicionar_pedido_coletado()