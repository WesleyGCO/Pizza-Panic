from entities.Jogo import Jogo

def main():
  # Cria uma instância da classe Jogo
  jogo = Jogo()

  # Inicializa o jogo
  jogo.init()

  # Executa o loop principal do jogo
  jogo.iniciar_menu()

  # Limpa recursos alocados pelo jogo
  jogo.cleanup()


if __name__ == "__main__":
  main()
