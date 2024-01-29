# test_mi_script.py
import unittest
from mi_script import suma

class TestMiScript(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
