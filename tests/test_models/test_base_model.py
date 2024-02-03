#!/usr/bin/python3
"""Defines Test Cases for the BaseModel"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest):

    def setUp(self):
        """Intialiaze BaseModel instance"""
        self.my_model = BaseModel()
        self.my_model.name = "Test Case"

    def tearDown(self):
        """Deleting BaseModel instance"""
        del self.my_model

    def test_name(self):
        """Checks if an attribute can be added"""
        self.assertEqual("Test Case", self.my_model.name)

    def test_id_type(self):
        """Checks if the type of id is str"""
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_save(self):
        """Checks if it updates datetime accordingly"""
        old = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old)

    def test_ids_differ(self):
        """Checks is ids between different instances are different"""
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_to_dict_type(self):
        """Checks the to_dict method type"""
        dict_type = str(type(self.my_model.to_dict()))
        self.assertEqual("<class 'dict'>", dict_type)

    def test_to_dict_class(self):
        """Checks if __class__ exists as a key"""
        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        """Checks type of value of updated_at"""
        value_type = str(type((self.my_model.to_dict())["updated_at"]))
        self.assertEqual("<class 'str'>", value_type)

    def test_to_dict_type_created_at(self):
        """"Checks type of value of created_at"""
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))


if __name__ == '__main__':
    unittest.main()
