import unittest
from board import *
from board_solver import *
from board_loader import *
from matrix_math import *


class BoardSolverCase(unittest.TestCase):

    def test_getBoardShapeTransforms(self):

        # Arrange
        #  *
        #  **
        #
        shape = {}
        shape['points'] = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
        shapes = [shape]
        boardLoader = BoardLoader()
        matrixMath = MatrixMath()
        board = boardLoader.getBoard('tests/shape-test.json')

        # Act
        solver = BoardSolver(board, shapes)
        result = solver.shapeTransforms

        # Assert
        p1 = matrixMath.transformPoint(
            shape['points'][0],
            result[0][0]['matrix']
        )
        p2 = matrixMath.transformPoint(
            shape['points'][1],
            result[0][0]['matrix']
        )
        p3 = matrixMath.transformPoint(
            shape['points'][2],
            result[0][0]['matrix']
        )

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
        board = boardLoader.getBoard('tests/board-tiny-test.json')
        solver = BoardSolver(board, shapes)

        solver.solveBoard()
        self.assertEqual(len(solver.solvedBoards), 3)
