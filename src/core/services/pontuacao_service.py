from application.models.Objeto import Objeto
from application.models.Personagem import Personagem

def coletar_item(personagem, item):
    if isinstance(item, Objeto):
        pontuacao = item.pontuacao()
    if isinstance(personagem, Personagem):
        personagem.coletar_item(pontuacao)

def pegar_itens_coletados(personagem):
    if isinstance(personagem, Personagem):
        return personagem.pegar_itens_coletados()