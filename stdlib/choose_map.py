import os
import tkinter
from . import create_map, load_game
class choose_map:
    def __init__(self, root, n, m):
        self.n = n
        self.m = m
        self.root = root
        file_dir = "./Maps"
        self.file_buf = file_dir + "/" + str(n) + "_" + str(m)
        if not os.path.exists(self.file_buf):
            os.makedirs(self.file_buf)
        for  buf, dirs, self.files in os.walk(self.file_buf, topdown=False):
            True

        textvar = tkinter.StringVar()
        infoL = tkinter.Label(root, textvariable = textvar)
        infoL.grid(row=1, column=2)
        self.row = 1

        button = []
        if len(self.files) <= 0:
            textvar.set("当前没有地图")
        else:
            textvar.set("当前地图")
            
            for i in range(len(self.files)):
                button_buf = tkinter.Label(root, text = self.files[i])
                self.row += 1
                button_buf.grid(row=self.row, column=2)
                button.append(buf)

        self.createE = tkinter.Entry(root)
        self.createE.grid(row=self.row + 1, column=2)

        create = tkinter.Button(root, text="创建地图", command= self.create_amap)
        create.grid(row = self.row + 2, column=1)

        load = tkinter.Button(root, text="加载地图", command= self.load_map)
        load.grid(row = self.row + 2, column= 3)
    def create_amap(self):
        if(self.createE.get() != ""):
            create_map.create_map(self.root, self.n, self.m, self.file_buf + "/" + self.createE.get())
    def load_map(self):
        if self.files.count(self.createE.get()):
            load_game.start_game(self.n, self.m, self.file_buf + "/" + self.createE.get(), self.root, "load")
        else:
            textvar_error = tkinter.StringVar()
            error = tkinter.Label(self.root, textvariable = textvar_error)
            error.grid(row=self.row + 1, column=3)
            textvar_error.set("请输入正确的地图")

