#!/usr/bin/python3
""" unit test for class BaseModel """

import models
import unittest

BaseModel = models.base_model.BaseModel
Review = models.review.Review

class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_module(self):
        """ validate documentation module """
        doc = models.review.__doc__
        assert doc is not None

    def test_doc_class(self):
        """ validate documentation class """
        doc = Review.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ validate documentation methods """
        l_meth = ["save", "__init__", "__str__", "to_dict"]
        for key in Review.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None


class TestBaseModelInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    def setUp(self):
        """create object new BaseModel """
        self.new_review = Review()

    def test_create_object(self):
        """ validate created instance """
        self.assertIsInstance(self.new_review, Review)

    def test_string_representation(self):
        """ validate string representation """
        rep_str = str(self.new_review)
        list_att = ['Review', 'id', 'created_at', 'updated_at']
        num_att = 0
        for att in list_att:
            if att in rep_str:
                num_att += 1
        self.assertTrue(4 == num_att)

    def test_method_save(self):
        """ validate save method """
        current = self.new_review.updated_at
        self.new_review.save()
        new = self.new_review.updated_at
        self.assertNotEqual(current, new)

    def test_add_attributes(self):
        """ add attributes to object"""
        self.new_review.text = "Comments"
        list_att = [self.new_review.text]
        expected = ["Comments"]
        self.assertEqual(expected, list_att)

    def test_method_to_dict(self):
        self.new_review.text = "Comments"
        dict_rep = self.new_review.to_dict()
        list_att = ['id', 'created_at', 'updated_at',
                    'text', '__class__']
        num_att = 0
        for att in dict_rep.keys():
            if att in list_att:
                num_att += 1
        self.assertTrue(5 == num_att)

if __name__ == '__main__':
    unittest.main()
