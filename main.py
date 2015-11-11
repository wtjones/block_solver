import time
from board_loader import *
from shapes import shapes
from permutations import *
from matrix_math import *
from board_solver import *

startTime = time.time()
solvedBoards = []
numRejected = 0
numProgress = 0
solver = None
defaultBoardFileName = 'boards/board-0.json'


def onProgress(board, shapeIndex):
    global startTime, numProgress
    numProgress += 1
    if shapeIndex == 0 or numProgress % 10000 == 0:
        print 'progress count: {0}. shapeindex: {1}'.format(
            numProgress, shapeIndex
        )
        print 'Elapsed: {0}'.format(time.time() - startTime)


def onSolved(solvedBoard):
    global startTime

    print 'Solution found:'
    print solvedBoard.prettyPrint()
    print 'Current solution count: {0}'.format(
        len(solver.solvedBoards)
    )
    print 'Elapsed: {0}'.format(time.time() - startTime)


def solve():
    global startTime, solver, numProgress, defaultBoardFileName
    boardLoader = BoardLoader()
    board = boardLoader.getBoard(defaultBoardFileName)
    print 'Solver init of board:'
    print board.prettyPrint()
    print '...'
    startTime = time.time()

    solver = BoardSolver(board, shapes, onProgress, onSolved)
    print 'Elapsed: {0}'.format(time.time() - startTime)
    for i in range(0, len(solver.shapeTransforms)):
        print 'Total possible transforms of shape {0}: {1}'.format(
            i, len(solver.shapeTransforms[i])
        )

    print 'Solving...'
    solver.solveBoard()
    print 'Total solutions: {0}'.format(len(solver.solvedBoards))
    print 'Elapsed: {0}'.format(time.time() - startTime)

    solutionHash = {}
    for i, solvedBoard in enumerate(solver.solvedBoards):
        solutionHash[hash(solvedBoard.prettyPrint())] = solvedBoard

    print 'Total unique solutions: {0}'.format(len(solutionHash))

if __name__ == '__main__':
    solve()
