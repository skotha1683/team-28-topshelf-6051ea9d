from unittest import TestCase
from levelup.controller import Direction
from levelup.player_input_helper import PlayerInputHelper
from unittest.mock import patch

class TestPlayerInputHelper(TestCase):

    response = ""



    @patch('builtins.input', side_effect=['thats all folks'])
    def test_get_input_from_user(self, mock_input):
        pih = PlayerInputHelper()
        result = pih.getInputFromPlayer('Whats up doc')
        self.assertEqual(result, 'thats all folks')

