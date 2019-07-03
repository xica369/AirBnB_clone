#!/usr/bin/python3
""" unit test for class FileStorage """

import models
import unittest
from os import exists, remove

FileStorage = models.engine.file_storage.FileStorage
BaseModel = models.base_model.BaseModel


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

    def test_create_object(self):
        """ validate created instance """
        self.assertIsInstance(self.storage, FileStorage)

    def test_method_all(self):
        """ validate return all objects """
        id_object =  self.new_model.id
        objects =  storage.all()
        for key in objects.keys():
            self.assertTrue(id_object in key)

    def test_method_save(self):
        """ validate save method """
        os.remove(File_storage.__file_path)
        self.new_model.save()
        id_object = self.new_model.id
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dict_obj = load(fil)
        for key in dict_obj.keys():
            self.assertTrue(id_object in key)

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

if __name__ == '__main__':
    unittest.main()
