#!/usr/bin/python3
"""Defines Test Cases for State Class"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateModel(unittest.TestCase):

    def test_State_inheritence(self):
        """Checks if State Class inherits BaseModel"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """Checks if State attrubutes exist"""
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())


if __name__ == '__main__':
    unittest.main()
