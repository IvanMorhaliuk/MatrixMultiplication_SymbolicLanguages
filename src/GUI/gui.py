import tkinter as tk
import tkinter.ttk as ttk

    
    
def changeMode(event):
    if mode.get() == "default":
        matrixesNotebook.place(relheight=1.0,relwidth=1.0)
        for i in range(2):
            m1HandSpinParam[i].grid_remove()
            m2HandSpinParam[i].grid_remove()
        for i in range(2):
            m1SpinParam[i].grid()
            m2SpinParam[i].grid()
    else:
        matrixesNotebook.place_forget()
        for i in range(2):
            m1SpinParam[i].grid_remove()
            m2SpinParam[i].grid_remove()
        for i in range(2):
            m1HandSpinParam[i].grid(column=i,row=1)
            m2HandSpinParam[i].grid(column=i,row=1)

root = tk.Tk()
root.title("Matrix Multiplication")
root.geometry('800x600')
root.minsize(width=500,height=550)





#MAIN FRAMES
body = ttk.Frame(root,style='bgLime.TFrame')
matrixesFrame = ttk.Frame(body,style='bgRed.TFrame')
logsFrame = ttk.Frame(body,style='bgBlue.TFrame')
configsFrame = ttk.Frame(body,style='bgGreen.TFrame')


#MATRIXESFRAME ELEMENTS
matrixesNotebook = ttk.Notebook(matrixesFrame)

matrixes = [ ttk.Frame(matrixesNotebook) for i in range(3)]
for i in range(2):
    matrixesNotebook.add(matrixes[i],text='matrix'+str(i+1))
matrixesNotebook.add(matrixes[2],text='result matrix')

matrixesTexts = [ tk.Text(matrixes[i],wrap="none",state='disabled') for i in range(3)]

matrixesXscrolls = [ ttk.Scrollbar(matrixes[i],orient="horizontal",command=matrixesTexts[i].xview) for i in range(3)]
matrixesYscrolls = [ ttk.Scrollbar(matrixes[i],orient="vertical",command=matrixesTexts[i].yview) for i in range(3)]

for i in range(3):
    matrixesTexts[i]['yscrollcommand'] = matrixesYscrolls[i].set
    matrixesTexts[i]['xscrollcommand'] = matrixesXscrolls[i].set

handMatrix1Label = ttk.Label(matrixesFrame,text="Matrix1")
handMatrix1Frame = ttk.Frame(matrixesFrame)
handMatrix1 = []
handMatrix2Label = ttk.Label(matrixesFrame,text="Matrix2")
handMatrix2Frame = ttk.Frame(matrixesFrame)
handMatrix2 = []
handMatrix3Label = ttk.Label(matrixesFrame,text="result")
handMatrix3 = tk.Text(matrixes[i],wrap="none",state='disabled')

#logsFrame elements
text = tk.Text(logsFrame,height=7,state='disabled')

#CONFIGFRAME ELEMENTS
panes = ttk.PanedWindow(configsFrame)

panesFrames = [ ttk.LabelFrame(panes,text="matrix " + str(i+1),width=100,height=100) for i in range(2)]

m1ParamLabels = [ttk.Label(panesFrames[0],text="Cols"),ttk.Label(panesFrames[0],text="Rows")]
m1RangeLabels = [ttk.Label(panesFrames[0],text="From:"),ttk.Label(panesFrames[0],text="To:")]
m1SpinParam = [ttk.Spinbox(panesFrames[0],from_=1,to=2000,width=4) for i in range(2)]
m1HandSpinParam = [ttk.Spinbox(panesFrames[0],from_=1,to=3,state='readonly',width=4) for i in range(2)]
m1SpinRange = [ttk.Spinbox(panesFrames[0],from_=1,to=2000,width=4) for i in range(2)]

m2ParamLabels = [ttk.Label(panesFrames[1],text="Cols"),ttk.Label(panesFrames[1],text="Rows")]
m2RangeLabels = [ttk.Label(panesFrames[1],text="From:"),ttk.Label(panesFrames[1],text="To:")]
m2SpinParam = [ttk.Spinbox(panesFrames[1],from_=1,to=2000,width=4) for i in range(2)]
m2HandSpinParam = [ttk.Spinbox(panesFrames[1],from_=1,to=3,state='readonly',width=4) for i in range(2)]
m2SpinRange = [ttk.Spinbox(panesFrames[1],from_=1,to=2000,width=4) for i in range(2)]

for i in range(2):
    panes.add(panesFrames[i])


typeLabel = ttk.Label(configsFrame,text='Type:')
types = ttk.Combobox(configsFrame,values=('integer','double'),state='readonly')
types.current(0)

modeLabel = ttk.Label(configsFrame,text='Mode:')
mode = ttk.Combobox(configsFrame,values=('default','hand'),state='readonly')
mode.current(0)
mode.bind("<<ComboboxSelected>>",changeMode)


button = ttk.Button(configsFrame,text="Run Calculations")



#Styles
for i in (body,matrixesFrame,logsFrame):
    i['padding'] = 15
configsFrame['padding'] = 20
ttk.Style().configure('bgRed.TFrame',background='red')
ttk.Style().configure('bgBlue.TFrame',background='blue')
ttk.Style().configure('bgLime.TFrame',background='lime')
ttk.Style().configure('bgGreen.TFrame',background='green')





#grid

body.place(relheight=1.0,relwidth=1.0)

matrixesFrame.place(relheight=0.8,relwidth=0.7)
matrixesNotebook.place(relheight=1.0,relwidth=1.0)
for i in matrixesTexts:
    i.place(relheight=1.0,relwidth=1.0)

logsFrame.place(rely=0.8,relheight=0.2,relwidth=0.8)

configsFrame.place(relx=0.7,relheight=1.0,relwidth=0.3)
for pl,sp,rl,sr in (m1ParamLabels,m1SpinParam,m1RangeLabels,m1SpinRange),(m2ParamLabels,m2SpinParam,m2RangeLabels,m2SpinRange):
    for i in range(2):
        pl[i].grid(column=i,row=0)
    for i in range(2):
        sp[i].grid(column=i,row=1)
    for i in range(2):
        rl[i].grid(column=i,row=2)
    for i in range(2):
        sr[i].grid(column=i,row=3)


panes.pack()
mode.pack()

root.mainloop()