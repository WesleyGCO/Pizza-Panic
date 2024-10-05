
from config.config import carregar_configuracoes
from core.services.jogo_servico import JogoService


def main():
    configuracoes = carregar_configuracoes()

    jogo_servico = JogoService(configuracoes)

    jogo_servico.iniciar_jogo()

if __name__ == "__main__":
    main()