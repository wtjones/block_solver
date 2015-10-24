from board_loader import *
from shapes import shapes
from permutations import *
from matrix_math import *
from board_solver import *


#matrixMath = MatrixMath()


boardLoader = BoardLoader()
board = boardLoader.getBoard('boards/board-0.json')
solver = BoardSolver()

print 'Building shape transforms of board...'
transforms = solver.getBoardShapeTranforms(board, shapes)

for i in range(0, len(transforms)):
    print 'Total xforms of shape {0}: {1}'.format(i, len(transforms[i]))

print 'Building possible permuations of shapes...'
permutations = solver.getBoardPermutations(board, shapes, transforms)
print 'Total permutations: {0}'.format(len(permutations))
# print permutations[0]

# print 'solving'
# result = solver.solveBoard(board, shapes, transforms, permutations)

# print 'result total:'
# print 'numPermutations: {0}'.format(result['numPermutations'])
# print 'numSolutions: {0}'.format(result['numSolutions'])

# for i in range(0, len(result['boards'])):
#     print ''
#     print 'result:'
    
#     print result['boards'][i].prettyPrint()

