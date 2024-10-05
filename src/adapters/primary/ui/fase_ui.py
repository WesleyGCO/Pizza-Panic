from adapters.primary import pygame_output_adapter
from adapters.primary.ui.menu_borda_ui import menu_borda_ui
from core.services.placar_service import PlacarService
from application.models.Sprites import Sprites

class FaseUI:
    def __init__(self, tela_altura, tela_largura, relogio, posicao_x_texto, posicao_y_texto):
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.relogio = relogio
        self.posicao_x_texto = posicao_x_texto
        self.posicao_y_texto = posicao_y_texto
        self.imagem = pygame_output_adapter.carregar_imagem("./adapters/primary/sprites/fundo8x6.png")
        self.imagem_redimensionada = pygame_output_adapter.redimensionar_imagem(self.imagem, self.tela_altura, self.tela_largura)
        self.placar_service = PlacarService()
        self.sprites = Sprites()

        self.angulo = 0
        
    def renderizar(self, fase_model, personagem_servico, tempo_servico, item_servico, tempo, sprite):
        pygame_output_adapter.preencher_tela((147, 158, 150))
        pygame_output_adapter.desenhar_superficie(self.imagem_redimensionada, (0, 0))
        
        menu_borda_ui(self.tela_altura, self.tela_largura)

        
        
        
        personagem_servico.desenhar_personagem(fase_model.personagem, sprite)

        tempo_servico.atualizar_contador(fase_model.personagem, self.posicao_x_texto, self.posicao_y_texto)
        tempo_servico.contagem_regressiva(fase_model, self.tela_altura)

        if self.angulo >= 360:
            self.angulo = 0
        else:
            self.angulo -= 3

        # print(self.angulo)
        
        for item in fase_model.itens_ruins:
            item_servico.desenhar_rodar_item(item, self.angulo)
            item_servico.movimento_item(item, tempo)
            if (item.posicao.y > 600):
                novo_item = item_servico.reinicia_item(item)
                fase_model.itens_ruins.remove(item)
                fase_model.itens_ruins.append(novo_item)
        
        self.placar_service.renderizar_placar(fase_model)
        
        pygame_output_adapter.atualizacao_display()
        self.relogio.tick(60)