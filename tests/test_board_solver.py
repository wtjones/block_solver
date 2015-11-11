import unittest
from board import *
from board_solver import *
from board_loader import *
from matrix_math import *


class BoardSolverCase(unittest.TestCase):

    # def __init__(self):
    #     self._solvedBoards = []

    def test_getBoardShapeTransforms(self):

        # Arrange
        #  *
        #  **
        #
        shape = {} #{'transforms': []}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
        shapes = [shape]
        boardLoader = BoardLoader()
        matrixMath = MatrixMath()
        solver = BoardSolver()
        board = boardLoader.getBoard('tests/shape-test.json')

        # Act
        result = solver.getBoardShapeTranforms(board, shapes)

        # Assert
        p1 = matrixMath.transformPoint(shape['points'][0], result[0][0]['matrix'])
        p2 = matrixMath.transformPoint(shape['points'][1], result[0][0]['matrix'])
        p3 = matrixMath.transformPoint(shape['points'][2], result[0][0]['matrix'])

        # one possible transform
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(p1, [1, 0, 0])
        self.assertEqual(p2, [1, 0, 1])
        self.assertEqual(p3, [1, 1, 1])

    def test_solver(self):
        shapes = []
        # x*x
        # x**
        # xxx
        shape = {}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
        shapes.append(shape)
        # xxx
        # x**
        # xxx
        shape = {}
        shape['points'] = [[0, 0, 0], [1, 0, 0]]
        shapes.append(shape)

        boardLoader = BoardLoader()
        solver = BoardSolver()
       
        board = boardLoader.getBoard('tests/board-tiny-test.json')

        self._solvedBoards = []
        self._numRejected = 0
        solver.solveBoard(board, shapes, self.submitProgress)
        print 'Rejected: {0}'.format(self._numRejected)
        self.assertEqual(len(self._solvedBoards), 3)

    def submitProgress(self, solvedBoard, rejectedBoard, progressBoard, shapeIndex):
        if solvedBoard:
            self._solvedBoards.append(solvedBoard)
            print 'Progress solved:'
            print solvedBoard.prettyPrint()

        if rejectedBoard:
            self._numRejected += 1
