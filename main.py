import time
import argparse
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


def countUniqueBoards(boards):
    solutionHash = {}
    for i, solvedBoard in enumerate(solver.solvedBoards):
        solutionHash[hash(solvedBoard.prettyPrint())] = solvedBoard
    return len(solutionHash)


def writeResults(filePath):
    with open(filePath, 'w') as f:
        for i, solvedBoard in enumerate(solver.solvedBoards):
            f.write('Solution: {0}\n---------------\n'.format(i))
            f.write(solvedBoard.prettyPrint())
            f.write('===============\n')


def solve(args):
    global startTime, solver, numProgress

    boardFileName = 'boards/board-{0}.json'.format(args.board)
    boardLoader = BoardLoader()
    print 'Loading {0}'.format(boardFileName)
    board = boardLoader.getBoard(boardFileName)
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
    solver.solveBoard(args.maxSolutions)
    print 'Total solutions: {0}'.format(len(solver.solvedBoards))
    print 'Elapsed: {0}'.format(time.time() - startTime)

    print 'Total unique solutions: {0}'.format(
        countUniqueBoards(solver.solvedBoards)
    )
    if args.resultsFile:
        writeResults(args.resultsFile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--board',
        type=int,
        default=0,
        help='The board number. See the boards folder. Defaults to 0.'
    )
    parser.add_argument(
        '--maxSolutions',
        type=int,
        default=max,
        help='Stop solving after reaching this count.'
    )
    parser.add_argument(
        '--resultsFile',
        help='Write solutions to a file.'
    )

    args = parser.parse_args()
    solve(args)
