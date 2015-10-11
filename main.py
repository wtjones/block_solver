import copy
from board_loader import *
from shapes import shapes
from permutations import *
from matrix_math import *
from board_solver import *


matrixMath = MatrixMath()
boardMax = 3

boardLoader = BoardLoader()
b1 = boardLoader.getBoard('tests/board-test.json')
solver = BoardSolver()

shapeTransforms = solver.getBoardShapeTranforms(b1, shapes)
# for shapeIndex, shape in enumerate(shapes):
#     st = solver.getShapeTranforms(b1, shape)
#     shapeTransforms[shapeIndex] = st
#     
#     
  
    #shape['transforms'] = st

    #print 'shape transforms: ' + str(len(st))


# Build a list of possible permutations. 
# Of each permutation: 
#   First index is the index of the shape
#   Second index is the index of the shape transform.
# permutationInput = []



# for shapeIndex in range(0, len(shapes)):
#     shape = shapes[shapeIndex]
#     outerList = []
#     for transformIndex in range(0, len(shape['transforms'])):
#         item = [shapeIndex, transformIndex]
#         outerList.append(item)
#     permutationInput.append(outerList)

# print permutationInput
# permutionBuilder = PermutationBuilder()
# boardPermutations = permutionBuilder.getPermutations(permutationInput)
# print len(boardPermutations)
#print boardPermutations


solved = False
permIndex = 0
while not solved and permIndex < len(boardPermutations):
    permutation = boardPermutations[permIndex]

    workBoard = copy.deepcopy(b1) #np.copy(b1)
    validShapes = 0
    for shapePosition in permutation:
        shape = shapes[shapePosition[0]]
        m = shape['transforms'][shapePosition[1]]
        #print transform

        tempPoints = []
        valid = True
        for sp in shape['points']:
            p = matrixMath.transformPoint(sp, m)

            if p[0] < boardMax and p[1] < boardMax and p[2] < boardMax:
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

        print workBoard.prettyPrint()

    permIndex += 1
