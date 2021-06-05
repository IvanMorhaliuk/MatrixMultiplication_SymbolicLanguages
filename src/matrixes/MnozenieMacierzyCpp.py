from ctypes import *
from matrixes.MnozenieMacierzy import MnozenieMacierzy
def float_list(lst):
    if isinstance(lst[0], list):
        data = [float_list(row) for row in lst]
        return (POINTER(c_float) * len(lst))(*data)
    return (c_float * len(lst))(*lst)

def int_list(lst):
    if isinstance(lst[0], list):
        data = [int_list(row) for row in lst]
        return (POINTER(c_int) * len(lst))(*data)
    return (c_int * len(lst))(*lst)

class MnozenieMacierzyCpp(MnozenieMacierzy):
    def __init__(self,cols,rows):
        super().__init__(cols,rows)
        self.cols = cols
        self.rows = rows
        self.matrix = [ [ 0 for j in range(cols)] for i in range(rows)]
    def takeMatrixes(self,m1,isInteger):
        if isInteger == False:
            self.arg1 = float_list(m1.matrix)
        else:
            self.arg1 = int_list(m1.matrix)

    def convert(self,isInteger):
        if isInteger == False:
            self.arg1 = float_list(self.matrix)
        else:
            self.arg1 = int_list(self.matrix)

    def printMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.arg1[i][j],end=' ')
            print()
    @staticmethod
    def areEqual(m1,m2):
        if m1.rows != m2.rows or m1.cols != m2.cols:
            return False
        for i in range(m1.rows):
            for j in range(m1.cols):
                if m1.arg1[i][j] != m2.arg1[i][j]:
                    return False
        return True
    @staticmethod
    def mnoz(m1,m2,m3,m3rows,m3cols,m1cols,isInteger):

        lib = windll.LoadLibrary("src/dlls/mydll.dll")
        if isInteger==False: 
            lib.float_mnoz.argtypes = [type(m1),type(m2),type(m3),c_int,c_int,c_int]
            lib.float_mnoz(m1,m2,m3,m3rows,m3cols,m1cols)
        else:
            lib.int_mnoz.argtypes = [type(m1),type(m2),type(m3),c_int,c_int,c_int]
            lib.int_mnoz(m1,m2,m3,m3rows,m3cols,m1cols)