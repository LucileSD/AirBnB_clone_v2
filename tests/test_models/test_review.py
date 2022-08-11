#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pycodestyle


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_id(self):
        """ """
        new = self.value(place_id="srh544775srg")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value(user_id="rhq5475herh")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value(text="super")
        self.assertEqual(type(new.text), str)
