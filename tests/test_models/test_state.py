#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State
import models


class TestStateInstantiation(unittest.TestCase):
    """Tests instantiation of the State class."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(State(), State)

    def test_instance_in_storage(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(State().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_name_is_class_attr(self):
        state = State()
        self.assertTrue(hasattr(State, 'name'))
        self.assertNotIn('name', state.__dict__)

    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_different_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        expected_str = f"[State] (123456) {state.__dict__}"
        self.assertEqual(state.__str__(), expected_str)

    def test_unused_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """Tests the save method of the State class."""

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
        state = State()
        sleep(0.05)
        prev_updated_at = state.updated_at
        state.save()
        self.assertGreater(state.updated_at, prev_updated_at)

    def test_multiple_saves(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertGreater(second_updated_at, first_updated_at)
        sleep(0.05)
        state.save()
        self.assertGreater(state.updated_at, second_updated_at)

    def test_save_with_arg_raises_typeerror(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        state = State()
        state.save()
        state_id = f"State.{state.id}"
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class TestStateToDict(unittest.TestCase):
    """Tests the to_dict method of the State class."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(State().to_dict(), dict)

    def test_to_dict_has_correct_keys(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_to_dict_includes_added_attrs(self):
        state = State()
        state.middle_name = "Holberton"
        state.my_number = 98
        self.assertIn("middle_name", state.to_dict())
        self.assertIn("my_number", state.to_dict())

    def test_datetime_attrs_are_strs(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), expected_dict)

    def test_to_dict_not_equal_to_dunder_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg_raises_typeerror(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()

