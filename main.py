import time
from board_loader import *
from shapes import shapes
from permutations import *
from matrix_math import *
from board_solver import *

startTime = time.time()
solvedBoards = []
numRejected = 0


def submitProgress(solvedBoard, rejectedBoard, progressBoard, shapeIndex):
    global numRejected, solvedBoards, startTime
    if shapeIndex == 0:
        print 'shapeindex: {0}'.format(shapeIndex)
        print 'Elapsed: {0}'.format(time.time() - startTime)
    if solvedBoard:
        solvedBoards.append(solvedBoard)
        print 'Progress solved:'
        print solvedBoard.prettyPrint()
        print 'Rejected: {0}'.format(numRejected)
        print 'Elapsed: {0}'.format(time.time() - startTime)
        exit(0)
    if rejectedBoard:
        numRejected += 1
        if numRejected % 1000 == 1:
            print 'Rejected: {0}. ShapeIndex: {1}. Elapsed: {2}'.format(
                    numRejected,
                    shapeIndex,
                    time.time() - startTime,
            )


def solve():
    boardLoader = BoardLoader()
    board = boardLoader.getBoard('boards/board-0.json')
    solver = BoardSolver()
    solvedBoards = []
    startTime = time.time()
    print 'Building shape transforms of board...'
    solver.solveBoard(board, shapes, submitProgress)
    print 'Total solutions: {0}'.format(len(solvedBoards))
    print 'Elapsed: {0}'.format(time.time() - startTime)


if __name__ == '__main__':
    solve()
