#!/usr/bin/python3
"""Define Test Cases for City Model"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityModel(unittest.TestCase):

    def test_City_inheritance(self):
        """Checks is City class inherits from BaseModel class"""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_City_attributes(self):
        """Checks if City class attributes exists"""
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())


if __name__ == '__main__':
    unittest.main()
