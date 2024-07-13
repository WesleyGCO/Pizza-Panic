import pygame

class FaseView:
    def __init__(self, tela, tela_altura, tela_largura, fonte, relogio, posicao_x_texto, posicao_y_texto, gravidade):
        self.tela = tela
        self.tela_altura = tela_altura
        self.tela_largura = tela_largura
        self.fonte = fonte
        self.relogio = relogio
        self.posicao_x_texto = posicao_x_texto
        self.posicao_y_texto = posicao_y_texto
        self.gravidade = gravidade

    def renderizar(self, fase_model, personagem_servico, tempo_servico, item_servico, jogo_servico):
        self.tela.fill((147, 158, 150))

        jogo_servico.menu_borda(self.tela, self.tela_altura, self.tela_largura)

        # Renderiza a borda do menu
        personagem_servico.desenhar_personagem(fase_model.personagem, self.tela)
        
        tempo_servico.atualizar_contador(self.tela, fase_model.personagem, self.posicao_x_texto, self.posicao_y_texto, self.fonte)
        tempo_servico.contagem_regressiva(self.tela, fase_model.tempo_inicial, self.tela_altura, self.fonte)
        
        # Desenha, movimenta e reinicia os itens
        for item in fase_model.itens_ruins:
            item_servico.desenhar_item(item, self.tela)
            item_servico.movimento_item(item, self.gravidade)
            item_servico.reinicia_item_sumiu(item)

        pygame.display.flip()
        self.relogio.tick(60)
