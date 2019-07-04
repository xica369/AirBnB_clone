#!/usr/bin/python3
""" unit test for class Place """

from models.place import Place
import unittest
import pep8


class TestPlaceDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = Place.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ validate documentation methods """
        l_meth = ["save", "__init__", "__str__", "to_dict"]
        for key in Place.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None


class TestPlaceInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    @classmethod
    def setUpClass(cls):
        ''' new_place up '''
        cls.new_place = Place()
        cls.new_place.name = "Hotel"
        cls.new_place.save()
        cls.new_place_str = cls.new_place.to_dict()

    def test_create_object(self):
        """ validate created instance """
        self.assertIsInstance(self.new_place, Place)

    def test_string_representation(self):
        """ validate string representation """
        rep_str = str(self.new_place)
        list_att = ['Place', 'id', 'created_at', 'updated_at']
        num_att = 0
        for att in list_att:
            if att in rep_str:
                num_att += 1
        self.assertTrue(4 == num_att)

    def test_method_save(self):
        """ validate save method """
        current = self.new_place.updated_at
        self.new_place.save()
        new = self.new_place.updated_at
        self.assertNotEqual(current, new)

    def test_add_attributes(self):
        """ add attributes to object"""
        self.new_place.name = "Hotel"
        list_att = [self.new_place.name]
        expected = ["Hotel"]
        self.assertEqual(expected, list_att)

    def test_hasMethods(self):
        ''' test the instance have the methods  '''
        self.assertTrue(hasattr(self.new_place, '__str__'))
        self.assertTrue(hasattr(self.new_place, '__init__'))
        self.assertTrue(hasattr(self.new_place, 'to_dict'))
        self.assertTrue(hasattr(self.new_place, 'save'))

    def test_method_to_dict(self):
        self.new_place.name = "Hotel"
        dict_rep = self.new_place.to_dict()
        list_att = ['id', 'created_at', 'updated_at',
                    'name', '__class__']
        num_att = 0
        for att in dict_rep.keys():
            if att in list_att:
                num_att += 1
        self.assertTrue(5 == num_att)

    def test_pep8_conformance(self):
        ''' Test that we conform to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                                        'models/place.py',
                                        'tests/test_models/test_place.py'
                                        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def tearDownClass(cls):
        ''' new_place Down '''
        del cls.new_place
        try:
            os.remove("objects.json")
        except BaseException:
            pass


if __name__ == '__main__':
    unittest.main()
