#!/usr/bin/python3
""" unit test for class BaseModel """

import models
import unittest

BaseModel = models.base_model.BaseModel

class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_module(self):
        doc = models.base_model.__doc__
        assert doc is not None

    def test_doc_class(self):
        doc = BaseModel.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        l_meth = ["save", "__init__", "__str__", "to_dict"]
        for key in  BaseModel.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None

class TestBaseModelInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    def test_create_object(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model,BaseModel)



if __name__ == '__main__':
    unittest.main()
