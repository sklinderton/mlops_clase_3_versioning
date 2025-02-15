import unittest
from suma import suma


class MyTestCase(unittest.TestCase):
    def test_suma(self):
        resultado_suma = suma(3, 5)
        self.assertEqual(resultado_suma, 8)


if __name__ == '__main__':
    unittest.main()
