import unittest
from block_solver.board import *
from block_solver.board_loader import *


class BoardLoaderTestCase(unittest.TestCase):
    def runTest(self):
        boardLoader = BoardLoader()
        board = boardLoader.getBoard('tests/board-test.json')

        self.assertEqual(board.xMax, 3)
        self.assertEqual(board.cells[0, 2, 1], 8)


if __name__ == '__main__':
    unittest.main()
