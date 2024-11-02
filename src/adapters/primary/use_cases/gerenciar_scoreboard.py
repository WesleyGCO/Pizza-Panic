def salvar_pontuacao(nome_jogador, pontuacao_personagem):
    with open(".\\adapters\\primary\\resources\\pontuacoes.txt", "a") as file:
        file.write(f"Nome: {nome_jogador} - Pontos: {pontuacao_personagem}\n")