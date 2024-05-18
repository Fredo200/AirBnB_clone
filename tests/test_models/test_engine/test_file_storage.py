#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
"""
import os
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_is_private_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_storage_initialization(self):
        self.assertIsInstance(models.storage, FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all_returns_dict(self):
        self.assertIsInstance(models.storage.all(), dict)

    def test_all_with_args_raises_typeerror(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        objects = {
            "BaseModel": BaseModel(),
            "User": User(),
            "State": State(),
            "Place": Place(),
            "City": City(),
            "Amenity": Amenity(),
            "Review": Review()
        }
        for key, obj in objects.items():
            models.storage.new(obj)
            self.assertIn(f"{key}.{obj.id}", models.storage.all())
            self.assertIn(obj, models.storage.all().values())

    def test_new_with_args_raises_typeerror(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_none_raises_attributeerror(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        objects = {
            "BaseModel": BaseModel(),
            "User": User(),
            "State": State(),
            "Place": Place(),
            "City": City(),
            "Amenity": Amenity(),
            "Review": Review()
        }
        for obj in objects.values():
            models.storage.new(obj)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            for key, obj in objects.items():
                self.assertIn(f"{key}.{obj.id}", save_text)

    def test_save_with_args_raises_typeerror(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        objects = {
            "BaseModel": BaseModel(),
            "User": User(),
            "State": State(),
            "Place": Place(),
            "City": City(),
            "Amenity": Amenity(),
            "Review": Review()
        }
        for obj in objects.values():
            models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        for key, obj in objects.items():
            self.assertIn(f"{key}.{obj.id}", objs)

    def test_reload_with_args_raises_typeerror(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

