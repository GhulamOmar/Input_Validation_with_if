"""
Program: test_validation_with_if.py
Author: Ghulam Omar
Last date modified: 09/17/19
This tests the program for validation_with_if.py with if validation
"""
import unittest
from input_validation import validation_with_if
import unittest.mock as result

class MyTestCase(unittest.TestCase):

    def test_average(self):
        with result.patch('builtins.input', side_effect=[-1, -2, -2]):
            assert validation_with_if.average() == -1.6666666666666667



if __name__ == '__main__':
    unittest.main()
