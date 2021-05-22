import tkinter as tk
import tkinter.ttk as ttk

""" def onChange():
    for i in entrys:
        i.grid_forget()
    entrys.clear()
    for i in range(int(spin.get())):
        entrys.append(ttk.Entry(root,width=4))
    for i in range(int(spin.get())):
        entrys[i].grid() """
    

root = tk.Tk()
root.title("Matrix Multiplication")
root.geometry('900x600')
root.resizable(False,False)

body = ttk.Frame(root,style='bgRed.TFrame')
matrixesFrame = ttk.Frame(body)
logsFrame = ttk.Frame(body)
configsFrame = ttk.Frame(body)

#

#STYLES
for i in (body,matrixesFrame,logsFrame):
    i['padding'] = 15
configsFrame['padding'] = 20

ttk.Style().configure('bgRed.TFrame',background='red')


""" spin = ttk.Spinbox(root,from_=1,to=3,values=("1","2","3"),state='readonly',width=4,command=onChange)
spin.grid()
entrys = []   """

#GRID
for i in (root,body,matrixesFrame,logsFrame):
    i.columnconfigure(1, weight=1)
    i.rowconfigure(1, weight=1)
body.grid(column=0,row=0,columnspan=2,rowspan=2,sticky="nsew")
for i in range(3):
    ttk.Label(body,text="zhopa").grid(row=0,column=i,sticky="w")
root.mainloop()