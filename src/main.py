from config.config import carregar_configuracoes
from core.services.jogo_servico import JogoService

def main():
    """
    Função principal que inicializa o serviço do jogo.
    
    Esta função carrega as configurações do jogo e inicializa o serviço do jogo com essas configurações.
    Em seguida, o jogo é iniciado.
    
    O fluxo é o seguinte:
    1. Carregar configurações do jogo
    2. Inicializar o serviço do jogo com essas configurações
    3. Iniciar o jogo       
    """
    configuracoes = carregar_configuracoes()

    jogo_servico = JogoService(configuracoes)

    jogo_servico.iniciar_jogo()

if __name__ == "__main__":
    main()