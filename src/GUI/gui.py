import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
#root.minsize(width=800, height=500)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)



#Main frames
body = ttk.Frame(root,style='body.TFrame')
body.columnconfigure(1, weight=1)
body.rowconfigure(1, weight=1)

matrixesFrame = ttk.Frame(body,style='matrixesFrame.TFrame')


logsFrame = ttk.Frame(body,style='logsFrame.TFrame')
configsFrame = ttk.Frame(body,style='configsFrame.TFrame')


#matrixesFrame elements
matrixes = ttk.Notebook(matrixesFrame)
matrix1 = ttk.Frame(matrixes)
matrix2 = ttk.Frame(matrixes)
resultMatrix = ttk.Frame(matrixes)
matrixes.add(matrix1,text='matrix1')
matrixes.add(matrix2,text='matrix2')
matrixes.add(resultMatrix,text='resultMatrix')

#logsFrame elements
text = tk.Text(logsFrame,width=40,height=10).pack()

#configFrame elements
panes = ttk.PanedWindow(configsFrame)
matrix1Label = ttk.LabelFrame(panes,text="matrix1",width=100,height=100)
matrix2Label = ttk.LabelFrame(panes,text="matrix2",width=100,height=100)
panes.add(matrix1Label)
panes.add(matrix2Label)

#Styles
body['padding'] = 15
bodyStyle = ttk.Style().configure('body.TFrame',background='lime',borderwidth=5,relief='solid')

matrixesFrame['padding'] = 15
matrixesFrameStyle = ttk.Style().configure('matrixesFrame.TFrame',background='red',borderwidth=5,relief='solid')

logsFrame['padding'] = 15
logsFrameStyle = ttk.Style().configure('logsFrame.TFrame',background='blue',borderwidth=5,relief='solid')

configsFrame['padding'] = 15
configsFrameStyle = ttk.Style().configure('configsFrame.TFrame',background='orange',borderwidth=5,relief='solid')








#grid
body.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")

matrixesFrame.grid(column=0,row=0,sticky="nsew")
matrixes.grid(column=0,row=0)

logsFrame.grid(column=0,row=1,sticky="sew")

configsFrame.grid(column=1,row=0,rowspan=2,sticky="nse")
panes.grid(column=0,row=0)



root.mainloop()