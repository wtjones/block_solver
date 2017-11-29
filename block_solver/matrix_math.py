import numpy as np


class MatrixMath:

    def __init__(self):
        self._roty90 = np.matrix("0 0 1 0; 0 1 0 0; -1 0 0 0; 0 0 0 1")
        self._rotz90 = np.matrix("0 -1 0 0; 1 0 0 0; 0 0 1 0; 0 0 0 1")
        self._rotx90 = np.matrix("1 0 0 0; 0 0 -1 0; 0 1 0 0; 0 0 0 1")
        self._identity = np.matrix("1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1")
        self._rotations = self.__getRotations()

    @property
    def roty90(self):
        return self._roty90

    @property
    def rotz90(self):
        return self._rotz90

    @property
    def rotx90(self):
        return self._rotx90

    @property
    def rotations(self):
        return self._rotations

    def transformPoint(self, point, matrix):
        p1 = np.matrix([[point[0]], [point[1]], [point[2]], [1]])
        result = matrix * p1
        return [result[0, 0], result[1, 0], result[2, 0]]

    def applyTranslationToMatrix(self, matrix, x, y, z):
        transMatrix = np.matrix(matrix)
        transMatrix[0, 3] = x
        transMatrix[1, 3] = y
        transMatrix[2, 3] = z
        return transMatrix

    def __getRotations(self):
        """ Build an array of a all shape rotations. """
        roty90 = np.matrix("0 0 1 0; 0 1 0 0; -1 0 0 0; 0 0 0 1")
        rotz90 = np.matrix("0 -1 0 0; 1 0 0 0; 0 0 1 0; 0 0 0 1")
        rotx90 = np.matrix("1 0 0 0; 0 0 -1 0; 0 1 0 0; 0 0 0 1")
        identity = np.matrix("1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1")

        xRotations = \
            [identity, rotx90, rotx90 * rotx90, rotx90 * rotx90 * rotx90]
        yRotations = \
            [identity, roty90, roty90 * roty90, roty90 * roty90 * roty90]
        zRotations = \
            [identity, rotz90, rotz90 * rotz90, rotz90 * rotz90 * rotz90]

        rotations = []

        for rz in zRotations:
            for ry in yRotations:
                for rx in xRotations:
                    rotations.append(rz * ry * rx)
        return rotations
