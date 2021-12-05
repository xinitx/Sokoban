
from . import point2DMatrix, stddraw, draw, load_game
import tkinter
import time
class create_map:
    def __init__(self,root, n, m, filename):
        self.n = n
        self.m = m
        self.filename = filename
        root.destroy()
        stddraw.setCanvasSize(800, 800)
        stddraw.setXscale(-50,50)
        stddraw.setYscale(-50,50)
        
        gap = 100 / max(m, n)
        np = point2DMatrix.point2DMatrix(0, 0, (int)(gap * m), (int)(gap * n), n, m)

        for i in range(n):
            for j in range(m):
                np.set_value(i, j, 0)
        draw.draw( n, m, gap / 2, np)

        running = True
        while running:
            stddraw.show(60)
            if stddraw.mousePressed():
                x = stddraw.mouseX()
                y = stddraw.mouseY()

                mid1 = int( (x + (gap * m / 2)) / gap)
                mid2 = int( (y + (gap * n / 2)) /gap)
                if mid1 < m and mid2 < n:
                    np.set_value(mid2, mid1, 1)
                draw.draw(n, m, gap / 2, np)
            
            if stddraw.hasNextKeyTyped():
                k = stddraw.nextKeyTyped()
                if k == 's':
                    running  = False
        self.create_other( n, m, gap, np)
    def create_other( self, n, m, gap, np):
        f = open(self.filename, 'w')
        print("请选择人物、箱子、终点")
        running = True
        p = 2
        while running:
            stddraw.show(60)
            if stddraw.mousePressed():
                x = stddraw.mouseX()
                y = stddraw.mouseY()
                mid1 = int( (x + (gap * m / 2)) / gap)
                mid2 = int( (y + (gap * n / 2)) / gap)
                if mid1 < m and mid2 < n and np.get_value(mid2, mid1) == 0:
                    np.set_value(mid2, mid1, p)
                    p += 1
                    draw.draw(n, m, gap / 2, np)
            if p >= 5:
                running = False
                stddraw.show(60)
        start = ""
        
        for i in range(n):
            for j in range(n):
                p = np.get_value(i,j)
                print(str(int(p)))
                start += str(int(p))
        f.write(start)
        f.flush()
        f.close()
        print("开始游戏")
        buf = tkinter.Tk()
        load_game.start_game(self.n, self.m, self.filename, buf, "create")