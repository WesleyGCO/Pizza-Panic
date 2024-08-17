from adapters.primary.use_cases import gerenciar_personagem
from core.interfaces.PersonagemInterface import PersonagemInterface
from core.services import pontuacao_service

class PersonagemService(PersonagemInterface):
    def __init__(self):
        self.pontuacao_service = pontuacao_service

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        return gerenciar_personagem.criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao)

    def desenhar_personagem(self, personagem):
        return gerenciar_personagem.desenhar_personagem(personagem)

    def coletar_item(self, personagem, item):
        self.pontuacao_service.coletar_item(personagem, item)

    def pegar_itens_coletados(self, personagem):
        return self.pontuacao_service.pegar_itens_coletados(personagem)