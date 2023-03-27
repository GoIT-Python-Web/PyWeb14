import unittest
from unittest.mock import mock_open, patch

from src.method.main import read_contacts_from_file, write_contacts_to_file


class TestMethod(unittest.TestCase):
    contacts = [{'name': 'Andriy', 'age': 26}, {'name': 'Olga', 'age': 16}]
    mock_open_file = mock_open()

    @patch('json.dump')
    @patch('builtins.open', mock_open_file)
    def test_write(self, dump_mock):
        write_contacts_to_file('fake.json', self.contacts)
        self.mock_open_file.assert_called_with('fake.json', 'w')
        dump_mock.assert_called()
        dump_mock.assert_called_with({"contacts": self.contacts}, self.mock_open_file())

    @patch('json.load')
    @patch('builtins.open', mock_open_file)
    def test_read(self, load_mock):
        load_mock.return_value = {"contacts": self.contacts}
        result = read_contacts_from_file('fake.json')
        self.mock_open_file.assert_called_with('fake.json', 'r')
        load_mock.assert_called()
        load_mock.assert_called_with(self.mock_open_file())
        self.assertListEqual(result, self.contacts)
