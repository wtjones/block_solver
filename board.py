class Board:

    def __init__(self, cells, xMax, yMax, zMax):
        self.xMax = xMax
        self.yMax = yMax
        self.zMax = zMax
        self._cells = cells

    @property
    def cells(self):
        return self._cells

    def isSolved(self):
        result = True
        for by in range(0, self.yMax):
            for bz in range(0, self.yMax):
                for bx in range(0, self.zMax):
                    if int(self.cells[bx, by, bz]) == 8:
                        result = False
        return result

    def prettyPrint(self):
        result = ''
        for by in range(self.yMax - 1, -1, -1):
            for bz in range(0, self.yMax):
                for bx in range(0, self.zMax):
                    result += str(int(self.cells[bx, by, bz]))
                result += "\n"
            result += "\n" if by > 0 else ""
        return result
