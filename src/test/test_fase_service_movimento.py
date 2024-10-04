import unittest
from unittest.mock import Mock, patch
import sys
import os

# Adiciona o caminho 'src' ao sys.path para permitir importações de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import Mock, patch
from application.models.Personagem import Personagem
from adapters.primary.pygame_input_adapter import capturar_tecla
from core.services.personagem_service import PersonagemService
from core.services.item_service import ItemService
from core.services.fase_service import FaseService
from application.models.Sprites import Sprites


class TestFaseServiceMovimento(unittest.TestCase):

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_direita(self, mock_capturar_tecla):
        # Criação dos mocks para FaseService e suas dependências
        fase_model = Mock()
        fase_ui = Mock()
        item_service = Mock(spec=ItemService)
        personagem_service = Mock(spec=PersonagemService)
        jogo_model = Mock()
        sprites = Mock(spec=Sprites)

        # Configura o mock do personagem e inicializa posição e velocidade
        fase_model.personagem = Mock(spec=Personagem)
        fase_model.personagem.posicao = Mock()  # Mock para a posição do personagem
        fase_model.personagem.velocidade = Mock()  # Mock para a velocidade do personagem
        fase_model.personagem.posicao.x = 10  # Define a posição inicial x do personagem

        # Simula o comportamento de teclas pressionadas (tecla direita)
        mock_capturar_tecla.return_value = {'direita': True, 'esquerda': False}

        fase_service = FaseService(
            fase_model, fase_ui, item_service, personagem_service, jogo_model)
        fase_service.sprites = sprites

        fase_service.lidar_entrada()

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_esquerda(self, mock_capturar_tecla):
        fase_model = Mock()
        fase_ui = Mock()
        jogo_model = Mock()
        item_service = Mock(spec=ItemService)
        personagem_service = Mock(spec=PersonagemService)
        sprites = Mock(spec=Sprites)


        fase_model.personagem = Mock(spec=Personagem)
        fase_model.personagem.posicao = Mock()
        fase_model.personagem.velocidade = Mock()
        fase_model.personagem.posicao.x = 10

        mock_capturar_tecla.return_value = {'direita': False, 'esquerda': True}

        fase_service = FaseService(
            fase_model, fase_ui, item_service, personagem_service, jogo_model)
        fase_service.sprites = sprites

        fase_service.lidar_entrada()
        
        self.assertEqual(fase_model.personagem.velocidade.x, -500)

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_parado(self, mock_capturar_tecla):

        fase_model = Mock()
        fase_ui = Mock()
        jogo_model = Mock()
        item_service = Mock(spec=ItemService)
        personagem_service = Mock(spec=PersonagemService)
        sprites = Mock(spec=Sprites)
        
        mock_capturar_tecla.return_value = {
            'esquerda': False, 'direita': False}

        # Configura o mock do personagem corretamente
        personagem_mock = Mock(spec=Personagem)
        personagem_mock.posicao = Mock()
        personagem_mock.velocidade = Mock()
        personagem_mock.posicao.x = 10

        fase_service = FaseService(
            fase_model, fase_ui, item_service, personagem_service, jogo_model)
        fase_service.sprites = sprites

        fase_model.personagem = personagem_mock
        fase_service.lidar_entrada()

        # Verifica se a velocidade do personagem foi ajustada para zero
        self.assertEqual(
            fase_service.fase_model.personagem.velocidade.x, 0)


if __name__ == '__main__':
    # Executa os testes unitários
    unittest.main()
