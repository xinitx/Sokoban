import stddraw
class PointGrid(object):        #点阵
    # 给定行、列数定义一个点阵d
    def __init__(self, m=10, n=10):
        # 点阵的行数
        self.m = m
        # 点阵的列数
        self.n = n
        self.q = {}
        self._A = {}
        for i in range(self.n * self.m):
            self.q[i] = i
        for r in range(self.m):
            for c in range(self.n):
                key = r * self.n + c
                self._A[key] = 0
    # 设置点阵中点(r,c)的属性值为 a
    def set_attr(self, r, c, a):
        key = r * self.n + c
        self._A[key] = a

    # 设置点阵中第ix个点的属性值为a
    def set_attr_bykey(self, key, a):
        self._A[key] = a

    # 将点阵属性值矩阵置为 A. 应确保A为m行,n列矩阵
    def set_attrs(self, dict):
        self._A = dict
    def _key(self, r, c):
        return r * self.n + c

    def _r_c(self, key):
        return (int(key / self.n), key % self.n)
    def find(self, buf):
            if(self.q[buf] != buf):
                self.q[buf] = self.find(self.q[buf])
            return self.q[buf]
    def get_attr(self, r, c):
        key = r * self.n + c
        return self._A[key]
    def get_attrs(self):
        return self._A
    # 根据点的序号取出其属性值
    def get_attr_bykey(self, key):
        return self._A[key]
    def update(self):
        for i in range(self.n * self.m):
            mid = self.neighors_keys(i)
            if not mid == []:
                for j in range(len(mid)):
                    self.q[mid[j]] = self.find(self.q[i])
    # 返回点阵中ix点的left、right、up、down四个邻居点的pix
    # 不存在的邻居点返回 -1
    def neighors_keys(self, key, box_pos = -1):
        r = self._r_c(key)[0]
        c = self._r_c(key)[1]
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        neig = []
        
        for i in range(4):
            if c + dx[i] >= 0 and r + dy[i] >= 0 and r + dy[i] <= self.m - 1 and c + dx[i] <= self.n - 1:
                if box_pos == -1:
                    if r - dy[i] >= 0 and c - dx[i] >= 0 and r - dy[i] <= self.m - 1 and c - dx[i] <= self.n - 1:
                        
                        if self._A[self._key(r - dy[i], c - dx[i])] == 0 or self._A[self._key(r - dy[i], c - dx[i])] == 2:
                            neig.append(self._key(r + dy[i], c + dx[i]))
                            
                else:
                    if not self._A[self._key(r + dy[i], c + dx[i])] == 1 and not self._key(r + dy[i], c + dx[i]) == box_pos:
                            neig.append(self._key(r + dy[i], c + dx[i]))
                            
        return neig

    # 返回点阵属性值矩阵置为 A
    def get_attrs(self):
        return self._A

    def m(self):
        return self.m

    def n(self):
        return self.n

    def show(self):
        stddraw.clear(stddraw.WHITE)
        pos = {}
        for i in range(self.m):
            for j in range(self.n):
                if self.get_attr(i, j) == 0:
                    stddraw.setPenColor(stddraw.GRAY)
                    stddraw.square(j + 0.5,self.n - 1 - i + 0.5, 0.5)
                if self.get_attr(i, j) == 1:
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.filledSquare( j + 0.5,self.n - 1 -  i + 0.5, 0.5)
                if self.get_attr(i, j) == 2:
                    stddraw.setPenColor(stddraw.YELLOW)
                    stddraw.filledSquare( j + 0.5,self.n - 1 -  i + 0.5, 0.5)
                    pos[0] = self._key(i, j)
                if self.get_attr(i, j) == 3:
                    stddraw.setPenColor(stddraw.RED)
                    stddraw.filledSquare( j + 0.5,self.n - 1 -  i + 0.5, 0.5)
                    pos[1] = self._key(i, j)
                if self.get_attr(i, j) == 4:
                    stddraw.setPenColor(stddraw.GREEN)
                    stddraw.filledSquare( j + 0.5,self.n - 1 -  i + 0.5, 0.5)
                    pos[2] = self._key(i, j)
        return pos

