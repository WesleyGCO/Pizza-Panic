from adapters.implementations.PontuacaoService import PontuacaoService
from core.entities.Personagem import Personagem
from core.interfaces.PersonagemInterface import PersonagemInterface

class PersonagemServiceImpl(PersonagemInterface):
    def __init__(self):
        self.regra_pontuacao = PontuacaoService()

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        personagem_criado = Personagem(0, int(posicao_x_ratio * tela_altura), int(posicao_y_ratio * tela_largura), 100, 100, aceleracao)
        return personagem_criado
    
    def desenhar_personagem(self, personagem_desenho, tela):
        if isinstance(personagem_desenho, Personagem):
            personagem_desenho.desenhar(tela)

    def andar_esquerda(self, personagem, tempo, aceleracao):
        if isinstance(personagem, Personagem): 
            personagem.atualiza_mov_esquerda(tempo, aceleracao)
    
    def andar_direita(self, personagem, tempo, aceleracao, w_max):
        if isinstance(personagem, Personagem):
            personagem.atualiza_mov_direita(tempo, aceleracao, w_max)
    
    def coletar_item(self, personagem, item):
        self.regra_pontuacao.coletar_item(personagem, item)

    def pegar_itens_coletados(self, personagem):
        if isinstance(personagem, Personagem):
            return personagem.pegar_itens_coletados()
        
    def contar_pedido(self, fase, item):
        if item.tipo == "pizza":
            return fase.adicionar_pedido_coletado()
