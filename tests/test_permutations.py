import unittest
from block_solver.permutations import *


class PermutationTestCase(unittest.TestCase):
    def runTest(self):
        p = PermutationBuilder()
        things = [["apple", "bananna"], ["ford", "nissan"], ["2014", "2015"]]

        result = p.getPermutations(things)
        expected = [['apple', 'ford', '2014'],
                    ['apple', 'ford', '2015'],
                    ['apple', 'nissan', '2014'],
                    ['apple', 'nissan', '2015'],
                    ['bananna', 'ford', '2014'],
                    ['bananna', 'ford', '2015'],
                    ['bananna', 'nissan', '2014'],
                    ['bananna', 'nissan', '2015']]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
