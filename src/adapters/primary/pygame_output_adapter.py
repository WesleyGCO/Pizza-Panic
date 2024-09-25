import pygame, json #type: ignore

with open("settings.json") as f:
    configuracoes = json.load(f)

def iniciar():
    pygame.init()
    pygame.mixer.init()

iniciar()

#region Relacionados a tela

def criar_tela(tamanho):
    return pygame.display.set_mode(tamanho)

def criar_titulo(titulo):
    return pygame.display.set_caption(titulo)

def retornar_tela():
    return pygame.display.get_surface()

def preencher_tela(cor):
    tela = retornar_tela()
    return tela.fill(cor)
    
def preencher_superficie(superficie, cor):
    return superficie.fill(cor)

#endregion Relacionados a tela

#region Criar e Desenhar

def rodar_item(item,angulo):
    imagem = redimensionar_imagem(item.imagem, item.largura, item.altura)
    rotated_image = pygame.transform.rotate(imagem, angulo)
    image_rect = item.imagem.get_rect(center=(item.posicao.x, item.posicao.y))  # Posiciona a imagem no centro da tela
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    tela = retornar_tela()

    return tela.blit(rotated_image,rotated_rect)

def desenhar_item(item,angulo):
    # tela = retornar_tela()
    # return tela.blit(redimensionar_imagem(item.imagem, item.largura, item.altura), (item.posicao.x, item.posicao.y))
    imagem = redimensionar_imagem(item.imagem, item.largura, item.altura)
    rotated_image = pygame.transform.rotate(imagem, angulo)
    image_rect = item.imagem.get_rect(center=(item.posicao.x, item.posicao.y))  # Posiciona a imagem no centro da tela
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    tela = retornar_tela()

    return tela.blit(rotated_image,rotated_rect)

def rotacionar_item(item):
    pass

def desenhar_personagem(personagem,imagens):
    tela = retornar_tela()
    return tela.blit(redimensionar_imagem(imagens, personagem.largura, personagem.altura), (personagem.posicao.x, personagem.posicao.y))
    

def criar_superficie(tamanho):
    return pygame.Surface((tamanho, 50))    

def desenhar_superficie(superficie, posicao):
    tela = retornar_tela()
    return tela.blit(superficie, posicao)

def criar_retangulo(x, y, largura, altura):
    return pygame.Rect(x, y, largura, altura)

def desenhar_botao_retangulo(cor, retangulo):
    tela = retornar_tela()
    return pygame.draw.rect(tela, cor, retangulo)

def desenhar_retangulo(cor, retangulo, num):
    tela = retornar_tela()
    return pygame.draw.rect(tela, cor, retangulo, num)

#endregion Criar e Desenhar

#region Imagem
def carregar_imagem(imagem):
    return pygame.image.load(imagem)

def redimensionar_imagem(imagem, altura, largura):
    return pygame.transform.scale(imagem, (altura, largura))

#endregion Desenhar

#region Geral
def criar_relogio():
    return pygame.time.Clock()

def devolve_tempo():
    return pygame.time.get_ticks()

def sair():
    pygame.quit()

def atualizacao_tela():
    pygame.display.update()
    
def atualizacao_display():
    pygame.display.flip()
    
#endregion Geral

#region Cálculos

def calcular_posicao_x_centralizada(largura_total):
    tela = retornar_tela()
    return (tela.get_width() - largura_total) // 2

def calcular_posicao_y_centralizada_topo():
    return 50 // 2  # 50 é a altura do menu superior

#endregion Cálculos

#region Textos e fonte

fonte_padrao = pygame.font.Font(None, 30)

def renderizar_texto(texto, cor = (255, 255, 255), fonte = fonte_padrao):
    return fonte.render(texto, True, cor)

def renderizar_texto_placar(texto_pedidos, texto_atendidos):
    
    superficie_texto_pedidos = renderizar_texto(texto_pedidos)
    superficie_texto_atendidos = renderizar_texto(texto_atendidos)
    
    # Calcular a largura total dos textos
    largura_total = superficie_texto_pedidos.get_width() + superficie_texto_atendidos.get_width() + 5  # 5 é o espaçamento entre os textos

    # Calcular a posição X centralizada, considerando a borda
    posicao_x_centralizada = calcular_posicao_x_centralizada(largura_total)

    # Calcular a posição Y centralizada na parte superior, considerando a borda e o menu superior
    posicao_y_centralizada = calcular_posicao_y_centralizada_topo()
        
    desenhar_superficie(superficie_texto_pedidos, (posicao_x_centralizada, posicao_y_centralizada))
    desenhar_superficie(superficie_texto_atendidos, (posicao_x_centralizada + superficie_texto_pedidos.get_width() + 20, posicao_y_centralizada))

#endregion Textos e fonte

#region Sons

SONS_DIR = configuracoes['sons']['sons_dir']

# Dicionário de sons
sons = {
    "menu_inicial": pygame.mixer.Sound(SONS_DIR + "musica fundo inicial.mp3"),
    "lancamento": pygame.mixer.Sound(SONS_DIR + "lancamento.mp3"),
    "erro_item": pygame.mixer.Sound(SONS_DIR + "error.mp3"),
    "conclusao_fase": pygame.mixer.Sound(SONS_DIR + "Sucesso fase.mp3")
}

sons["menu_inicial"].set_volume(configuracoes["sons"]["volume_menu_inicial"])

for nome_som, som in sons.items():
    if nome_som != "menu_inicial":  # Ignora o som de fundo, que já teve o volume ajustado
        som.set_volume(configuracoes["sons"]["volume_efeitos"])

def tocar_som(nome_som):
    if nome_som in sons:
        sons[nome_som].play()

def parar_som(nome_som):
    if nome_som in sons:
        sons[nome_som].stop()

#endregion Sons
