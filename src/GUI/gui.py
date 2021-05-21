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
matrixes = ttk.Notebook(matrixesFrame)
matrix1 = ttk.Frame(matrixes)
matrix2 = ttk.Frame(matrixes)
resultMatrix = ttk.Frame(matrixes)
matrixes.add(matrix1,text='matrix1')
matrixes.add(matrix2,text='matrix2')
matrixes.add(resultMatrix,text='resultMatrix')

matrix1text = tk.Text(matrix1,wrap="none")
matrix1Yscroll = ttk.Scrollbar(matrix1,orient="vertical",command=matrix1text.yview)
matrix1Xscroll = ttk.Scrollbar(matrix1,orient="horizontal",command=matrix1text.xview)
matrix1text['yscrollcommand']=matrix1Yscroll.set
matrix1text['xscrollcommand']=matrix1Xscroll.set

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
matrix1text['state'] = 'disabled'

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
matrix1.columnconfigure(1, weight=1)
matrix1.rowconfigure(1, weight=1)

logsFrame.columnconfigure(1, weight=1)
logsFrame.rowconfigure(1, weight=1)

#grid
body.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")

matrixesFrame.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")
matrixes.grid(column=0,row=0,columnspan=2,rowspan=2,sticky='nsew')
matrix1text.grid(column=0,row=0,columnspan=2,rowspan=2,sticky='nsew')
matrix1Yscroll.grid(column=1,row=0,rowspan=2,sticky="nse")
matrix1Xscroll.grid(column=1,row=0,rowspan=2,sticky="sew")


logsFrame.grid(column=0,row=2,columnspan=2,sticky="ew")
text.grid(column=0,row=0,columnspan=2,sticky='ew')

configsFrame.grid(column=2,row=1,rowspan=2,sticky="ns")
panes.grid(column=0,row=0)



root.mainloop()