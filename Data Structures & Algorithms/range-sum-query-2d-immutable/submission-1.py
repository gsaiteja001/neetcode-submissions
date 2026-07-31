class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix) + 1, len(matrix[0]) + 1
        self.prefix = [[0] * COLS for i in range(ROWS)]
        
        for i in range(1, ROWS):
            total = 0
            for j in range(1, COLS):
                total += matrix[i-1][j-1]
                self.prefix[i][j] = total + self.prefix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1] 