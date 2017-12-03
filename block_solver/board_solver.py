import copy
from operator import itemgetter
from .matrix_math import *
from .permutations import *


class BoardSolver:

    def __init__(
        self,
        board, shapes,
        progressCallback=None,
        solvedCallback=None
    ):
        self._matrixMath = MatrixMath()
        self._shapeTransforms = []
        self._solvedBoards = []
        self._board = board
        self._shapes = shapes
        self._maxSolutions = max
        self._progressCallback = progressCallback
        self._solvedCallback = solvedCallback
        self._shapeTransforms = self.getBoardShapeTranforms(
            board, shapes
        )

    @property
    def shapeTransforms(self):
        return self._shapeTransforms

    @property
    def solvedBoards(self):
        return self._solvedBoards

    def __handleProgressCallback(self, board, shapeIndex):
        if self._progressCallback:
            self._progressCallback(board, shapeIndex)

    def __handleSolvedCallback(self, board):
        if self._solvedCallback:
            self._solvedCallback(board)

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
                            st[pointHash] = {
                                'matrix': m, 'points': sortedPoints
                            }

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

    def __solveBoardShape(self, board, shapeIndex):
        self.__handleProgressCallback(board, shapeIndex)
        if len(self._solvedBoards) == self._maxSolutions:
            return
        shape = self._shapes[shapeIndex]

        shapeTransforms = []
        for st in self._shapeTransforms[shapeIndex]:
            valid = True
            for point in st['points']:
                if board.cells[point[0], point[1], point[2]] != 8:
                    valid = False

            if valid:
                shapeTransforms.append(st)

        for tIndex, st in enumerate(shapeTransforms):
            workBoard = copy.deepcopy(board)

            self.applyTransformToBoard(
                workBoard,
                shape,
                shapeIndex,
                st
            )

            isSolved = False
            if shapeIndex == len(self._shapes) - 1:
                isSolved = workBoard.isSolved()
                if isSolved:
                    self._solvedBoards.append(workBoard)
                    self.__handleSolvedCallback(workBoard)
                    return

            if shapeIndex < len(self._shapes) - 1:
                self.__solveBoardShape(
                    workBoard, shapeIndex + 1
                )

    def solveBoard(self, maxSolutions=max):
        self._maxSolutions = maxSolutions
        self.__solveBoardShape(self._board, 0)

    def applyTransformToBoard(self, board, shape, shapeIndex, transform):
        for p in transform['points']:
            board.cells[p[0], p[1], p[2]] = shapeIndex + 1

    def pointInBoard(self, board, point):
        return (point[0] >= 0 and point[0] < board.xMax and
                point[1] >= 0 and point[1] < board.yMax and
                point[2] >= 0 and point[2] < board.zMax)
