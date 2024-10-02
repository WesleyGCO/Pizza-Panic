import unittest
# from src.application.models.Personagem import Personagem
# from src.application.models.Sprites import Sprites
# from src.core.services.fase_service import FaseService
from unittest.mock import patch, MagicMock

from application.models.Personagem import Personagem

class TestFaseService(unittest.TestCase):

    @patch('adapters.primary.pygame_input_adapter.capturar_eventos', return_value=[])
    @patch('adapters.primary.pygame_input_adapter.capturar_tecla', return_value={'direita': True, 'esquerda': False})
    def test_lidar_entrada_direita(self, mock_capturar_tecla, mock_capturar_eventos):
        personagem = Personagem()
        personagem.posicao.x = 0
        fase_model = MagicMock()
        fase_model.personagem = personagem
        fase_model.itens_ruins = []
        fase_ui = MagicMock()
        item_service = MagicMock()
        personagem_service = MagicMock()
        
        fase_service = FaseService(fase_model, fase_ui, item_service, personagem_service)
        fase_service.lidar_entrada()
        
        self.assertEqual(fase_model.personagem.velocidade.x, 500)
        self.assertEqual(fase_service.sprite_atual, fase_service.sprites.get_personagem_sprite_direita())

if __name__ == '__main__':
    unittest.main()
