from entities.Personagem import Personagem

class Personagem_Servico:

    def criar_personagem(tela_largura, tela_altura, posicao_x_ratio, posicao_y_ratio):
        personagemCriado = Personagem((237, 14, 178), int(posicao_x_ratio * tela_altura), int(posicao_y_ratio * tela_largura), 40, 40, 5)
        return personagemCriado
    
    def desenhar_personagem(personagemDesenho, tela):
        if isinstance(personagemDesenho, Personagem):
            personagemDesenho.desenhar(tela)

    def andar_esquerda(self):
        Personagem.andar_esquerda()
    
    def andar_direita(self):
        Personagem.andar_direita()
    
    def coletar_item(self):
        Personagem.coletar_item()

    def pegar_itens_coletados(self):
        return Personagem.pegar_itens_coletados()