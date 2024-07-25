from core.entities.Objeto import Objeto
from core.entities.Personagem import Personagem
from core.entities.Pizza import Pizza
from core.interfaces.PersonagemInterface import PersonagemInterface

class PersonagemServiceImpl(PersonagemInterface):
    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio, aceleracao):
        personagemCriado = Personagem(0, int(posicao_x_ratio * tela_altura), int(posicao_y_ratio * tela_largura), 100, 100, aceleracao)
        return personagemCriado
    
    def desenhar_personagem(self, personagemDesenho, tela):
        if isinstance(personagemDesenho, Personagem):
            personagemDesenho.desenhar(tela)

    def andar_esquerda(self, personagem, tempo, aceleracao):
        if isinstance(personagem, Personagem): 
            personagem.atualiza_mov_esquerda(tempo, aceleracao)
    
    def andar_direita(self, personagem, tempo, aceleracao, w_max):
        if isinstance(personagem, Personagem):
            personagem.atualiza_mov_direita(tempo, aceleracao, w_max)
    
    def coletar_item(self, personagem, item):
        if isinstance(item, Objeto):
            pontuacao = item.pontuacao()
        if isinstance(personagem, Personagem):
            personagem.coletar_item(pontuacao)

    def pegar_itens_coletados(self, personagem):
        if isinstance(personagem, Personagem):
            return personagem.pegar_itens_coletados()
        
    def contar_pedido(self, fase, item):
        if isinstance(item, Pizza):
            return fase.adicionar_pedido_coletado()