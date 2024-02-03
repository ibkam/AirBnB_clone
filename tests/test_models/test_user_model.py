#!/usr/bin/python3
"""Defines Test Cases for User Class"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):

    def test_User_inheritance(self):
        """Checks is User Class inherits from BaseModel"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        """Check is User class attributes exist"""
        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())


if __name__ == '__main__':
    unittest.main()
