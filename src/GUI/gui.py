import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.minsize(width=800, height=500)
#Styles
matrixesStyle = ttk.Style().configure('matrixesStyle.TFrame',background='red')
logsStyle = ttk.Style().configure('logsStyle.TFrame',background='blue')
configStyle = ttk.Style().configure('configStyle.TFrame',background='green')


#Main frames
body = ttk.Frame(root)
matrixes = ttk.Frame(body,width=500,height=300,style='matrixesStyle.TFrame')
logs = ttk.Frame(body,width=500,height=200,style='logsStyle.TFrame')
configs = ttk.Frame(body,width=300,height=500,style='configStyle.TFrame')





body.grid(column=0,row=0)

matrixes.grid(column=0,row=0)
logs.grid(column=0,row=1)
configs.grid(column=1,row=0,rowspan=2)



root.mainloop()