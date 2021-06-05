import unittest

from matrixes.MnozenieMacierzyPython import *
from matrixes.MnozenieMacierzyCpp import *
class TestMatrixes(unittest.TestCase):

    def test_shouldReturnCorrectAnswerForPython_1(self):
        #given
        m1 = MnozenieMacierzyPython(2,2)
        m2 = MnozenieMacierzyPython(2,2)
        m3 = MnozenieMacierzyPython(2,2)
        m1.matrix = [ [1,0], [0,1] ]
        m2.matrix = [ [2,3], [4,5] ]
        m3.matrix = [ [2,3], [4,5] ]
        #when
        result = MnozenieMacierzyPython.mnoz(m1,m2)
        #then
        self.assertEqual(m3.matrix,result.matrix)
    def test_shouldReturnCorrectAnswerForC_1(self):
        #given
        m1 = MnozenieMacierzyCpp(2,2)
        m2 = MnozenieMacierzyCpp(2,2)
        m3 = MnozenieMacierzyCpp(2,2)
        m1.matrix = [ [1,0], [0,1] ]
        m2.matrix = [ [2,3], [4,5] ]
        m3.matrix = [ [2,3], [4,5] ]
        m1.convert(True)
        m2.convert(True)
        m3.convert(True)
        result = MnozenieMacierzyCpp(2,2)
        result.convert(True)
        #when
        MnozenieMacierzyCpp.mnoz(m1.arg1,m2.arg1,result.arg1,result.rows,result.cols,m1.cols,True)
        #then
        self.assertTrue(MnozenieMacierzyCpp.areEqual(m3,result))
    
    def test_shouldReturnCorrectAnswerForPython_2(self):
        #given
        m1 = MnozenieMacierzyPython(3,2)
        m2 = MnozenieMacierzyPython(2,3)
        m3 = MnozenieMacierzyPython(2,2)
        m1.matrix = [ [1,2,1], [4,-2,0] ]
        m2.matrix = [ [0,1], [2,0], [-1,-1] ]
        m3.matrix = [ [3,0], [-4,4] ]
        #when
        result = MnozenieMacierzyPython.mnoz(m1,m2)
        #then
        self.assertEqual(m3.matrix,result.matrix)

    def test_shouldReturnCorrectAnswerForC_2(self):
        #given
        m1 = MnozenieMacierzyCpp(3,2)
        m2 = MnozenieMacierzyCpp(2,3)
        m3 = MnozenieMacierzyCpp(2,2)
        m1.matrix = [ [1,2,1], [4,-2,0] ]
        m2.matrix = [ [0,1], [2,0], [-1,-1] ]
        m3.matrix = [ [3,0], [-4,4] ]
        m1.convert(True)
        m2.convert(True)
        m3.convert(True)
        result = MnozenieMacierzyCpp(2,2)
        result.convert(True)
        #when
        MnozenieMacierzyCpp.mnoz(m1.arg1,m2.arg1,result.arg1,result.rows,result.cols,m1.cols,True)
        #then
        self.assertTrue(MnozenieMacierzyCpp.areEqual(m3,result))

    def test_shouldReturnCorrectAnswerForPython_3(self):
        #given
        m1 = MnozenieMacierzyPython(2,3)
        m2 = MnozenieMacierzyPython(3,2)
        m3 = MnozenieMacierzyPython(3,3)
        m1.matrix = [ [1,2], [4,-2], [0,3] ]
        m2.matrix = [ [0,1,-3], [2,-1,0] ]
        m3.matrix = [ [4,-1,-3], [-4,6,-12], [6,-3,0] ]
        #when
        result = MnozenieMacierzyPython.mnoz(m1,m2)
        #then
        self.assertEqual(m3.matrix,result.matrix)

    def test_shouldReturnCorrectAnswerForC_3(self):
        #given
        m1 = MnozenieMacierzyCpp(2,3)
        m2 = MnozenieMacierzyCpp(3,2)
        m3 = MnozenieMacierzyCpp(3,3)
        m1.matrix = [ [1,2], [4,-2], [0,3] ]
        m2.matrix = [ [0,1,-3], [2,-1,0] ]
        m3.matrix = [ [4,-1,-3], [-4,6,-12], [6,-3,0] ]
        m1.convert(True)
        m2.convert(True)
        m3.convert(True)
        result = MnozenieMacierzyCpp(3,3)
        result.convert(True)
        #when
        MnozenieMacierzyCpp.mnoz(m1.arg1,m2.arg1,result.arg1,result.rows,result.cols,m1.cols,True)
        #then
        self.assertTrue(MnozenieMacierzyCpp.areEqual(m3,result))

    def test_shouldRaiseException_WhenWrongDimentions(self):
        m1 = MnozenieMacierzyPython(3,2)
        m2 = MnozenieMacierzyPython(2,1)
        with self.assertRaises(Exception):
            MnozenieMacierzyPython.ifMultipliable(m1,m2)

if __name__ == '__main__':
    unittest.main()