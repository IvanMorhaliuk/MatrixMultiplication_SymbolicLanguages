from GUI.gui import *
from tkinter import messagebox
from matrixes.MnozenieMacierzyPython import *
from datetime import datetime
from platform import python_version
import timeit

def printToLogFrame(screenText,time,numOfrepeats=1):
    tString = '''Date: {}
    timePy: {}
    Num of Rep: {}
'''.format(str(datetime.today()),str(time),str(numOfrepeats))

    screenText.configure(state="normal")
    screenText.insert('1.0',tString)
    screenText.configure(state="disabled")
def printMatrix(screenText,matrix):
    tString = ""
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            tString += str(matrix.matrix[i][j]) + "\t"
        tString += '\n'
    screenText.configure(state="normal")
    screenText.delete('1.0',"end")
    screenText.insert('1.0',tString)
    screenText.configure(state="disabled")

def Run(event):
    if (mainWindow.mode.get() == "hand"):
        m1 = MnozenieMacierzyPython(int(mainWindow.m1HandSpinParam[0].get()),int(mainWindow.m1HandSpinParam[1].get()))
        m2 = MnozenieMacierzyPython(int(mainWindow.m2HandSpinParam[0].get()),int(mainWindow.m2HandSpinParam[1].get()))
        if mainWindow.types.get() == "integer":
            m1.readFromEntries(mainWindow.handMatrix1,int)
            m2.readFromEntries(mainWindow.handMatrix2,int)
        else:
            m1.readFromEntries(mainWindow.handMatrix1,float)
            m2.readFromEntries(mainWindow.handMatrix2,float)
        try:
            if (not m1.ifMultipliable(m2)):
                raise Exception("Wrong dimentions!")  
        except Exception as e:
            messagebox.showerror(message=e)
        else:
            timeStart = timeit.timeit()
            m3 = MnozenieMacierzyPython.mnoz(m1,m2)
            timeEnd = timeit.timeit()
            printMatrix(mainWindow.handMatrix3,m3)
            printToLogFrame(mainWindow.text,timeEnd-timeStart)
    else:
        m1 = MnozenieMacierzyPython(int(mainWindow.m1SpinParam[0].get()),int(mainWindow.m1SpinParam[1].get()))
        m2 = MnozenieMacierzyPython(int(mainWindow.m2SpinParam[0].get()),int(mainWindow.m2SpinParam[1].get()))
        m1From = int(mainWindow.m1SpinRange[0].get())
        m1To = int(mainWindow.m1SpinRange[1].get())
        m2From = int(mainWindow.m2SpinRange[0].get())
        m2To = int(mainWindow.m2SpinRange[1].get())
        try:
            if (not m1.ifMultipliable(m2)):
                raise Exception("Wrong dimentions!")  
        except Exception as e:
            messagebox.showerror(message=e)
        else:
            if mainWindow.types.get() == "integer":
                m1.fillMatrix(m1From,m1To,True)
                m2.fillMatrix(m2From,m2To,True)
            else:
                m1.fillMatrix(m1From,m1To,False)
                m2.fillMatrix(m2From,m2To,False)
            printMatrix(mainWindow.matrixesTexts[0],m1)
            printMatrix(mainWindow.matrixesTexts[1],m2)
            timeStart = timeit.timeit()
            m3 = MnozenieMacierzyPython.mnoz(m1,m2)
            timeEnd = timeit.timeit()
            printMatrix(mainWindow.matrixesTexts[2],m3)
            printToLogFrame(mainWindow.text,timeEnd-timeStart)



mainWindow = GUI()
mainWindow.button.bind("<Button-1>",Run)
mainWindow.render()



