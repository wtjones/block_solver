import unittest
from board import *
from board_solver import *
from shapes import shapes
from board_loader import *


class BoardSolverCase(unittest.TestCase):
    def runTest(self):

        #  *
        #  **
        #
        shape = {'transforms': []}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]

        boardLoader = BoardLoader()
        solver = BoardSolver()
        board = boardLoader.getBoard('tests/shape-test.json')
        result = solver.getShapeTranforms(board, shape)

        # print ''
        # print board.prettyPrint()
        # print result
        # print 'test'

        self.assertEqual(len(result), 0)
