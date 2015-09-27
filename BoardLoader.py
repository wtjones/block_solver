import json
import numpy as np


def LoadBoard():
    f = open('board-test.json', 'r')
    boardJson = f.read()
    board = json.loads(boardJson)
    return board


def PrintBoard(board):
    for cell in range(0, len(board['data'])):
        print cell


def PrettyPrint(board, x, y, z):
    result = ''
    for by in range(0, y):
        for bz in range(0, z):
            for bx in range(0, x):
                result += str(int(board[bx, by, bz]))
            result += "\r\n"
        result += "\r\n"
    return result


def GetBoard():
    board = LoadBoard()
    print board
    boardCells = board['x'] * board['y'] * board['z']
    print boardCells
    result = np.zeros((board['x'], board['y'], board['z']))
    i = 0
    for ty in range(0, board['y']):
        for tz in range(0, board['z']):
            for tx in range(0, board['x']):
                result[tx, ty, tz] = int(board['data'][i])
                #print board['data'][i]
                i = i + 1

    return result

if __name__ == '__main__':
    
    #print LoadBoard()
    print PrintBoard(LoadBoard())
    print PrettyPrint(GetBoard(), 3, 3, 3)
    print 'hi'
