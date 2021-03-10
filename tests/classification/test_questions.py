import unittest
import questions as q
from unittest.mock import patch
from unittest import TestCase
from contextlib import contextmanager
import builtins
@contextmanager


def mockRawInput(mock):
    original_raw_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_raw_input

class test_questions(unittest.TestCase):
    def test_valid_seats(self):
        with mockRawInput(6):
             self.assertEqual(q.seats(), 6)
             self.assertIsNot(q.seats(), 2)

        with mockRawInput(7):
             self.assertEqual(q.seats(), 7)

        with mockRawInput(5):
             self.assertEqual(q.seats(), 5)
             self.assertIsNot(q.seats(), 4)

    def test_invalid_seats(self):
        with mockRawInput(1000):
            with self.assertRaises(Exception) as cm:
                q.seats()
            err = cm.exception
            self.assertEqual(str(err), "Please enter one of the following numbers: 2,4,5,6,7")

    def test_string_seats(self):
        with mockRawInput('HELLO'):
            with self.assertRaises(TypeError) as cm:
                q.seats()
            err = cm.exception
            self.assertEqual(str(err), "The number of seats must be an integer.")

    def test_valid_rapidCharge(self):
        with mockRawInput('yes'):
            self.assertEqual(q.rapid_charge(), 'yes')
        with mockRawInput('NO'):
            self.assertEqual(q.rapid_charge(), 'NO')


    def test_invalid_int_rapidCharge(self):
        with mockRawInput(20):
            with self.assertRaises(Exception) as cm:
                q.rapid_charge()
            err = cm.exception
            self.assertEqual(str(err), "Input must be not a digit")

    def test_invalid_string_rapidCharge(self):
        with mockRawInput("YESSSSSSSS"):
            with self.assertRaises(Exception) as cm:
                q.rapid_charge()
            err = cm.exception
            self.assertEqual(str(err), 'Choose Yes if you would like your EV to have Rapid Charge and No if not.')

    def test_valid_drivingRange(self):
        with mockRawInput('50-250'):
            self.assertEqual(q.driving_range(), '50-250')
        with mockRawInput('450-650'):
            self.assertEqual(q.driving_range(), '450-650')


    def test_invalid_driving_range(self):
        with mockRawInput('5'):
            with self.assertRaises(Exception) as cm:
                q.driving_range()
            err = cm.exception
            self.assertEqual(str(err), 'Please choose one of the following ranges: 50-250, 250-450,450-650')

        with mockRawInput(100):
            with self.assertRaises(Exception) as cm:
                q.driving_range()
            err = cm.exception
            self.assertEqual(str(err), "Input must be a range.")

    def test_valid_budgetRange(self):
        with mockRawInput('0-50000'):
            self.assertEqual(q.budget_range(), '0-50000')
        with mockRawInput('150000-200000'):
            self.assertEqual(q.budget_range(), '150000-200000')

    def test_invalid_budgetRange(self):
        with mockRawInput('NO PREFERENCE'):
            with self.assertRaises(Exception) as cm:
                q.budget_range()
            err = cm.exception
            self.assertEqual(str(err), 'Please choose one of the following ranges: 0-50000, 50000-100000,100000-150000,150000-200000,200000-250000,300000-350000')

        with mockRawInput(100):
            with self.assertRaises(Exception) as cm:
                q.budget_range()
            err = cm.exception
            self.assertEqual(str(err), "Input must be a range.")




if __name__ == '__main__':
    unittest.main()
