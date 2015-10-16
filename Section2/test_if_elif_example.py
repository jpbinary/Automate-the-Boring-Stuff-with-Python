#!/usr/bin/env python3
import unittest
from if_elif_example import check_name

# create a class of object type unittest.TestCase
class SimpleTest(unittest.TestCase):
    '''Test if_elif_example.py for errors'''

    # define the tests you want to run
    def test_names(self):
        # these run the check_name function with the specified arguments, and check for the proper return value
        self.assertEquals(check_name('Bob', 1), 'Hi Bob')
        self.assertEquals(check_name('Billy', 3), 'You are not Alice, kiddo.')
        self.assertEquals(check_name('Gina', 4000), 'Unlike you, Alice is not immortal.')
        self.assertEquals(check_name('Alice', 22), 'Hi Alice')


if __name__ == '__main__':
    unittest.main() # this allows us to run all of the test code