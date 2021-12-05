import numpy as np

class point2DMatrix:  #矩阵
    def __init__(self, cx=0.0, cy=0.0, w=100, h=100, m=10, n=10):
        self._cx = cx
        self._cy = cy
        self._w = w
        self._h = h
        self._m = m  # 行列
        self._n = n
        self._X = np.empty([m, n], dtype=float)  # X坐标的矩阵
        self._Y = np.empty([m, n], dtype=float)
        self._poss = np.empty([m * n, 2], dtype=float)  # 所有点的坐标矩阵 m*n行 2列
        
        self._A = np.zeros([m, n], dtype=float)  # 点阵中点的属性值矩阵
        lbx = self._cx - w / 2
        lby = self._cy - h / 2
        delta_x = w / n
        delta_y = h / m
        lbcx = lbx + delta_x / 2  # X_Mat= xmin+h/m *i +h/2m
        lbcy = lby + delta_y / 2
        for i in range(n):
            self._X[:, [i]] = lbcx + delta_x * i
        for j in range(m):
            self._Y[[j], :] = lbcy + delta_y * j
        self._updata_poss_byXY()

    def _updata_poss_byXY(self):
        tempX = self._X
        tempY = self._Y
        tempX = tempX.reshape(self._m * self._n, 1)
        tempY = tempY.reshape(self._m * self._n, 1)
        self._poss = np.c_[tempX, tempY]

    def _updata_XY_byposs(self):
        temp_left = self._poss[:, 0]
        temp_right = self._poss[:, 1]
        self._X = temp_left.reshape(self._m, self._n)
        self._X = temp_right.reshape(self._m, self._n)

    def pos(self, r, c):
        return self._X[r, c], self._Y[r, c]

    def updataXY(self, r, c, a, b):
        self._X[r, c] = a
        self._Y[r, c] = b

    def m(self):
        return self._m

    def n(self):
        return self._n

    def set_value(self, r, c, a):
        self._A[(r, c)] = a

    def set_values(self, A):
        self._A = A

    def get_value(self, r, c):
        return self._A[(r, c)]

    def get_values(self):
        return self._A

    def cordi_mx(self):
        return self._poss

    def ix_pos(self, ix):
        return self._poss[ix,:]
    
    def row_pos(self,r):
        r_ps = []
        for j in range(self._n):
            r_ps.append((self._X[r,j],self._Y[r,j]))
        return r_ps

    def col_pos(self,c):
        c_ps = []
        for i in range(self._m):
            c_ps.append((self._X[i,c],self._Y[i,c]))
        return c_ps

    def transform(self, T):
        x1 = self._cx * T[0][0] + self._cy * T[1][0] + T[2][0]
        y1 = self._cx * T[0][1] + self._cy * T[1][1] + T[2][1]
        npm = point2DMatrix(x1, y1, self._w, self._h, self._m, self._n)
        for i in range(self._m):
            for j in range(self._n):
                p = self.pos(i, j)
                a1 = p[0] * T[0][0] + p[1] * T[1][0] + T[2][0]
                b1 = p[0] * T[0][1] + p[1] * T[1][1] + T[2][1]
                npm.updataXY(i, j, a1, b1)
        return npm
