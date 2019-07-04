#!/usr/bin/python3
""" unit test for class State """

from models.state import State
import unittest
import pep8


class TestStateDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = State.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ validate documentation methods """
        l_meth = ["save", "__init__", "__str__", "to_dict"]
        for key in State.__dict__.keys():
            if key is l_meth:
                doc = key.__doc__
                assert doc is not None


class TestStateInstances(unittest.TestCase):
    """ validate creation objects and use methods """
    @classmethod
    def setUpClass(cls):
        ''' new_state up '''
        cls.new_state = State()
        cls.new_state.name = "Florida"
        cls.new_state.save()
        cls.new_state_str = cls.new_state.to_dict()

    def test_create_object(self):
        """ validate created instance """
        self.assertIsInstance(self.new_state, State)

    def test_string_representation(self):
        """ validate string representation """
        rep_str = str(self.new_state)
        list_att = ['State', 'id', 'created_at', 'updated_at']
        num_att = 0
        for att in list_att:
            if att in rep_str:
                num_att += 1
        self.assertTrue(4 == num_att)

    def test_method_save(self):
        """ validate save method """
        current = self.new_state.updated_at
        self.new_state.save()
        new = self.new_state.updated_at
        self.assertNotEqual(current, new)

    def test_hasMethods(self):
        ''' test the instance have the methods  '''
        self.assertTrue(hasattr(self.new_state, '__str__'))
        self.assertTrue(hasattr(self.new_state, '__init__'))
        self.assertTrue(hasattr(self.new_state, 'to_dict'))
        self.assertTrue(hasattr(self.new_state, 'save'))

    def test_add_attributes(self):
        """ add attributes to object"""
        self.new_state.name = "Florida"
        list_att = [self.new_state.name]
        expected = ["Florida"]
        self.assertEqual(expected, list_att)

    def test_method_to_dict(self):
        self.new_state.name = "Florida"
        dict_rep = self.new_state.to_dict()
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
                                        'models/state.py',
                                        'tests/test_models/test_state.py'
                                        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def tearDownClass(cls):
        ''' new_state Down '''
        del cls.new_state
        try:
            os.remove("objects.json")
        except BaseException:
            pass

if __name__ == '__main__':
    unittest.main()
