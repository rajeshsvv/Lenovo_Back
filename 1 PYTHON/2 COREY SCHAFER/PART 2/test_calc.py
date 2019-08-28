# to change the directory enter like this which drive u want to change k D:
# in test case result in console f indicates Fail the case when we define the function take care it must start with test otherwise not work
# if name ==main then enter python test_calc.py in command prompt directly otherwise enter python -m unittest test_calc.py

import unittest
import calc


class TestClass(unittest.TestCase):
    def test_add(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_mul(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(-1, 1), -1)
        self.assertEqual(calc.mul(-1, -1), 1)

    def test_div(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -1), 1)
        self.assertEqual(calc.div(-5, -2), 2.5)

        # self.assertRaises(ValueError, calc.div, 10, 0)     #but corey does not prefer this to check divide by zero k he like function call

        # corey like this calling the function in context manager

        with self.assertRaises(ValueError):
            calc.div(10, 0)


if __name__ == "__main__":
    unittest.main()
