from adapters.primary import pygame_input_adapter, pygame_output_adapter
import pygame

from adapters.primary.use_cases import gerenciar_scoreboard

class MenuPerdeuUI:
    def __init__(self, tela_altura, tela_largura, personagem):
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        self.personagem = personagem
        self.nome_jogador = ""  # Nome digitado pelo jogador

        # Configuração do botão "Voltar ao menu"
        botao_largura = 200
        botao_altura = 50
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = int(tela_altura * 0.75)
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

        # Configuração do campo de entrada para o nome do jogador
        campo_nome_largura = 300
        campo_nome_altura = 50
        campo_nome_pos_x = (tela_largura - campo_nome_largura) // 2
        campo_nome_pos_y = int(tela_altura * 0.6)
        self.campo_nome_rect = pygame_output_adapter.criar_retangulo(campo_nome_pos_x, campo_nome_pos_y, campo_nome_largura, campo_nome_altura)
        self.cor_campo_nome = (255, 255, 255)  # Cor de fundo do campo de entrada

    def renderizar_menu_perdeu(self):
        # Exibir "Game Over!"
        texto_game_over = pygame_output_adapter.renderizar_texto("Game Over!")
        largura_texto_go, altura_texto_go = texto_game_over.get_size()
        posicao_x_texto_go = (self.tela_largura - largura_texto_go) // 2
        posicao_y_texto_go = (self.tela_altura - altura_texto_go) // 4
        pygame_output_adapter.desenhar_superficie(texto_game_over, (posicao_x_texto_go, posicao_y_texto_go))

        # Exibir pontuação
        texto_pontuacao = pygame_output_adapter.renderizar_texto(f"Pontuação: {self.personagem.pontuacao_personagem}")
        posicao_y_texto_pontuacao = posicao_y_texto_go + 60
        pygame_output_adapter.desenhar_superficie(texto_pontuacao, (posicao_x_texto_go, posicao_y_texto_pontuacao))

        # Exibir o campo de entrada de nome
        pygame_output_adapter.desenhar_botao_retangulo(self.cor_campo_nome, self.campo_nome_rect)
        texto_nome = pygame_output_adapter.renderizar_texto(self.nome_jogador or "Digite seu nome...", cor=(0, 0, 0))
        largura_texto_nome, altura_texto_nome = texto_nome.get_size()
        posicao_x_texto_nome = self.campo_nome_rect.x + 10  # Espaçamento interno
        posicao_y_texto_nome = self.campo_nome_rect.y + (self.campo_nome_rect.height - altura_texto_nome) // 2
        pygame_output_adapter.desenhar_superficie(texto_nome, (posicao_x_texto_nome, posicao_y_texto_nome))

        # Desenhar o botão "Voltar ao menu" mais abaixo
        mouse_pos = pygame_input_adapter.mouse_posicao()
        cor_atual = self.cor_botao_hover if self.botao_voltar_menu.collidepoint(mouse_pos) else self.cor_botao_normal
        pygame_output_adapter.desenhar_botao_retangulo(cor_atual, self.botao_voltar_menu)
        texto_botao = pygame_output_adapter.renderizar_texto("Voltar ao menu")
        largura_texto, altura_texto = texto_botao.get_size()
        posicao_x_texto = self.botao_voltar_menu.x + (self.botao_voltar_menu.width - largura_texto) // 2
        posicao_y_texto = self.botao_voltar_menu.y + (self.botao_voltar_menu.height - altura_texto) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_perdeu(self, evento):
        tecla_pressionada = pygame_input_adapter.capturar_tecla()
        
        if (pygame_input_adapter.clicado(evento) and self.botao_voltar_menu.collidepoint(evento.pos)):
            return "Voltar ao menu"
        
        if (pygame_input_adapter.teclado(evento)):
            if (tecla_pressionada['backspace']):
                self.nome_jogador = self.nome_jogador[:-1]
                
            elif (tecla_pressionada['enter']):
                gerenciar_scoreboard.salvar_pontuacao(self.nome_jogador, self.personagem.pontuacao_personagem)
                return "Voltar ao menu"
            
            elif len(self.nome_jogador) < 20:  # Limita o nome a 20 caracteres
                self.nome_jogador += pygame_input_adapter.tecla(evento)