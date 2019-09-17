"""
Program: test.py
Author: Ghulam Omar
Last date modified: 09/10/19
This tests the program for average_score.py.
"""
import unittest
from input_validation import validation_with_if
import unittest.mock as result

class MyTestCase(unittest.TestCase):

    def test_average(self):
        with result.patch('builtins.input', side_effect=[-1, -2, 2]):
            assert validation_with_if.average() == -0.3333333333333333



if __name__ == '__main__':
    unittest.main()
