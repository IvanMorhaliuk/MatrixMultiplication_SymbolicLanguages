import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Matrix Multiplication")
root.geometry('800x500')
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
text = tk.Text(logsFrame,height=7)

#configFrame elements
panes = ttk.PanedWindow(configsFrame)
matrix1Label = ttk.LabelFrame(panes,text="matrix1",width=100,height=100)
matrix2Label = ttk.LabelFrame(panes,text="matrix2",width=100,height=100)
panes.add(matrix1Label)
panes.add(matrix2Label)

#Styles
body['padding'] = 15


matrixesFrame['padding'] = 15
matrixesFrameStyle = ttk.Style().configure('matrixesFrame.TFrame',background='red',borderwidth=5,relief='solid')


logsFrame['padding'] = 15
logsFrameStyle = ttk.Style().configure('logsFrame.TFrame',background='blue',borderwidth=5,relief='solid')
text['state'] = 'disabled'

configsFrame['padding'] = 20
configsFrameStyle = ttk.Style().configure('configsFrame.TFrame',background='orange',borderwidth=5,relief='solid')








#configures
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

body.columnconfigure(1, weight=1)
body.rowconfigure(1, weight=1)

matrixesFrame.columnconfigure(1, weight=1)
matrixesFrame.rowconfigure(1, weight=1)

for i in range(3):
    matrixes[i].columnconfigure(1,weight=1)
    matrixes[i].rowconfigure(1,weight=1)


logsFrame.columnconfigure(1, weight=1)
logsFrame.rowconfigure(1, weight=1)

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



root.mainloop()