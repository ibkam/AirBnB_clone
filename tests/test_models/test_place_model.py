#!/usr/bin/python3
"""Defines Test Case for Place Model"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceModel(unittest.TestCase):

    def setUp(self):
        """Create Place Class instance"""
        self.new_place = Place()

    def tearDown(self):
        pass

    def test_Place_inheritance(self):
        """Checks is Place class inherits BaseModel"""
        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        """Checks if Place attributes exist"""
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())
        self.assertTrue("amenity_ids" in self.new_place.__dir__())


if __name__ == '__main__':
    unittest.main()
