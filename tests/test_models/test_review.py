#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review
import models


class TestReviewInstantiation(unittest.TestCase):
    """Tests instantiation of the Review class."""

    def test_instantiates_with_no_args(self):
        self.assertIsInstance(Review(), Review)

    def test_new_instance_in_storage(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(Review().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(Review().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(Review().updated_at, datetime)

    def test_place_id_is_class_attr(self):
        rv = Review()
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertNotIn('place_id', rv.__dict__)

    def test_user_id_is_class_attr(self):
        rv = Review()
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertNotIn('user_id', rv.__dict__)

    def test_text_is_class_attr(self):
        rv = Review()
        self.assertTrue(hasattr(Review, 'text'))
        self.assertNotIn('text', rv.__dict__)

    def test_unique_ids_for_reviews(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_different_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_method(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        expected_str = f"[Review] (123456) {rv.__dict__}"
        self.assertEqual(rv.__str__(), expected_str)

    def test_unused_args(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiates_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Tests the save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_updates_updated_at(self):
        rv = Review()
        sleep(0.05)
        prev_updated_at = rv.updated_at
        rv.save()
        self.assertGreater(rv.updated_at, prev_updated_at)

    def test_multiple_saves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertGreater(second_updated_at, first_updated_at)
        sleep(0.05)
        rv.save()
        self.assertGreater(rv.updated_at, second_updated_at)

    def test_save_with_arg_raises_typeerror(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_file(self):
        rv = Review()
        rv.save()
        rvid = f"Review.{rv.id}"
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReviewToDict(unittest.TestCase):
    """Tests the to_dict method of the Review class."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(Review().to_dict(), dict)

    def test_to_dict_has_correct_keys(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertIn("id", rv_dict)
        self.assertIn("created_at", rv_dict)
        self.assertIn("updated_at", rv_dict)
        self.assertIn("__class__", rv_dict)

    def test_to_dict_includes_added_attrs(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertIn("middle_name", rv.to_dict())
        self.assertIn("my_number", rv.to_dict())

    def test_datetime_attrs_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertIsInstance(rv_dict["created_at"], str)
        self.assertIsInstance(rv_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), expected_dict)

    def test_to_dict_not_equal_to_dunder_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg_raises_typeerror(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()

