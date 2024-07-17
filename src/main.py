from logic.JogoService import JogoService

def main():
  # Cria uma instância da classe Jogo
  jogo_service = JogoService()

  jogo_service.iniciar_jogo(jogo_service)

if __name__ == "__main__":
  main()
