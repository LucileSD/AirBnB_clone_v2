#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


class test_Amenity(test_basemodel):
    """ """

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value(name="wifi")
        self.assertEqual(isinstance(new.name, str), True)
