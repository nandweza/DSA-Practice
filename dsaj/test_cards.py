"""Test cards module"""

from unittest import TestCase
import unittest


class TestCards(unittest.TestCase):
    def test_cards(self):
        self.assertEqual('a: [9, 8, 7, 5, 4, 2, 1]', 'b: 5', 3)

    def test_error(self):
        with self.assertRaises(ValueError) as e:
            self.assertEqual()