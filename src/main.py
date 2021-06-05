from GUI.gui import *
from tkinter import messagebox
from matrixes.MnozenieMacierzyPython import *
from matrixes.MnozenieMacierzyCpp import *
from datetime import datetime
from platform import python_version
import timeit

def printToLogFrame(screenText,timePy,convertTime,timeC,numOfrepeats=1):
    tString = '''Date: {}
    timePy: {}
    convert Time: {}
    timeC: {}
    Num of Rep: {}
'''.format(str(datetime.today()),str(timePy),str(convertTime),str(timeC),str(numOfrepeats))

    screenText.configure(state="normal")
    screenText.insert('1.0',tString)
    screenText.configure(state="disabled")
    f = open("src/logs/log.txt", "w")
    f.write(tString)
    f.close()

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
    numOfRepeats = 1 if (mainWindow.repeats.get() in ['','+','-','0'] ) else int(mainWindow.repeats.get())
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
            
            m1C = MnozenieMacierzyCpp(m1.cols,m1.rows)
            m2C = MnozenieMacierzyCpp(m2.cols,m2.rows)
            m3C = MnozenieMacierzyCpp(m2.cols,m1.rows)
            if mainWindow.types.get() == "integer":

                convertTimeStart = timeit.timeit()
                m3C.convert(True)
                m1C.takeMatrixes(m1,True)
                m2C.takeMatrixes(m2,True)
                convertTimeEnd = timeit.timeit()
                for i in range(numOfRepeats):
                    cTimeStart = timeit.timeit()
                    MnozenieMacierzyCpp.computeInC(m1C.arg1,m2C.arg1,m3C.arg1,m3C.rows,m3C.cols,m1C.cols,True)
                    cTimeEnd = timeit.timeit()
                    timeStart = timeit.timeit()
                    m3 = MnozenieMacierzyPython.mnoz(m1,m2)
                    timeEnd = timeit.timeit()
            else:
                convertTimeStart = timeit.timeit()
                m3C.convert(False)
                m1C.takeMatrixes(m1,False)
                m2C.takeMatrixes(m2,False)
                convertTimeEnd = timeit.timeit()
                for i in range(numOfRepeats):
                    cTimeStart = timeit.timeit()
                    MnozenieMacierzyCpp.computeInC(m1C.arg1,m2C.arg1,m3C.arg1,m3C.rows,m3C.cols,m1C.cols,False)
                    cTimeEnd = timeit.timeit()
                    timeStart = timeit.timeit()
                    m3 = MnozenieMacierzyPython.mnoz(m1,m2)
                    timeEnd = timeit.timeit()

            m3C.printMatrix()

            printMatrix(mainWindow.handMatrix3,m3)
            printToLogFrame(mainWindow.text,timeEnd-timeStart,convertTimeEnd-convertTimeStart,cTimeEnd-cTimeStart,numOfRepeats)
    else:
        try:
            m1 = MnozenieMacierzyPython(int(mainWindow.m1SpinParam[0].get()),int(mainWindow.m1SpinParam[1].get()))
            m2 = MnozenieMacierzyPython(int(mainWindow.m2SpinParam[0].get()),int(mainWindow.m2SpinParam[1].get()))
            if mainWindow.types.get() == "integer":
                m1From = int(mainWindow.m1SpinRange[0].get())
                m1To = int(mainWindow.m1SpinRange[1].get())
                m2From = int(mainWindow.m2SpinRange[0].get())
                m2To = int(mainWindow.m2SpinRange[1].get())
            else:
                m1From = float(mainWindow.m1SpinRange[0].get())
                m1To = float(mainWindow.m1SpinRange[1].get())
                m2From = float(mainWindow.m2SpinRange[0].get())
                m2To = float(mainWindow.m2SpinRange[1].get())
            if (not m1.ifMultipliable(m2)):
                raise Exception("Wrong dimentions!")  
        except ValueError as e:
            messagebox.showerror(message="Wrong input!")   
        except Exception as e:
            messagebox.showerror(message=e)
        else:
            m1C = MnozenieMacierzyCpp(m1.cols,m1.rows)
            m2C = MnozenieMacierzyCpp(m2.cols,m2.rows)
            m3C = MnozenieMacierzyCpp(m2.cols,m1.rows)
            if mainWindow.types.get() == "integer":
                m1.fillMatrix(m1From,m1To,True)
                m2.fillMatrix(m2From,m2To,True)
                convertTimeStart = timeit.timeit()
                m3C.convert(True)
                m1C.takeMatrixes(m1,True)
                m2C.takeMatrixes(m2,True)
                convertTimeEnd = timeit.timeit()
                for i in range(numOfRepeats):
                    cTimeStart = timeit.timeit()
                    MnozenieMacierzyCpp.computeInC(m1C.arg1,m2C.arg1,m3C.arg1,m3C.rows,m3C.cols,m1C.cols,True)
                    cTimeEnd = timeit.timeit()
                    timeStart = timeit.timeit()
                    m3 = MnozenieMacierzyPython.mnoz(m1,m2)
                    timeEnd = timeit.timeit()
            else:
                m1.fillMatrix(m1From,m1To,False)
                m2.fillMatrix(m2From,m2To,False)
                convertTimeStart = timeit.timeit()
                m3C.convert(False)
                m1C.takeMatrixes(m1,False)
                m2C.takeMatrixes(m2,False)
                convertTimeEnd = timeit.timeit()
                for i in range(numOfRepeats):
                    cTimeStart = timeit.timeit()
                    MnozenieMacierzyCpp.computeInC(m1C.arg1,m2C.arg1,m3C.arg1,m3C.rows,m3C.cols,m1C.cols,False)
                    cTimeEnd = timeit.timeit()
                    timeStart = timeit.timeit()
                    m3 = MnozenieMacierzyPython.mnoz(m1,m2)
                    timeEnd = timeit.timeit()
            m3C.printMatrix()
            printMatrix(mainWindow.matrixesTexts[0],m1)
            printMatrix(mainWindow.matrixesTexts[1],m2)
            
            printMatrix(mainWindow.matrixesTexts[2],m3)
            printToLogFrame(mainWindow.text,timeEnd-timeStart,convertTimeEnd-convertTimeStart,cTimeEnd-cTimeStart,numOfRepeats)



mainWindow = GUI()

try:
    f = open("src/logs/log.txt","r")
    lines = f.readlines()
    text = ""
    for i in lines:
        text += str(i)
    mainWindow.text.configure(state="normal")
    mainWindow.text.insert('1.0',text)
    mainWindow.text.configure(state="disabled") 
    
except Exception as e:
    print("there is no log file to read")
    print(e)

mainWindow.button.bind("<Button-1>",Run)
mainWindow.render()



