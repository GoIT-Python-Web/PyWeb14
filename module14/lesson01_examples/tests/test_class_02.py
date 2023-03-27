import unittest

from src.my_class.main import Cat, Dog, CatDog, DogCat, Animal


class TestExamples(unittest.TestCase):
    def test_dog(self):
        self.assertEqual(Dog.__base__, Animal)

    def test_cat_dog(self):
        assert Dog in CatDog.__bases__, 'Class Dog must be parent for clas CatDog'
        assert 'info' in dir(CatDog), 'Not implemented method info'
