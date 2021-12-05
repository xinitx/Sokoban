from . import point2DMatrix, stddraw

def draw(n, np):
    stddraw.clear(stddraw.WHITE)
    for i in range(n):
        for j in range(n):
            p = np.pos(i, j)
            if np.get_value(i, j) == 0:             #间隔
                stddraw.setPenColor(stddraw.GRAY)
                stddraw.square(p[0], p[1], 50 * 1.0 / n)
            if np.get_value(i, j) == 1:
                stddraw.setPenColor(stddraw.BLACK)  #墙
                stddraw.filledSquare(p[0], p[1], 50 * 1.0 / n)
            if np.get_value(i, j) == 2:
                stddraw.setPenColor(stddraw.YELLOW) #人物
                stddraw.filledSquare(p[0], p[1], 50 * 1.0 / n)
            if np.get_value(i, j) == 3:
                stddraw.setPenColor(stddraw.RED)   #箱子
                stddraw.filledSquare(p[0], p[1], 50 * 1.0 / n)
            if np.get_value(i, j) == 4:
                stddraw.setPenColor(stddraw.GREEN)  #终点
                stddraw.filledSquare(p[0], p[1], 50 * 1.0 / n)

def test():
    n = 5
    np = point2DMatrix.point2DMatrix(0, 0, 100, 100, n, n)
    draw(n, np)
    stddraw.show()
if __name__ == '__main__':
    test()