from . import point2DMatrix, stddraw

def draw(n, m, gap, np):
    stddraw.clear(stddraw.WHITE)
    for i in range(n):
        for j in range(m):
            p = np.pos(i, j)
             #间隔
            stddraw.setPenColor(stddraw.GRAY)
            stddraw.square(p[0], p[1], gap)
            if np.get_value(i, j) > 0.1:
                stddraw.setPenColor(stddraw.BLACK)  #墙
                stddraw.filledSquare(p[0], p[1], gap - gap / 5)
            if np.get_value(i, j) > 1.5 and np.get_value(i, j) < 2.5:
                stddraw.setPenColor(stddraw.YELLOW) #人物
                stddraw.filledSquare(p[0], p[1], gap  - gap / 5)
            if np.get_value(i, j) > 2.5 and np.get_value(i, j) < 3.5:
                stddraw.setPenColor(stddraw.RED)   #箱子
                stddraw.filledSquare(p[0], p[1], gap  - gap / 5)
            if np.get_value(i, j) > 3.5 and np.get_value(i, j) < 4.5:
                stddraw.setPenColor(stddraw.GREEN)  #终点
                stddraw.filledSquare(p[0], p[1], gap  - gap / 5)

def test():
    n = 5
    m = 8
    np = point2DMatrix.point2DMatrix(0, 0, 100, 100, n, n)
    draw( n, m, np)
    stddraw.show()
if __name__ == '__main__':
    test()