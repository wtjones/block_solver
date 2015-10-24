import copy
from operator import itemgetter
from matrix_math import *
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
            
        permutionBuilder = PermutationBuilder()
        boardPermutations = permutionBuilder.getPermutations(permutationInput)
        return boardPermutations

    def solveBoard(self, board, shapes, shapeTransforms, boardPermutations):

        # shapeTransforms = [];
        # for shapeIndex, shape in enumerate(shapes):
        #     st = solver.getShapeTranforms(b1, shape)
        #     shapeTransforms[shapeIndex] = st
        #     
        #     
        result = {}
        result['boards'] = []

        print shapeTransforms[0]
        print shapeTransforms[1]
        
        matrixMath = MatrixMath()

        solved = False
        permIndex = 0
        while not solved and permIndex < len(boardPermutations):
            permutation = boardPermutations[permIndex]
            print 'permutation'
            print permutation
            
            # Create a copy of the board to modify by placing
            # shapes.
            workBoard = copy.deepcopy(board) #np.copy(b1)
            validShapes = 0
            #for shapeIndex in range(0, len(permutation)):
            #    shape = shapes[shapeIndex]
             #   shapePosition = permutation[shapeIndex]
            for shapePosition in permutation:
                print 'shapPosition:'
                print shapePosition

                #print shapePosition[1]
                shapeIndex = shapePosition[0]
                shapeTransformIndex = shapePosition[1]
                shape = shapes[shapeIndex]
                print 'shape'
                print shape
                
                m = shapeTransforms[shapeIndex][shapeTransformIndex]

                print 'transform'
                print m
                

                tempPoints = []
                valid = True
                for sp in shape['points']:
                    p = matrixMath.transformPoint(sp, m)

                    # make sure point is in board
                    if self.pointInBoard(board, p):
                        if workBoard.cells[p[0], p[1], p[2]] != 8:
                            valid = False
                    else:
                        valid = False
                    tempPoints.append(p)

                if valid:
                    validShapes += 1

                    for p in tempPoints:
                        print p
                        # mark the cells of the working board with the
                        # index of the current shape + 1
                        workBoard.cells[p[0], p[1], p[2]] = shapePosition[0] + 1

            if validShapes == len(shapes):
                print 'all valid'
                result['boards'].append(workBoard)
                print workBoard.prettyPrint()

            permIndex += 1
        result['numPermutations'] = len(boardPermutations)
        result['numSolutions'] = len(result['boards'])
        return result

    def pointInBoard(self, board, point):
        return (point[0] >= 0 and point[0] < board.xMax and
                point[1] >= 0 and point[1] < board.yMax and
                point[2] >= 0 and point[2] < board.zMax)
