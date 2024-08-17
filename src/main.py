
from config.config import carregar_configuracoes
from core.services.jogo_service import JogoService


def main():
    configuracoes = carregar_configuracoes()

    jogo_service = JogoService(configuracoes)

    jogo_service.iniciar_jogo()

if __name__ == "__main__":
    main()