import pygame #type: ignore

from ports.ui.PlacarFaseUI import PlacarFaseUI
from ports.ui.MenuBordaUI import MenuBordaUI

class FaseUI:
    def __init__(self, tela, tela_altura, tela_largura, fonte, relogio, posicao_x_texto, posicao_y_texto, velocidade):
        self.tela = tela
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.fonte = fonte
        self.relogio = relogio
        self.posicao_x_texto = posicao_x_texto
        self.posicao_y_texto = posicao_y_texto
        self.velocidade = velocidade
        self.imagem = pygame.image.load("assets\\Imagens\\fundo8x6.png")
        self.imagem_fundo = pygame.transform.scale(self.imagem, (self.tela_altura, self.tela_largura))
        self.placar_fase_ui = PlacarFaseUI()

    def renderizar(self, fase_model, personagem_servico, tempo_servico, item_servico, tempo):
        self.tela.fill((147, 158, 150))

        self.tela.blit(self.imagem_fundo, (0, 0))

        MenuBordaUI.menuBordaUI(self.tela, self.tela_altura, self.tela_largura)

        # Renderiza a borda do menu
        personagem_servico.desenhar_personagem(fase_model.personagem, self.tela)
        
        tempo_servico.atualizar_contador(self.tela, fase_model.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)
        tempo_servico.contagem_regressiva(self.tela, fase_model.tempo_inicial, self.tela_altura, self.fonte)
        
        # Desenha, movimenta e reinicia os itens
        for item in fase_model.itens_ruins:
            item_servico.desenhar_item(item, self.tela)
            item_servico.movimento_item(item, tempo)
            item_servico.reinicia_item_sumiu(item)

        self.placar_fase_ui.renderizar(self.fonte, self.tela, fase_model.pedido_coletado, self.posicao_x_texto, self.posicao_y_texto + 30, fase_model)

        pygame.display.flip()
        self.relogio.tick(60)
