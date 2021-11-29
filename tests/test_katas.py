import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5,7), 5+7, "add broken")

    def test_multiply(self):
        self.assertEqual(katas.multiply(5,7), 5*7, "mult broken")

    def test_power(self):
        self.assertEqual(katas.power(5,7), 5 ** 7, "power broken")

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120, "factorial broken")

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3, "fibb broken")


if __name__ == '__main__':
    unittest.main()
