#!/usr/bin/python3
"""Defines Test Cases for Review Class"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewModel(unittest.TestCase):

    def test_Review_inheritance(self):
        """Checks is Review Class inherits from BaseModel"""
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """Checks if Review Class attribute exit"""
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())


if __name__ == '__main__':
    unittest.main()
