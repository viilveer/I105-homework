from fractions import Fraction


class MatrixDeterminantSolver:
    matrix = []
    multiplyMatrix = 1
    zeroCount = 0

    def __init__(self, initialMatrix):
        for index, row in enumerate(initialMatrix):
            initialMatrix[index] = [Fraction(x) for x in row]

        self.matrix = initialMatrix

    def checkMatrix(self):
        matrixLength = len(self.matrix)
        for matrixRow in self.matrix:
            if matrixRow[0] == 0:
                self.zeroCount += 1
            if len(matrixRow) != matrixLength:
                return False
        return matrixLength > 0

    def isFirstRowFirstItemOne(self):
        return self.matrix[0][0] == 1

    def divideByFirstElement(self, index):
        divideBy = self.matrix[index][0]
        self.multiplyMatrix *= divideBy
        self.matrix[index] = [x / divideBy for x in self.matrix[index]]

    def recalculateMatrix(self):
        firstRow = self.matrix[0]
        for row in self.matrix[1:]:
            multiplier = row[0]
            for index, item in enumerate(row):
                row[index] = item - multiplier * firstRow[index]

    def solveDeterminant(self):
        if self.zeroCount == len(self.matrix):
            return 0

        if len(self.matrix) == 1:
            return self.matrix[0][0]

        if len(self.matrix) > 2:
            if self.isFirstRowFirstItemOne():
                # recalculate and then shrink
                self.recalculateMatrix()
                self.shrinkMatrix()
            else:
                if self.matrix[0][0] != 0:
                    # can divide
                    self.divideByFirstElement(0)
                else:
                    # when shifting rows, then matrix must be multipled by -1
                    self.multiplyMatrix *= -1
                    self.matrix = self.matrix[1:] + self.matrix[:1]

            self.solveDeterminant()

        return self.multiplyMatrix * (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0])

    def shrinkMatrix(self):
        self.multiplyMatrix = self.multiplyMatrix * self.matrix[0][0] * ((-1) ** (1 + 1))
        # print(self.multiplyMatrix)
        self.matrix = [row[1:] for row in self.matrix[1:]]


testMatrices = [
    [
        [3, -4, 5],
        [2, -3, 1],
        [3, -5, -1]
        # -1
    ],
    [
        [0, -4, 0, 6],
        [0, -5, 6, 7],
        [0, 0, 1, 2],
        [0, 2, -8, 0]
        # 0
    ],
    [
        [2, -4, 0, 6],
        [4, -5, 6, 7],
        [3, 0, 1, 2],
        [-2, 2, -8, 0]
        # -104
    ],
    [
        [2, -4, 0, 6],
        [4, -5, 6, 7],
        [3, 0, 1, 2],
        [-2, 2, -8, 0, 1]
        # Not square matrix
    ],
    [
        [1, 2], [3, 4]
        # -2
    ],
    [
        [-562, 40, 43, -586, 347],
        [-229, 177, 305, -367, 50],
        [-434, 343, 241, -365, -86],
        [-3, -384, -351, 61, -214],
        [-400, 96, -339, 25, -116],
        # 282416596900
        # võrdluseks http://www.wolframalpha.com/input/?i=det+%5B%5B-562,+40,+43,+-586,+347%5D,+%5B-229,+177,+305,+-367,+50%5D,+%5B-434,+343,+241,+-365,+-86%5D,+%5B-3,+-384,+-351,+61,+-214%5D,+%5B-400,+96,+-339,+25,+-116%5D%5D
    ],

]

for matrix in testMatrices:
    solver = MatrixDeterminantSolver(matrix)
    if solver.checkMatrix():
        print(solver.solveDeterminant())
    else:
        print("Not square matrix")
