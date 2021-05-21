import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Matrix Multiplication")
root.geometry('800x600')
root.minsize(width=500,height=550)
#root.minsize(width=800, height=500)




#Main frames
body = ttk.Frame(root)
matrixesFrame = ttk.Frame(body)
logsFrame = ttk.Frame(body)
configsFrame = ttk.Frame(body)


#matrixesFrame elements
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


#logsFrame elements
text = tk.Text(logsFrame,height=7,state='disabled')

#configFrame elements
panes = ttk.PanedWindow(configsFrame)

panesFrames = [ ttk.LabelFrame(panes,text="matrix " + str(i+1),width=100,height=100) for i in range(2)]
spinBoxesM1 = [ttk.Spinbox(panesFrames[0],from_=1,to=2000,textvariable=tk.StringVar()) for i in range(4)]
spinBoxesM2 = [ttk.Spinbox(panesFrames[1],from_=1,to=2000,textvariable=tk.StringVar()) for i in range(4)]
i=0
for item in (spinBoxesM1,spinBoxesM2):
    ttk.Label(panesFrames[i],text='Columns:').pack()
    item[0].pack()
    ttk.Label(panesFrames[i],text='Rows:').pack()
    item[1].pack()
    ttk.Label(panesFrames[i],text='From:').pack()
    item[2].pack()
    ttk.Label(panesFrames[i],text='To:').pack()
    item[3].pack()
    i+=1
for i in range(2):
    panes.add(panesFrames[i])

types = ttk.Combobox(configsFrame,values=('integer','double'),state='readonly')
types.current(0)
mode = ttk.Combobox(configsFrame,values=('default','hand'),state='readonly')
mode.current(0)

checkVal = tk.BooleanVar(value=False)
check = ttk.Checkbutton(configsFrame,text="Strict",variable=checkVal)
typeLabel = ttk.Label(configsFrame,text='Type:')
modeLabel = ttk.Label(configsFrame,text='Mode:')
button = ttk.Button(configsFrame,text="Run Calculations")



#Styles
for i in (body,matrixesFrame,logsFrame):
    i['padding'] = 15
configsFrame['padding'] = 20

#configures
for i in (root,body,matrixesFrame,logsFrame):
    i.columnconfigure(1, weight=1)
    i.rowconfigure(1, weight=1)


for i in range(3):
    matrixes[i].columnconfigure(1,weight=1)
    matrixes[i].rowconfigure(1,weight=1)


#grid
body.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")

matrixesFrame.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")
matrixesNotebook.grid(column=0,row=0,columnspan=2,rowspan=2,sticky='nsew')

for i in range(3):
    matrixesTexts[i].grid(column=0,row=0,columnspan=2,rowspan=2,sticky='nsew')
for i in range(3):
    matrixesYscrolls[i].grid(column=1,row=0,rowspan=2,sticky="nse")
    matrixesXscrolls[i].grid(column=0,row=1,columnspan=2,sticky="sew")

logsFrame.grid(column=0,row=2,columnspan=2,sticky="ew")
text.grid(column=0,row=0,columnspan=2,sticky='ew')

configsFrame.grid(column=2,row=1,rowspan=2,sticky="ns")
panes.grid(column=0,row=0)
typeLabel.grid()
types.grid()
modeLabel.grid()
mode.grid()
check.grid(sticky="e")
button.grid(sticky="w")
root.mainloop()