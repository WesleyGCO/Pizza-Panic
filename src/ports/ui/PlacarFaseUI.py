class PlacarFaseUI:
    def renderizar(self, fonte, tela, pedidos_coletados, posicao_x, posicao_y, fase):
        self.pedido = fase.pedido

        texto = f"Atender: {self.pedido}"
        texto2 = f"Atendidos: {pedidos_coletados}"

        superficie_texto = fonte.render(texto, True, (255, 255, 255))
        superficie_texto2 = fonte.render(texto2, True, (255, 255, 255))

        # Calcular a largura total dos textos
        largura_total = superficie_texto.get_width() + superficie_texto2.get_width() + 5  # 20 é o espaçamento entre os textos

        # Calcular a posição X centralizada, considerando a borda
        posicao_x_centralizada = (tela.get_width() - largura_total) // 2

        # Calcular a posição Y centralizada na parte superior, considerando a borda e o menu superior
        posicao_y_centralizada = 50 // 2  # 50 é a altura do menu superior

        # Desenhar os textos centralizados
        tela.blit(superficie_texto, (posicao_x_centralizada, posicao_y_centralizada))
        tela.blit(superficie_texto2, (posicao_x_centralizada + superficie_texto.get_width() + 20, posicao_y_centralizada))


        if (self.pedido == pedidos_coletados):
            fase.concluida = True

    
