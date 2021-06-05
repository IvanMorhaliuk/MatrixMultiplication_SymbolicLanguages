import tkinter as tk
import tkinter.ttk as ttk
import re


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Matrix Multiplication")
        self.root.geometry('800x600')
        self.root.minsize(width=700,height=550)

        self.body = ttk.Frame(self.root)
        self.matrixesFrame = ttk.Frame(self.body)
        self.logsFrame = ttk.Frame(self.body)
        self.configsFrame = ttk.Frame(self.body)
        self.checkNumWrapper = (self.root.register(self.checkNum),'%P')
        self.checkNumWrapperT = (self.root.register(self.checkNum2),'%P')
        self.createMatrixesFrameElems()
        self.createLogsFrameElems()
        self.createConfigFrameElems()
        self.styles()
    
    def changeSpin(self,handSpinParam,handMatrix,handMatrixFrame,handMatrixVals):
        cols = int(handSpinParam[0].get())
        rows = int(handSpinParam[1].get())
        for i in handMatrix:
            for j in i:
                j.grid_remove()
        handMatrix.clear()
        handMatrixVals.clear()
        for i in range(rows):
            handMatrixVals.append([tk.StringVar() for j in range(cols)])
        for i in range(rows):
            for j in range(cols):
                handMatrixVals[i][j].set("0")
                

        for i in range(rows):
            handMatrix.append([ ttk.Entry(handMatrixFrame,textvariable=handMatrixVals[i][j],validate="key",validatecommand=self.checkNumWrapper,width=7) for j in range(cols)])
        for i in range(rows):
            for j in range(cols):
                handMatrix[i][j].grid(row=i,column=j)
    @staticmethod
    def checkNum(newval):
        return re.match('^[+-]?[0-9]*$',newval) is not None and len(newval) <= 5
    @staticmethod
    def checkNum2(newval):
        return re.match('^[+-]?([0-9]*[.])?[0-9]*$',newval) is not None and len(newval) <= 6
    
    def changeType(self,event):
        if self.types.get() == "integer":
            self.checkNumWrapper = (self.root.register(self.checkNum),'%P')
            self.changeSpin(self.m1HandSpinParam,self.handMatrix1,self.handMatrix1Frame,self.handMatrix1Vals)
            self.changeSpin(self.m2HandSpinParam,self.handMatrix2,self.handMatrix2Frame,self.handMatrix2Vals)
        else:
            self.checkNumWrapper = (self.root.register(self.checkNum2),'%P')
            self.changeSpin(self.m1HandSpinParam,self.handMatrix1,self.handMatrix1Frame,self.handMatrix1Vals)
            self.changeSpin(self.m2HandSpinParam,self.handMatrix2,self.handMatrix2Frame,self.handMatrix2Vals)

    def changeMode(self,event):
        if self.mode.get() == "default":
            self.handMatrix1Label.place_forget()
            self.handMatrix2Label.place_forget()
            self.handMatrix3Label.place_forget()
            self.handMatrix1Frame.place_forget()
            self.handMatrix2Frame.place_forget()
            self.handMatrix3Frame.place_forget()
            self.matrixesNotebook.place(relheight=1.0,relwidth=1.0)
            for i in range(2):
                self.m1HandSpinParam[i].grid_remove()
                self.m2HandSpinParam[i].grid_remove()
            for i in range(2):
                self.m1SpinParam[i].grid()
                self.m2SpinParam[i].grid()
            for i in range(2):
                self.m1SpinRange[i].grid()
                self.m2SpinRange[i].grid()
                self.m1RangeLabels[i].grid()
                self.m2RangeLabels[i].grid()
        else:
            cols1 = int(self.m1HandSpinParam[0].get())
            rows1 = int(self.m1HandSpinParam[1].get())
            cols2 = int(self.m2HandSpinParam[0].get())
            rows2 = int(self.m2HandSpinParam[1].get())
            for i in range(2):
                self.m1SpinRange[i].grid_remove()
                self.m2SpinRange[i].grid_remove()
                self.m1RangeLabels[i].grid_remove()
                self.m2RangeLabels[i].grid_remove()
                

            self.matrixesNotebook.place_forget()
            for i in range(2):
                self.m1SpinParam[i].grid_remove()
                self.m2SpinParam[i].grid_remove()
            for i in range(2):
                self.m1HandSpinParam[i].grid(column=i,row=1)
                self.m2HandSpinParam[i].grid(column=i,row=1)
            self.handMatrix1Label.place(x=0,y=0)
            self.handMatrix1Frame.place(x=0,rely=0.05)
            for i in range(rows1):
                for j in range(cols1):
                    self.handMatrix1[i][j].grid(row=i,column=j)
            self.handMatrix2Label.place(x=0,rely=0.25)
            self.handMatrix2Frame.place(x=0,rely=0.30)
            for i in range(rows2):
                for j in range(cols2):
                    self.handMatrix2[i][j].grid(row=i,column=j)
            self.handMatrix3Label.place(x=0,rely=0.50)
            self.handMatrix3Frame.place(x=0,rely=0.57,relwidth=1.0)
            self.handMatrix3.pack(anchor="w",fill="both")

    def createMatrixesFrameElems(self):
        self.matrixesNotebook = ttk.Notebook(self.matrixesFrame)

        self.matrixes = [ ttk.Frame(self.matrixesNotebook) for i in range(3)]
        for i in range(2):
            self.matrixesNotebook.add(self.matrixes[i],text='matrix'+str(i+1))
        self.matrixesNotebook.add(self.matrixes[2],text='result matrix')

        self.matrixesTexts = [ tk.Text(self.matrixes[i],wrap="none",state='disabled') for i in range(3)]

        self.matrixesXscrolls = [ ttk.Scrollbar(self.matrixes[i],orient="horizontal",command=self.matrixesTexts[i].xview) for i in range(3)]
        self.matrixesYscrolls = [ ttk.Scrollbar(self.matrixes[i],orient="vertical",command=self.matrixesTexts[i].yview) for i in range(3)]

        for i in range(3):
            self.matrixesTexts[i]['yscrollcommand'] = self.matrixesYscrolls[i].set
            self.matrixesTexts[i]['xscrollcommand'] = self.matrixesXscrolls[i].set

        self.handMatrix1Label = ttk.Label(self.matrixesFrame,text="Matrix1")
        self.handMatrix1Frame = ttk.Frame(self.matrixesFrame)
        
        self.handMatrix1Vals = []
        for i in range(3):
            self.handMatrix1Vals.append([tk.StringVar() for j in range(3)])
        self.handMatrix1 = []
        for i in range(3):
            self.handMatrix1.append([ ttk.Entry(self.handMatrix1Frame,textvariable=self.handMatrix1Vals[i][j],validate="key",validatecommand=self.checkNumWrapper,width=7) for j in range(3)])

        self.handMatrix2Label = ttk.Label(self.matrixesFrame,text="Matrix2")
        self.handMatrix2Frame = ttk.Frame(self.matrixesFrame)
        self.handMatrix2Vals = []
        for i in range(3):
            self.handMatrix2Vals.append([tk.StringVar() for j in range(3)])
        self.handMatrix2 = []
        for i in range(3):
            self.handMatrix2.append([ ttk.Entry(self.handMatrix2Frame,textvariable=self.handMatrix2Vals[i][j],validate="key",validatecommand=self.checkNumWrapper,width=7) for j in range(3)])

        for i in range(3):
            for j in range(3):
                self.handMatrix1Vals[i][j].set("0")
                self.handMatrix2Vals[i][j].set("0")
        


        self.handMatrix3Frame = ttk.Frame(self.matrixesFrame)
        self.handMatrix3Label = ttk.Label(self.matrixesFrame,text="result")
        self.handMatrix3 = tk.Text(self.handMatrix3Frame,wrap="none",state='disabled')

    def createLogsFrameElems(self):
        self.text = tk.Text(self.logsFrame,height=7,state='disabled')

    def createConfigFrameElems(self):
        self.panes = ttk.PanedWindow(self.configsFrame)

        self.panesFrames = [ ttk.LabelFrame(self.panes,text="matrix " + str(i+1),width=100,height=100) for i in range(2)]

        self.m1ParamLabels = [ttk.Label(self.panesFrames[0],text="Cols"),ttk.Label(self.panesFrames[0],text="Rows")]
        self.m1RangeLabels = [ttk.Label(self.panesFrames[0],text="From:"),ttk.Label(self.panesFrames[0],text="To:")]
        self.m1SpinParam = [ttk.Spinbox(self.panesFrames[0],from_=1,to=2000,validate="key",validatecommand=self.checkNumWrapper,width=4) for i in range(2)]
        self.m1HandSpinParamVal = [tk.StringVar(),tk.StringVar()]
        self.m1HandSpinParam = [ttk.Spinbox(self.panesFrames[0],from_=1,to=3,state='readonly',width=4,textvariable=self.m1HandSpinParamVal[i],command=lambda : self.changeSpin(self.m1HandSpinParam,self.handMatrix1,self.handMatrix1Frame,self.handMatrix1Vals)) for i in range(2)]
        self.m1SpinRange = [ttk.Spinbox(self.panesFrames[0],from_=1,to=2000,validate="key",validatecommand=self.checkNumWrapperT,width=4) for i in range(2)]

        for i in self.m1HandSpinParamVal:
            i.set("3")

        self.m2ParamLabels = [ttk.Label(self.panesFrames[1],text="Cols"),ttk.Label(self.panesFrames[1],text="Rows")]
        self.m2RangeLabels = [ttk.Label(self.panesFrames[1],text="From:"),ttk.Label(self.panesFrames[1],text="To:")]
        self.m2SpinParam = [ttk.Spinbox(self.panesFrames[1],from_=1,to=2000,validate="key",validatecommand=self.checkNumWrapper,width=4) for i in range(2)]
        self.m2HandSpinParamVal = [tk.StringVar(),tk.StringVar()]
        self.m2HandSpinParam = [ttk.Spinbox(self.panesFrames[1],from_=1,to=3,state='readonly',width=4,textvariable=self.m2HandSpinParamVal[i],command=lambda : self.changeSpin(self.m2HandSpinParam,self.handMatrix2,self.handMatrix2Frame,self.handMatrix2Vals)) for i in range(2)]
        self.m2SpinRange = [ttk.Spinbox(self.panesFrames[1],from_=1,to=2000,validate="key",validatecommand=self.checkNumWrapperT,width=4) for i in range(2)]

        for i in range(2):
            self.m1SpinParam[i].set("0")
            self.m2SpinParam[i].set("0")
            self.m1SpinRange[i].set("0")
            self.m2SpinRange[i].set("0")

        for i in self.m2HandSpinParamVal:
            i.set("3")

        for i in range(2):
            self.panes.add(self.panesFrames[i])


        self.typeLabel = ttk.Label(self.configsFrame,text='Type:')
        self.types = ttk.Combobox(self.configsFrame,values=('integer','double'),state='readonly')
        self.types.current(0)
        self.types.bind("<<ComboboxSelected>>",self.changeType)

        self.modeLabel = ttk.Label(self.configsFrame,text='Mode:')
        self.mode = ttk.Combobox(self.configsFrame,values=('default','hand'),state='readonly')
        self.mode.current(0)
        self.mode.bind("<<ComboboxSelected>>",self.changeMode)

        self.repeatsLabel = ttk.Label(self.configsFrame,text='Repeats:')
        self.repeats = ttk.Spinbox(self.configsFrame,from_=1,to=2000,validate="key",validatecommand=self.checkNumWrapper,width=4)
        self.repeats.set("1")

        self.button = ttk.Button(self.configsFrame,text="Run Calculations")

    def styles(self):
        for i in (self.body,self.matrixesFrame,self.logsFrame):
            i['padding'] = 15
        self.configsFrame['padding'] = 20

    def render(self):
        self.body.place(relheight=1.0,relwidth=1.0)

        self.matrixesFrame.place(relheight=0.8,relwidth=0.8)

        self.matrixesNotebook.place(relheight=1.0,relwidth=1.0)
        for i in self.matrixesTexts:
            i.place(relheight=1.0,relwidth=0.97)

        
            
            



        self.logsFrame.place(rely=0.8,relheight=0.2,relwidth=0.8)
        self.text.pack(anchor="w",fill="both")

        self.configsFrame.place(relx=0.8,relheight=1.0,relwidth=0.2)
        for pl,sp,rl,sr in (self.m1ParamLabels,self.m1SpinParam,self.m1RangeLabels,self.m1SpinRange),(self.m2ParamLabels,self.m2SpinParam,self.m2RangeLabels,self.m2SpinRange):
            for i in range(2):
                pl[i].grid(column=i,row=0)
            for i in range(2):
                sp[i].grid(column=i,row=1)
            for i in range(2):
                rl[i].grid(column=i,row=2)
            for i in range(2):
                sr[i].grid(column=i,row=3)


        self.panes.pack()
        self.modeLabel.pack(pady="5")
        self.mode.pack(pady="5")
        self.typeLabel.pack(pady="5")
        self.types.pack(pady="5")
        self.repeats.pack(pady="5")
        self.button.pack(pady="5")

        self.root.mainloop()