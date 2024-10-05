
from adapters.primary.use_cases import gerenciar_personagem
from core.interfaces.PersonagemInterface import PersonagemInterface
from core.services import pontuacao_servico

class PersonagemService(PersonagemInterface):
    def __init__(self):
        self.pontuacao_servico = pontuacao_servico

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        return gerenciar_personagem.criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao)

    def desenhar_personagem(self, personagem, imagens):
        return gerenciar_personagem.desenhar_personagem(personagem, imagens)

    def adicionar_pontuacao(self, personagem, item):
        self.pontuacao_servico.adicionar_pontuacao(personagem, item)