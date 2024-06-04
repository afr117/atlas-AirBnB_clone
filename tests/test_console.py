# tests/test_console.py
import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        self.assertEqual(self.console.onecmd("quit"), True)

    def test_EOF(self):
        """Test EOF command"""
        self.assertEqual(self.console.onecmd("EOF"), True)

    def test_emptyline(self):
        """Test empty line input"""
        output = StringIO()
        sys.stdout = output
        self.console.onecmd("")
        self.assertEqual(output.getvalue(), "")
        sys.stdout = sys.__stdout__

    def test_create(self):
        """Test create command"""
        output = StringIO()
        sys.stdout = output
        self.console.onecmd("create BaseModel")
        instance_id = output.getvalue().strip()
        self.assertTrue(len(instance_id) > 0)
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()

