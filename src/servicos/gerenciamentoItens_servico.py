from servicos.item_servico import Item_Servico

class GerenciamentoItens_Servico:

    def criar_item(self):
        return Item_Servico.criar_item()

    def desenhar_item(self, itemRuim, screen, imagem):
        Item_Servico.desenhar_item(itemRuim, screen, imagem)

    def movimento_item(self, itemRuim, gravidade):
        # Dá movimento para os itens baseados na gravidade
        Item_Servico.movimento_item(itemRuim, gravidade)

    def reinicia_item(self, itemRuim):
        # Reinicia os itens de acordo com o eixo y
        Item_Servico.reinicia_item(itemRuim)

    def checa_colisao(self, personagem, itemColide):
        return Item_Servico.checa_colisao(personagem, itemColide)