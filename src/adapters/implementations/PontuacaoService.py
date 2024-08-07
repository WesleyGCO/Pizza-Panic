from core.entities.Objeto import Objeto
from core.entities.Personagem import Personagem

class PontuacaoService:
    def coletar_item(self, personagem, item):
        if isinstance(item, Objeto):
            pontuacao = item.pontuacao()
        if isinstance(personagem, Personagem):
            personagem.coletar_item(pontuacao)

    def pegar_itens_coletados(self, personagem):
        if isinstance(personagem, Personagem):
            return personagem.pegar_itens_coletados()
        
    def contar_pedido(self, fase, item):
        if item.tipo == "pizza":
            return fase.adicionar_pedido_coletado()