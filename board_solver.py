from matrix_math import *
from operator import itemgetter
from permutations import *


class BoardSolver:

    def __getShapeTranforms(self, board, shape):
        """For every cell within the board bounds, apply each
        rotation of every shape. Rotations that fit within
        the board are added to the transforms array.
        """

        result = []

        matrixMath = MatrixMath()

        st = {}
        for tz in range(0, board.zMax):
            for ty in range(0, board.yMax):
                for tx in range(0, board.xMax):
                    for rotation in matrixMath.rotations:
                        m = matrixMath.applyTranslationToMatrix(
                            rotation, tx, ty, tz
                        )

                        # Determine if this matrix places the shape in a valid
                        # position.
                        valid = True
                        tempPoints = []
                        for point in shape['points']:
                            p = matrixMath.transformPoint(point, m)

                            # make sure point is in board
                            if (p[0] >= 0 and p[0] < board.xMax and
                                    p[1] >= 0 and p[1] < board.yMax and
                                    p[2] >= 0 and p[2] < board.zMax):

                                if board.cells[p[0], p[1], p[2]] == 0:
                                    valid = False
                            else:
                                valid = False
                            tempPoints.append(p)

                        if valid:
                            # Valid transforms are hashed by their
                            # sorted points.

                            sortedPoints = \
                                sorted(tempPoints, key=itemgetter(0, 1, 2))
                            pointHash = hash(str(sortedPoints))
                            st[pointHash] = m

        for m in st:
            result.append(st[m])

        return result

    def getBoardShapeTranforms(self, board, shapes):
        """Returns all possible transforms of each shape, indexed
        by the same index as the shape
        """
        shapeTransforms = []
        for shapeIndex, shape in enumerate(shapes):
            #print shapeIndex
            #print shape
            st = self.__getShapeTranforms(board, shape)
            #print st
            shapeTransforms.append(st)
        return shapeTransforms

    def getBoardPermutations(self, board, shapes, shapeTransforms):

        permutationInput = []
        for shapeIndex in range(0, len(shapes)):
            outerList = []
            for transformIndex in range(0, len(shapeTransforms[shapeIndex])):
                item = [shapeIndex, transformIndex]
                outerList.append(item)
            permutationInput.append(outerList)

        print permutationInput
        permutionBuilder = PermutationBuilder()
        boardPermutations = permutionBuilder.getPermutations(permutationInput)
        return boardPermutations
#print boardPermutations



   # def solveBoard(self, board, shapes, shapeTransforms, permutations):

        # shapeTransforms = [];
        # for shapeIndex, shape in enumerate(shapes):
        #     st = solver.getShapeTranforms(b1, shape)
        #     shapeTransforms[shapeIndex] = st


