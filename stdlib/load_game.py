from pygame.gfxdraw import bezier, box
from . import stddraw, point2DMatrix, draw, move
import time, numpy
from pygame import math
class start_game:
    def __init__(self, n, m, filename, root, type_op):
        root.destroy()
        if type_op == "load":
            stddraw.setCanvasSize(800,800)
            stddraw.setXscale(-50,50)
            stddraw.setYscale(-50,50)
        self.filename = filename
        self.gap = 100 / max(m, n)
        self.np = point2DMatrix.point2DMatrix(0, 0, (int)(self.gap * m), (int)(self.gap * n), n, m)
        self.n = n
        self.m = m
        self.pos1 = -1
        self.pos2 = -1
        self.pos3 = -1
        #print(n, m)
        f = open(filename, 'r')
        start = f.read()
        for i in range(n):
            for j in range(m):
                #print(i * m + j)
                self.np.set_value(i, j, int(start[i * m + j]))

        self.find_pos()
        if self.pos1 == -1 or self.pos2 == -1 or self.pos3 == -1:
            print("Map Error")
            exit()
        f.close()
        draw.draw(n, m, self.gap / 2, self.np)
        stddraw.show(60)
        self.manual()
    def manual(self):
        flag = 0
        while True:
            stddraw.show(60)
            self.find_pos()
            if stddraw.hasNextKeyTyped():
                k = stddraw.nextKeyTyped()
                if k == 's':
                    #print(self.pos1)
                    flag = move.move(self.pos1, -1, 0, self.np)
                if k == 'a':
                    flag = move.move(self.pos1, 0, -1, self.np)
                if k == 'w':
                    flag = move.move(self.pos1, 1, 0, self.np)
                if k == 'd':
                    flag = move.move(self.pos1, 0, 1, self.np)
                if k == 'q' or flag == 1:
                    break
                if k == 'p':
                    f = open(self.filename, 'w')
                    store = ""
                    for i in range(self.n):
                        for j in range(self.m):
                            p = self.np.get_value(i,j)
                            print(str(int(p)))
                            store += str(int(p))
                    f.write(store)
                    f.flush()
                    f.close()
                if k == 'm':
                    self.find_pos()
                    self.auto()
                    flag = 1
                    break
                draw.draw(self.n, self.m, self.gap / 2, self.np)
        if(flag == 1):
            print("Win!")
    def auto(self):
        boxpath = []
        #print(1)
        boxpath = self.min_path(self.pos2, self.pos3)
        if boxpath[0] == -1:
            print("You loss")
            exit()
        
        tt = boxpath[-1]
        boxpath.pop()
        
        while len(boxpath):
            stddraw.show(60)
            playerpath = []
            self.find_pos()
            playerpath = self.min_path(self.pos1, tt - boxpath[-1] + tt)
            print(playerpath)
            pp = playerpath[-1]
            playerpath.pop()
            while len(playerpath):
                stddraw.show(60)
                time.sleep(1)
                self.np.set_value((int)(pp / self.m),(int)(pp % self.m), 0)
                pp = playerpath[-1]
                playerpath.pop()
                self.np.set_value((int)(pp / self.m),(int)(pp % self.m), 2)
                draw.draw(self.n, self.m, self.gap / 2, self.np)
            stddraw.show(60)
            self.np.set_value( (int)((tt - boxpath[-1] + tt) / self.m), (int)((tt - boxpath[-1] + tt) % self.m), 0)
            self.np.set_value((int)(tt / self.m),(int)(tt % self.m), 2)
            
            tt = boxpath[-1]
            boxpath.pop()
            time.sleep(1)
            self.np.set_value((int)(tt / self.m),(int)(tt % self.m), 3)
            draw.draw(self.n, self.m, self.gap / 2, self.np)
    def min_path(self, a, b):
        if a == b:
            return [b]
        dist = numpy.ndarray( [self.n * self.m], int)
        st = numpy.ndarray([self.n * self.m], bool)
        
        for i in range(self.n * self.m):
            dist[i] = 1e4
            st[i] = False
        
        dist[a] = 0
        
        for i in range(self.n * self.m):
            t = -1
            for j in range(self.n * self.m):
                if not st[j] and (t == -1 or dist[t] > dist[j]):
                    t = j
            st[t] = True

            if (int)(t / self.m)  > 0:
                dist[t - self.m] = min(dist[t - self.m], dist[t] + 1)
                if self.np.get_value( (int)(t / self.m) - 1, t % self.m) > 0:
                    dist[t - self.m] = 1e4
            
            if (int)(t / self.m)  < self.n - 1:
                dist[t + self.m] = min(dist[t + self.m], dist[t] + 1)
                if self.np.get_value( (int)(t / self.m) + 1, t % self.m) > 0:
                    dist[t + self.m] = 1e4
            if t % self.m  < self.m - 1:
                dist[t + 1] = min(dist[t+1], dist[t] + 1)
                if self.np.get_value( (int)(t / self.m) , t % self.m + 1) > 0:
                    dist[t + 1] = 1e4
            if t % self.m  > 0:
                dist[t - 1] = min(dist[t-1], dist[t] + 1)
                if self.np.get_value( (int)(t / self.m), t % self.m - 1) > 0:
                    dist[t - 1] = 1e4
        dist[a] = 0
        #print(dist)
        minpath = []
        minpath.append(b)
        
        if dist[b] > 1e4:
            return [-1]
        else:
            
            while True:
                buf_pos = minpath[-1]
                st[(int)(buf_pos)] = False
                buf_value = 1e9
                target_pos = 0
                if (int)(buf_pos / self.m)  > 0 and st[buf_pos - self.m]:
                    buf_value = min(buf_value, dist[buf_pos - self.m])
                    if buf_value == dist[buf_pos - self.m]:
                        target_pos = buf_pos - self.m
                if (int)(buf_pos / self.m)  < self.n - 1 and st[buf_pos + self.m]:
                    buf_value = min(buf_value, dist[buf_pos + self.m])
                    if buf_value == dist[buf_pos + self.m]:
                        target_pos = buf_pos + self.m
                if buf_pos % self.m  > 0 and st[buf_pos - 1]:
                    buf_value = min(buf_value, dist[buf_pos - 1])
                    if buf_value == dist[buf_pos - 1]:
                        target_pos = buf_pos - 1
                if buf_pos % self.m  < self.m - 1 and st[buf_pos + 1]:
                    buf_value = min(buf_value, dist[buf_pos + 1])
                    if buf_value == dist[buf_pos + 1]:
                        target_pos = buf_pos + 1
                
                minpath.append(target_pos)
                if target_pos == a:
                    return minpath
            
            
    def find_pos(self):
        #print(self.pos1, self.pos2, self.pos3)
        for i in range(self.n):
            for j in range(self.m):
                if (int)(self.np.get_value(i,j)) == 2:
                    self.pos1 = i * self.m + j
                if (int)(self.np.get_value(i,j)) == 3:
                    self.pos2 = i * self.m + j
                if (int)(self.np.get_value(i,j)) == 4:
                    self.pos3 = i * self.m + j
