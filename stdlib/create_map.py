
from . import point2DMatrix, stddraw, draw, load_game
import tkinter
class create_map:
    def __init__(self,root, n, m, filename):
        self.n = n
        self.m = m
        self.filename = filename
        root.destroy()
        stddraw.setCanvasSize(800,800)
        stddraw.setXscale(-50,50)
        stddraw.setYscale(-50,50)
        np = point2DMatrix.point2DMatrix(0, 0, 100, 100, n, m)

        for i in range(n):
            for j in range(n):
                np.set_value(i, j, 0)
        draw.draw(n, np)

        running = True
        while running:
            stddraw.show(60)
            if stddraw.mousePressed():
                x = stddraw.mouseX()
                y = stddraw.mouseY()

                #print(int( (x + 50) *  n / 100), int((y + 50) *  n / 100))
                mid1 = int( (x + 50) *  n / 100)
                mid2 = int( (y + 50) *  n / 100)
                np.set_value(mid2, mid1, 1)
                draw.draw(n, np)
            
            if stddraw.hasNextKeyTyped():
                k = stddraw.nextKeyTyped()
                if k == 's':
                    running  = False
        self.create_other( n, m, np)
    def create_other( self, n, m, np):
        
        print("请选择人物、箱子、终点")
        running = True
        p = 2
        while running:
            stddraw.show(60)
            if stddraw.mousePressed():
                x = stddraw.mouseX()
                y = stddraw.mouseY()
                mid1 = int( (x + 50) *  n / 100)
                mid2 = int( (y + 50) *  n / 100)
                if np.get_value(mid2, mid1) == 0:
                    np.set_value(mid2, mid1, p)
                    p += 1
                    draw.draw(n, np)
            if p == 5:
                running = False
                stddraw.show(60)
        start = ""
        f = open(self.filename, 'w')
        for i in range(n):
            for j in range(n):
                p = np.get_value(i,j)
                #print(str(int(p)))
                start += str(int(p))
        f.write(start)
        f.flush()
        print("开始游戏")
        buf = tkinter.Tk()
        load_game.start_game(self.n, self.m, self.filename, buf, "create")