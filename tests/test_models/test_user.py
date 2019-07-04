#!/usr/bin/python3
""" unit test for class BaseModel """

from models.user import User
import unittest
import pep8


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = User.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ validate documentation methods """
        l_meth = ["save", "__init__", "__str__", "to_dict"]
        for key in User.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None


class TestBaseModelInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    @classmethod
    def setUpClass(cls):
        ''' new_user up '''
        cls.new_user = User()
        cls.new_user.first_name = "Betty"
        cls.new_user.last_name = "Holberton"
        cls.new_user.email = "airbnb@holberton.com"
        cls.new_user.password = "root"
        cls.new_user.save()
        cls.new_user_str = cls.new_user.to_dict()

    def test_create_object(self):
        """ validate created instance """
        self.assertIsInstance(self.new_user, User)

    def test_string_representation(self):
        """ validate string representation """
        rep_str = str(self.new_user)
        list_att = ['User', 'id', 'created_at', 'updated_at']
        num_att = 0
        for att in list_att:
            if att in rep_str:
                num_att += 1
        self.assertTrue(4 == num_att)

    def test_method_save(self):
        """ validate save method """
        current = self.new_user.updated_at
        self.new_user.save()
        new = self.new_user.updated_at
        self.assertNotEqual(current, new)

    def test_hasMethods(self):
        ''' test the instance have the methods  '''
        self.assertTrue(hasattr(self.new_user, '__str__'))
        self.assertTrue(hasattr(self.new_user, '__init__'))
        self.assertTrue(hasattr(self.new_user, 'to_dict'))
        self.assertTrue(hasattr(self.new_user, 'save'))

    def test_add_attributes(self):
        """ add attributes to object"""
        self.new_user.first_name = "Jhon"
        self.new_user.last_name = "Doe"
        list_att = [self.new_user.first_name, self.new_user.last_name]
        expected = ["Jhon", "Doe"]
        self.assertEqual(expected, list_att)

    def test_method_to_dict(self):
        self.new_user.first_name = "Jhon"
        self.new_user.last_name = "Doe"
        dict_rep = self.new_user.to_dict()
        list_att = ['id', 'created_at', 'updated_at',
                    'first_name', 'last_name', '__class__']
        num_att = 0
        for att in dict_rep.keys():
            if att in list_att:
                num_att += 1
        self.assertTrue(6 == num_att)

    def test_pep8_conformance(self):
        ''' Test that we conform to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                                        'models/user.py',
                                        'tests/test_models/test_user.py'
                                        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def tearDownClass(cls):
        ''' new_user Down '''
        del cls.new_user
        try:
            os.remove("file.json")
        except BaseException:
            pass


if __name__ == '__main__':
    unittest.main()
