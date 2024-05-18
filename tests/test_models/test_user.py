#!/usr/bin/python3
"""Defines unittests for models/user.py.

Test classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User
import models


class TestUserInstantiation(unittest.TestCase):
    """Test cases for the instantiation of the User class."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(User(), User)

    def test_instance_stored_in_storage(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(User().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_email_is_class_attribute(self):
        self.assertIsInstance(User.email, str)

    def test_password_is_class_attribute(self):
        self.assertIsInstance(User.password, str)

    def test_first_name_is_class_attribute(self):
        self.assertIsInstance(User.first_name, str)

    def test_last_name_is_class_attribute(self):
        self.assertIsInstance(User.last_name, str)

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn(f"'id': '{user.id}'", user_str)
        self.assertIn(f"'created_at': {repr(dt)}", user_str)
        self.assertIn(f"'updated_at': {repr(dt)}", user_str)

    def test_unused_args(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Test cases for the save method of the User class."""

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
        user = User()
        sleep(0.05)
        prev_updated_at = user.updated_at
        user.save()
        self.assertGreater(user.updated_at, prev_updated_at)

    def test_multiple_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertGreater(second_updated_at, first_updated_at)
        sleep(0.05)
        user.save()
        self.assertGreater(user.updated_at, second_updated_at)

    def test_save_with_arg_raises_typeerror(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        user_id = f"User.{user.id}"
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Test cases for the to_dict method of the User class."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(User().to_dict(), dict)

    def test_to_dict_has_correct_keys(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)

    def test_to_dict_includes_added_attrs(self):
        user = User()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertIn("middle_name", user.to_dict())
        self.assertIn("my_number", user.to_dict())

    def test_datetime_attrs_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_to_dict_not_equal_to_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg_raises_typeerror(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()

