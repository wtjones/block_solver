import unittest
from board import *
from board_loader import *


class BoardTestCase(unittest.TestCase):
    def runTest(self):
        boardLoader = BoardLoader()
        board = boardLoader.getBoard('tests/board-test.json')

        result = board.prettyPrint()

        expected = '''\
000
800
000

000
888
000

000
008
088
'''
        self.assertEqual(result, expected)
