#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pycodestyle


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_first_name(self):
        """ """
        new = self.value(first_name="Raphael")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(last_name="Chemouni")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(email="raph.du.77@gmail.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(password="1234")
        self.assertEqual(type(new.password), str)
