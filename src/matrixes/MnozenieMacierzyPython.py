from matrixes.MnozenieMacierzy import MnozenieMacierzy

class MnozenieMacierzyPython(MnozenieMacierzy):
    cols = 0
    rows = 0
    matrix = [[]]
    def __init__(self,cols,rows):
        super().__init__(cols,rows)
        self.cols = cols
        self.rows = rows
        self.matrix = [ [ [] for j in range(cols)] for i in range(rows)]
    
    def printMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end = ' ')
            print()
    
    def readFromEntries(self,oMatrix):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(oMatrix[i][j].get())
    
    def ifMultipliable(self,other):
        if (self.cols == other.rows):
            return True
        return False
    @staticmethod
    def summ(m1,m2,row,col,n):
        summa = 0
        for i in range(n):
            summa += m1.matrix[row][i] * m2.matrix[i][col]
        return summa
    @staticmethod
    def multiplicatePython(m1,m2):
        m3 = MnozenieMacierzyPython(m2.cols,m1.rows)
        for i in range(m3.rows):
            for j in range(m3.cols):
                m3.matrix[i][j] = MnozenieMacierzyPython.summ(m1,m2,i,j,m1.cols)
        return m3
    