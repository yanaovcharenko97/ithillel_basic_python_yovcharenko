import unittest
from unittest.mock import patch
from io import StringIO
from __main__ import Phonebook, Contact


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook(file_name="test_phonebook.json",
                                   verbose=True)

    def tearDown(self):
        self.phonebook = None

    def test_print_phonebook(self):
        # Add some test data to the phone book
        test_contact_1 = Contact(
            "Doe", "John", 30, "+1234567890", "johndoe@example.com")
        test_contact_2 = Contact(
            "Smith", "Jane", 25, "+0987654321", "janesmith@example.com")
        self.phonebook.phone_book = [test_contact_1, test_contact_2]

        # Redirect stdout to a buffer, so we can capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.print_phonebook()
            expected_output = "\n\n#########  Phone book  ##########\n"
            expected_output += "1: John Doe, 30 years old\n"
            expected_output += "2: Jane Smith, 25 years old\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_calculate_average_age_of_all_persons_in_phonebook(self):
        expected_output = "Average age of all persons:\n~ 27.50 years ~\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.average_age()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test case for empty phonebook
        self.phonebook.phone_book = []
        expected_output = "Error: Division by zero. The phone book is empty.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.average_age()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_count_all_entries_in_phonebook(self):
        expected_output = "Total number of entries:  2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.count_all_entries()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test case for empty phonebook
        self.phonebook.phone_book = []
        expected_output = "Total number of entries:  0\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.count_all_entries()
            self.assertEqual(fake_out.getvalue(), expected_output)

