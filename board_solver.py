import copy
from operator import itemgetter
from matrix_math import *
from permutations import *


class BoardSolver:

    def __init__(self):
        self._matrixMath = MatrixMath()

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

                            if self.pointInBoard(board, p):
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
            st = self.__getShapeTranforms(board, shape)
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
            
        permutionBuilder = PermutationBuilder()
        boardPermutations = permutionBuilder.getPermutations(permutationInput)
        return boardPermutations

    def __solveBoardShape(self, board, shapes, shapeIndex, callback):
        callback(None, None, board, shapeIndex)
        shape = shapes[shapeIndex]
        
        shapeTransforms = self.__getShapeTranforms(board, shape)
        for tIndex, st in enumerate(shapeTransforms):
            workBoard = copy.deepcopy(board)
           
            valid = self.applyTransformToBoard(
                workBoard,
                shape,
                shapeIndex,
                st
            )

            if valid:
                isSolved = False
                if shapeIndex == len(shapes) - 1:
                    isSolved = workBoard.isSolved()
                    if isSolved:
                        callback(workBoard, None, None, shapeIndex)
                        return
                    else:
                        # Report rejected
                        callback(None, workBoard, None, shapeIndex)
                if shapeIndex < len(shapes) - 1:
                    self.__solveBoardShape(
                        workBoard, shapes, shapeIndex + 1, callback
                    )
                

    def solveBoard(self, board, shapes, callback):
        self.__solveBoardShape(board, shapes, 0, callback)

    def applyTransformToBoard(self, board, shape, shapeIndex, transform):
        tempPoints = []
        valid = True
        for sp in shape['points']:
            p = self._matrixMath.transformPoint(sp, transform)

            # make sure point is in board
            if self.pointInBoard(board, p):
                if board.cells[p[0], p[1], p[2]] != 8:
                    valid = False
            else:
                valid = False
            tempPoints.append(p)

        if valid:
            for p in tempPoints:
                # mark the cells of the working board with the
                # index of the current shape + 1
                board.cells[p[0], p[1], p[2]] = shapeIndex + 1
        return valid

    def pointInBoard(self, board, point):
        return (point[0] >= 0 and point[0] < board.xMax and
                point[1] >= 0 and point[1] < board.yMax and
                point[2] >= 0 and point[2] < board.zMax)
