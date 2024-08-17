import pygame #type: ignore

def iniciar():
    pygame.init()

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

def desenhar_item(item):
    tela = retornar_tela()
    return tela.blit(redimensionar_imagem(item.imagem, item.largura, item.altura), (item.posicao.x, item.posicao.y))

def desenhar_personagem(personagem):
    tela = retornar_tela()
    return tela.blit(redimensionar_imagem(personagem.imagem_pizzaiolo, personagem.largura, personagem.altura), (personagem.posicao.x, personagem.posicao.y))
    
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