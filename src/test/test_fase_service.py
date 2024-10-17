import unittest
from unittest.mock import Mock, Mock, patch
import sys
import os

from core.services.tempo_servico import TempoService

# Adiciona o caminho 'src' ao sys.path para permitir importações de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import Mock, patch
from application.models.Personagem import Personagem
from adapters.primary.pygame_input_adapter import capturar_tecla
from core.services.personagem_servico import PersonagemService
from core.services.item_servico import ItemService
from core.services.fase_servico import FaseService
from application.models.Sprites import Sprites
from adapters.primary.pygame_output_adapter import criar_relogio

class TestFaseService(unittest.TestCase):

    def setUp(self):
        # Mock dependencies
        self.fase_model = Mock()
        self.fase_ui = Mock()
        self.item_servico = Mock()
        self.personagem_servico = Mock()
        self.tempo_servico = Mock()
        self.jogo_model = Mock()

        # Configurações do personagem mockado
        self.fase_model.personagem = Mock(spec=Personagem)
        self.fase_model.personagem.velocidade = Mock()
        self.fase_model.personagem.posicao = Mock()
        
        # Definindo valores iniciais para o personagem mockado
        self.fase_model.personagem.velocidade.x = 0
        self.fase_model.personagem.posicao.x = 100

        # Mock da lista de itens ruins
        self.fase_model.itens_ruins = [Mock()]

        # Configurações para fase model
        self.fase_model.concluida = False
        self.fase_model.perdida = False

        # Mock do sprite
        self.sprites = Mock(spec=Sprites)

        with patch('adapters.primary.pygame_output_adapter.criar_relogio') as mock_criar_relogio:
            mock_relogio = Mock()
            mock_criar_relogio.return_value = mock_relogio
            self.fase_service = FaseService(self.fase_model, self.fase_ui, self.item_servico, 
                                            self.personagem_servico, self.tempo_servico, 
                                            self.jogo_model, 800, 600)
            self.fase_service.sprites = self.sprites
            self.fase_service.relogio = mock_relogio


    @patch('adapters.primary.pygame_input_adapter.capturar_eventos')
    @patch('adapters.primary.pygame_input_adapter.eh_sair')
    def test_iniciar(self, mock_eh_sair, mock_capturar_eventos):
        # Testa o método iniciar, mockando as dependências
        mock_capturar_eventos.return_value = []
        mock_eh_sair.return_value = False
        self.fase_service.is_running = False

        self.fase_service = Mock()

        self.assertTrue(self.fase_service.is_running)
        self.fase_model.personagem.processamento_fisica = Mock()

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_esquerda(self, mock_capturar_tecla):
        # Testa movimentação para a esquerda
        mock_capturar_tecla.return_value = {'esquerda': True, 'direita': False}

        self.fase_service.lidar_entrada()

        self.assertEqual(self.fase_service.ultima_posicao, 'esquerda')
        self.assertEqual(self.fase_model.personagem.velocidade.x, -500)

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_direita(self, mock_capturar_tecla):
        # Testa movimentação para a direita
        mock_capturar_tecla.return_value = {'esquerda': False, 'direita': True}

        self.fase_service.lidar_entrada()

        self.assertEqual(self.fase_service.ultima_posicao, 'direita')
        self.assertEqual(self.fase_model.personagem.velocidade.x, 500)

    @patch('adapters.primary.pygame_input_adapter.capturar_tecla')
    def test_lidar_entrada_parado(self, mock_capturar_tecla):
        # Testa se o personagem para quando nenhuma tecla é pressionada
        mock_capturar_tecla.return_value = {'esquerda': False, 'direita': False}

        self.fase_service.ultima_posicao = 'esquerda'
        self.fase_service.lidar_entrada()

        self.assertEqual(self.fase_model.personagem.velocidade.x, 0)
        self.assertEqual(self.fase_service.sprite_atual, self.sprites.get_personagem_sprite_esquerda_parado())

    def test_atualizar_fase_concluida(self):
        # Testa o cenário de fase concluída
        self.fase_model.concluida = True
        self.fase_service.atualizar()

        self.assertFalse(self.fase_service.is_running)

    def test_atualizar_fase_perdida(self):
        # Testa o cenário de fase perdida
        self.fase_model.perdida = True
        self.fase_service.atualizar()

        self.assertFalse(self.fase_service.is_running)

    def test_contar_pedido(self):
        # Testa a contagem de pedidos coletados
        item = Mock()
        item.tipo = "pizza"
        self.fase_service.contar_pedido(self.fase_model, item)

        self.fase_model.adicionar_pedido_coletado.assert_called()

    def test_colisao_item(self):
        # Testa a lógica de colisão com um item
        item = self.fase_model.itens_ruins[0]
        self.item_servico.checa_colisao.return_value = True

        self.fase_service.atualizar()

        self.personagem_servico.adicionar_pontuacao.assert_called_with(self.fase_model.personagem, item)
        self.item_servico.reinicia_item.assert_called_with(item)

if __name__ == '__main__':
    unittest.main()
