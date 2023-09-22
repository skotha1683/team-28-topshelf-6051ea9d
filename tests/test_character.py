from unittest import TestCase
from levelup.character import Character, CharacterType
from levelup.controller import Direction

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_name(self):
        ARBITRARY_NAME = "FooBar"
        testobj = Character(ARBITRARY_NAME)
        result = testobj.getName()
        self.assertEqual(ARBITRARY_NAME, result)

    def test_move(self):
        ARBITRARY_NAME = "Im_Moving"
        testobj = Character(ARBITRARY_NAME)
        result = testobj.move(Direction.WEST)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_character_type(self):
        ARBITRARY_NAME = "MurderHobo"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
        self.assertEqual(CharacterType.Elf, testobj.character_type)


