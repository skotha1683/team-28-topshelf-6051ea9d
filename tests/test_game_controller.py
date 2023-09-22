from contextlib import AbstractContextManager
from typing import Any
from unittest import TestCase
from levelup.controller import GameController

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None

    def test_controller_creates_character(self):
        testObj = GameController()
        result = testObj.create_character("mickey mouse")
        self.assertEqual(testObj.character.name, "mickey mouse")

    def test_controller_sets_running_to_true(self):
        testObj = GameController()
        result = testObj.start_game()
        self.assertTrue(testObj.status.running)

    def test_controller_sets_character_name(self):
        testObj = GameController()
        character_result = testObj.create_character("mickey mouse")
        result = testObj.start_game()
        self.assertTrue(testObj.status.running)
        self.assertEqual(testObj.character.name, "mickey mouse")

        
