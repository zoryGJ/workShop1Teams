import unittest

from Exercise9 import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aviva'))
        self.assertFalse(is_palindrome('python'))
        self.assertFalse(is_palindrome('teams'))
    

if __name__ == '__main__':
    unittest.main()