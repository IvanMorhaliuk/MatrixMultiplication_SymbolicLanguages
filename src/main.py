from GUI.gui import *
from tkinter import messagebox
import matrixes.MnozenieMacierzyPython as mmp
def Run(event):
    if (mainWindow.mode.get() == "hand"):
        m1 = mmp.MnozenieMacierzyPython(int(mainWindow.m1HandSpinParam[0].get()),int(mainWindow.m1HandSpinParam[1].get()))
        m1.readFromEntries(mainWindow.handMatrix1)
        m1.printMatrix()
        print()
        m2 = mmp.MnozenieMacierzyPython(int(mainWindow.m2HandSpinParam[0].get()),int(mainWindow.m2HandSpinParam[1].get()))
        m2.readFromEntries(mainWindow.handMatrix2)
        m2.printMatrix()
        print()
        try:
            if (not m1.ifMultipliable(m2)):
                raise Exception("Wrong dimentions!")
            
        except Exception as e:
            messagebox.showerror(message=e)
        else:
            m3 = mmp.MnozenieMacierzyPython.multiplicatePython(m1,m2)
            m3.printMatrix()


mainWindow = GUI()
mainWindow.button.bind("<Button-1>",Run)
mainWindow.render()



