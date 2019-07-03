#!/usr/bin/python3
""" unit test for class FileStorage """

import models
import unittest
from json import load
from os.path import exists
from os import remove

FileStorage = models.engine.file_storage.FileStorage
BaseModel = models.base_model.BaseModel
file_path = "objects.json"


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_module(self):
        """ validate documentation module """
        doc = models.engine.file_storage.__doc__
        assert doc is not None

    def test_doc_class(self):
        """ validate documentation class """
        doc = FileStorage.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ validate documentation methods """
        l_meth = ["all", "new", "save", "reload"]
        for key in FileStorage.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None


class TestFileStorageInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    def setUp(self):
        """create object new BaseModel and FileStorage """
        self.new_model = BaseModel()
        self.storage = FileStorage()

    def test_mehotd_new(self):
        """ validate created instance """
        self.assertIsInstance(self.storage, FileStorage)

    def test_method_all(self):
        """ validate return all objects """
        id_object = self.new_model.id
        cl_nm = self.new_model.__class__.__name__
        cl_id = cl_nm + "." + id_object
        objects = self.storage.all()
        flag = 0
        if cl_id in objects:
            flag = 1
        self.assertEqual(1, flag)

    def test_method_save(self):
        """ validate save method """
        remove(file_path)
        self.new_model.save()
        id_object = self.new_model.id
        cl_nm = self.new_model.__class__.__name__
        cl_id = cl_nm + "." + id_object
        if(exists(file_path)):
            with open(file_path, "r") as fil:
                dict_obj = load(fil)
        flag = 0
        if cl_id in dict_obj:
            flag = 1
        self.assertEqual(1, flag)

    def test_add_attributes(self):
        """ add attributes to object"""
        self.new_model.name = "Holberton"
        self.new_model.my_number = 98
        list_att = [self.new_model.name, self.new_model.my_number]
        expected = ["Holberton", 98]
        self.assertEqual(expected, list_att)

    def test_method_to_dict(self):
        self.new_model.name = "Holberton"
        self.new_model.my_number = 98
        dict_rep = self.new_model.to_dict()
        list_att = ['id', 'created_at', 'updated_at',
                    'name', 'my_number', '__class__']
        num_att = 0
        for att in dict_rep.keys():
            if att in list_att:
                num_att += 1
        self.assertTrue(6 == num_att)

    def test_method_reload(self):
        self.storage.reload()
        dict_obj = self.storage.all()
        self.assertTrue(len(dict_obj) > 0)


if __name__ == '__main__':
    unittest.main()
