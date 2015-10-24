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
        p1 = matrixMath.transformPoint(shape['points'][0], result[0][0])
        p2 = matrixMath.transformPoint(shape['points'][1], result[0][0])
        p3 = matrixMath.transformPoint(shape['points'][2], result[0][0])

        # one possible transform
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(p1, [1, 0, 0])
        self.assertEqual(p2, [1, 0, 1])
        self.assertEqual(p3, [1, 1, 1])

    def test_solver(self):

        # Arrange

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
        #permutationBuilder = PermutationBuilder()
        board = boardLoader.getBoard('tests/board-tiny-test.json')
        
        transforms = solver.getBoardShapeTranforms(board, shapes)
        print 'transforms'
        print transforms[0]
        print 'transforms'
        print transforms[1]
        
        permutations = solver.getBoardPermutations(board, shapes, transforms)
        print 'permutations: ' + str(len(permutations))
        print permutations[0]
        
        print 'solving'
        result = solver.solveBoard(board, shapes, transforms, permutations)

        print 'result total:'
        print 'numPermutations: {0}'.format(result['numPermutations'])
        print 'numSolutions: {0}'.format(result['numSolutions'])
        
        for i in range(0, len(result['boards'])):
            print ''
            print 'result:'
            
            print result['boards'][i].prettyPrint()


        # print ''
        # print board.prettyPrint()
        # print result
        # print 'test'

        #self.assertEqual(len(result), 0)