from adapters.implementations.JogoServiceImpl import JogoServiceImpl
from config.config import load_settings

def main():

  settings = load_settings()
  # Cria uma instância da classe Jogo
  jogo_service = JogoServiceImpl(settings)

  jogo_service.iniciar_jogo(jogo_service)

if __name__ == "__main__":
  main()
