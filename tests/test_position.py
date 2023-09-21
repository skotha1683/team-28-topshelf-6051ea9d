from unittest import TestCase
from levelup.position import Position


class TestPosition(TestCase):
    def test_init(self):
        testobj = Position()
        self.assertIsNotNone(testobj)