
class PlacarFaseUI:

    def renderizar(self, fonte, tela, pedidos_coletados, posicao_x, posicao_y, fase):
        self.pedido = fase.pedido

        texto = f"Pedidos Coletados: {pedidos_coletados}"
        texto2 = f"Pedido para atender: {self.pedido}"

        superficie_texto = fonte.render(texto, True, (255, 255, 255))
        superficie_texto2 = fonte.render(texto2, True, (255, 255, 255))

        tela.blit(superficie_texto, (posicao_x, posicao_y))
        tela.blit(superficie_texto2, (posicao_x + 20, posicao_y + 30))

        if (self.pedido == pedidos_coletados):
            fase.concluida = True

    
