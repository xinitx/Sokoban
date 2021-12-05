from time import sleep
import os
import tkinter
from stdlib import stddraw, point2DMatrix, load_game, choose_map, create_map, move, draw

class input_size:
    def __init__(self, root):
        root.minsize(400, 100)
        root.title("请输入地图大小")
    
        self.root = root

        self.rowL = tkinter.Label(root, text="行数：")  
        self.rowL.grid(row=1,column=1)
        self.rowE = tkinter.Entry(root)
        self.rowE.grid(row=1, column=2)

        self.colL = tkinter.Label(root, text="列数：" )  
        self.colL.grid(row=2,column=1)
        self.colE = tkinter.Entry(root)
        self.colE.grid(row=2, column=2)
        
        self.sizeB = tkinter.Button(root, text="确定", command=self.running)
        self.sizeB.grid(row=4, column=2)

        self.textvar1 = tkinter.StringVar()
        self.info1L = tkinter.Label(root, textvariable =self.textvar1)
        self.info1L.grid(row=1, column=3)
        
        self.textvar2 = tkinter.StringVar()
        self.info2L = tkinter.Label(root, textvariable =self.textvar2)
        self.info2L.grid(row=2, column=3)
    def running(self):
        
        row = self.rowE.get()
        col = self.colE.get()
        if not row.isdigit() or int(row) <= 2:
            self.textvar1.set("需要大于2的整数")
        else:
            self.textvar1.set("")
        if not col.isdigit() or int(col) <= 2:
            self.textvar2.set("需要大于2的整数")
        else:
            self.textvar2.set("")
        if row.isdigit() and col.isdigit():
            n = int(row)
            m = int(col)
            if n >= 3 and m >= 3:
                self.sizeB.destroy()
                self.rowL.destroy()
                self.rowE.destroy()
                self.colL.destroy()
                self.colE.destroy()
                choose_map.choose_map(self.root, n, m)
                
root = tkinter.Tk()
input_size(root)
root.mainloop()