import unittest
from matrix_math import *


class MatrixMathTestCase(unittest.TestCase):
    def runTest(self):
        matrixMath = MatrixMath()
        point = [1, 0, 0]

        result = matrixMath.transformPoint(point, matrixMath.rotz90)

        self.assertEqual(result, [0, 1, 0])


if __name__ == '__main__':
    unittest.main()
