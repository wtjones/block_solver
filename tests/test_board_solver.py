import unittest
from board import *
from board_solver import *
from board_loader import *
from matrix_math import *


class BoardSolverCase(unittest.TestCase):
    def test_getBoardShapeTransforms(self):

        #  *
        #  **
        #
        shape = {} #{'transforms': []}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
        shapes = [shape]
        boardLoader = BoardLoader()
        solver = BoardSolver()
        board = boardLoader.getBoard('tests/shape-test.json')
        result = solver.getBoardShapeTranforms(board, shapes)
        print result
        matrixMath = MatrixMath()


        p1 = matrixMath.transformPoint(shape['points'][0], result[0][0])
        p2 = matrixMath.transformPoint(shape['points'][1], result[0][0])
        p3 = matrixMath.transformPoint(shape['points'][2], result[0][0])
        print p1, p2, p3
        # print ''
        # print board.prettyPrint()
        # print result
        # print 'test'

        # one possible transform
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(p1, [1, 0, 0])
        self.assertEqual(p2, [1, 0, 1])
        self.assertEqual(p3, [1, 1, 1])

    def runTinyTest(self):

        shapes = []
        #  *
        #  **
        #
        shape = {}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
        shapes.append(shape)
        # **
        shape = {}
        shape['points'] = [[0, 0, 0], [1, 0, 0]]
        shapes.append(shape)

        boardLoader = BoardLoader()
        solver = BoardSolver()
        board = boardLoader.getBoard('tests/board-tiny-test.json')
        transforms = solver.getBoardShapeTranforms(board, shapes)



        # print ''
        # print board.prettyPrint()
        # print result
        # print 'test'

        #self.assertEqual(len(result), 0)