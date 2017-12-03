import json
import numpy as np
from .board import *


class BoardLoader:

    def __loadBoard(self, fileName):
        f = open(fileName, 'r')
        boardJson = f.read()
        f.close()
        board = json.loads(boardJson)
        return board

    def getBoard(self, fileName):
        board = self.__loadBoard(fileName)
        result = np.zeros((board['x'], board['y'], board['z']))
        i = 0
        for ty in reversed(list(range(0, board['y']))):
            for tz in range(0, board['z']):
                for tx in range(0, board['x']):
                    result[tx, ty, tz] = int(board['data'][i])
                    i = i + 1

        return Board(result, board['x'], board['y'], board['z'])
