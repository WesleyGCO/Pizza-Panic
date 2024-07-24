from adapters.implementations.JogoServiceImpl import JogoServiceImpl

def main():
  # Cria uma instância da classe Jogo
  jogo_service = JogoServiceImpl()

  jogo_service.iniciar_jogo(jogo_service)

if __name__ == "__main__":
  main()
