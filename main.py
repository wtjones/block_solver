from operator import itemgetter
import copy
from board_loader import *
from shapes import shapes
from permutations import *
from matrix_math import *

matrixMath = MatrixMath()
boardMax = 3

boardLoader = BoardLoader()
b1 = boardLoader.getBoard('tests/board-test.json')

# For every cell within the board bounds, apply each rotation of every shape.
# Rotations that fit within the board are added to the transforms array.

for shape in shapes:
    st = {}
    for tz in range(0, b1.zMax):
        for ty in range(0, b1.yMax):
            for tx in range(0, b1.xMax):
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
                        if (p[0] < boardMax and
                                p[1] < boardMax and
                                p[2] < boardMax):

                            if b1.cells[p[0], p[1], p[2]] == 0:
                                valid = False
                        else:
                            valid = False
                        tempPoints.append(p)

                    if valid:
                        # Valid transforms are hashed by their sorted points.
                        sortedPoints = \
                            sorted(tempPoints, key=itemgetter(0, 1, 2))
                        pointHash = hash(str(sortedPoints))
                        st[pointHash] = m

    for m in st:
        shape['transforms'].append(st[m])
        print st[m]

    print 'shape transforms: ' + str(len(st))


# Build a list of possible permutations. 
# Of each permutation: 
#   First index is the index of the shape
#   Second index is the index of the shape transform.
permutationInput = []

for shapeIndex in range(0, len(shapes)):
    shape = shapes[shapeIndex]
    outerList = []
    for transformIndex in range(0, len(shape['transforms'])):
        item = [shapeIndex, transformIndex]
        outerList.append(item)
    permutationInput.append(outerList)

print permutationInput
permutionBuilder = PermutationBuilder()
boardPermutations = permutionBuilder.getPermutations(permutationInput)
print len(boardPermutations)
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
