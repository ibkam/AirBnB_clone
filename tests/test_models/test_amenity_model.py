#!/usr/bin/python3
"""Defines Test Cases Amenity class"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):

    def test_Amenity_inheritence(self):
        """Checks if Amenity Class inherits BaseModel"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Checks inf Amenity attributes exist"""
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())


if __name__ == '__main__':
    unittest.main()
