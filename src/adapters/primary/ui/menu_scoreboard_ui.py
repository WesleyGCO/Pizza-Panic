from adapters.primary import pygame_input_adapter, pygame_output_adapter

class MenuScoreboardUI:
    def __init__(self, tela_altura, tela_largura):
        self.tela_largura = tela_largura
        self.tela_altura = tela_altura
        self.pontuacoes = []  # Lista para armazenar pontuações
        self.carregar_pontuacoes()  # Carrega pontuações do arquivo

        # Configuração do botão "Voltar ao menu"
        botao_largura = 200
        botao_altura = 50
        botao_posicao_x = (tela_largura - botao_largura) // 2
        botao_posicao_y = int(tela_altura * 0.75)
        self.botao_voltar_menu = pygame_output_adapter.criar_retangulo(botao_posicao_x, botao_posicao_y, botao_largura, botao_altura)
        self.cor_botao_hover = (15, 99, 245)
        self.cor_botao_normal = (5, 40, 97)

    def carregar_pontuacoes(self):
        try:
            with open('pontuacoes.txt', 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha:  # Verifica se a linha não está vazia
                        partes = linha.split(' - ')
                        if len(partes) == 2:  # Verifica se existem duas partes
                            nome = partes[0].split(': ')[1]  # Extrai o nome
                            pontos = int(partes[1].split(': ')[1])  # Extrai os pontos e converte para inteiro
                            self.pontuacoes.append((nome, pontos))  # Armazena como tupla (nome, pontos)
            self.pontuacoes.sort(key=lambda x: x[1], reverse=True)  # Ordena por pontos, do maior para o menor
        except FileNotFoundError:
            self.pontuacoes = []  # Se o arquivo não existir, inicializa como lista vazia
        except Exception as e:
            print(f"Ocorreu um erro ao carregar as pontuações: {e}")  # Adiciona um tratamento genérico de erros

    def renderizar_scoreboard(self):
        # Exibir título
        texto_scoreboard = pygame_output_adapter.renderizar_texto("Scoreboard")
        largura_texto_sb, altura_texto_sb = texto_scoreboard.get_size()
        posicao_x_texto_sb = (self.tela_largura - largura_texto_sb) // 2
        posicao_y_texto_sb = int(self.tela_altura * 0.1)
        pygame_output_adapter.desenhar_superficie(texto_scoreboard, (posicao_x_texto_sb, posicao_y_texto_sb))

        # Exibir pontuações
        for i, (nome, pontos) in enumerate(self.pontuacoes):
            texto_pontuacao = pygame_output_adapter.renderizar_texto(f"{i + 1}. Nome: {nome} - Pontos: {pontos}")
            posicao_y_texto = posicao_y_texto_sb + 50 + i * 30  # Espaçamento entre as pontuações
            pygame_output_adapter.desenhar_superficie(texto_pontuacao, (posicao_x_texto_sb, posicao_y_texto))

        # Desenhar o botão "Voltar ao menu"
        mouse_pos = pygame_input_adapter.mouse_posicao()
        cor_atual = self.cor_botao_hover if self.botao_voltar_menu.collidepoint(mouse_pos) else self.cor_botao_normal
        pygame_output_adapter.desenhar_botao_retangulo(cor_atual, self.botao_voltar_menu)
        texto_botao = pygame_output_adapter.renderizar_texto("Voltar ao menu")
        largura_texto, altura_texto = texto_botao.get_size()
        posicao_x_texto = self.botao_voltar_menu.x + (self.botao_voltar_menu.width - largura_texto) // 2
        posicao_y_texto = self.botao_voltar_menu.y + (self.botao_voltar_menu.height - altura_texto) // 2
        pygame_output_adapter.desenhar_superficie(texto_botao, (posicao_x_texto, posicao_y_texto))

    def lidar_entrada_menu_scoreboard(self, evento):
        
        """Lida com a entrada do jogador na tela do scoreboard."""
        if pygame_input_adapter.clicado(evento) and self.botao_voltar_menu.collidepoint(evento.pos):
            return "Voltar ao menu"
