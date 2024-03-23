from entities.Personagem import Personagem

class Personagem_Servico:

    def criar_personagem(self, tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio):
        personagemCriado = Personagem((237, 14, 178), int(posicao_x_ratio * tela_altura), int(posicao_y_ratio * tela_largura), 40, 40, 5)
        return personagemCriado
    
    def desenhar_personagem(self, personagemDesenho, tela):
        if isinstance(personagemDesenho, Personagem):
            personagemDesenho.desenhar(tela)

    def andar_esquerda(self, personagem):
        if isinstance(personagem, Personagem): 
            personagem.andar_esquerda()
    
    def andar_direita(self, personagem, tela_altura):
        if isinstance(personagem, Personagem):
            personagem.andar_direita(tela_altura)
    
    def coletar_item(self, personagem):
        if isinstance(personagem, Personagem):
            personagem.coletar_item()

    def pegar_itens_coletados(self, personagem):
        if isinstance(personagem, Personagem):
            return personagem.pegar_itens_coletados()