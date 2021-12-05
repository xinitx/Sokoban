from . import stddraw, point2DMatrix, draw, move
import time
class start_game:
    def __init__(self, n, m, filename, root, type_op):
        root.destroy()
        if type_op == "load":
            stddraw.setCanvasSize(800,800)
            stddraw.setXscale(-50,50)
            stddraw.setYscale(-50,50)

        gap = 100 / max(m, n)
        np = point2DMatrix.point2DMatrix(0, 0, (int)(gap * m), (int)(gap * n), n, m)

        f = open(filename, 'r')
        start = f.read()
        posx = 0
        posy = 0
        jud = False
        for i in range(n):
            for j in range(n):
                np.set_value(i, j, int(start[i * n + j]))
                if int(start[i * n + j]) == 2:
                    jud = True
                    posx = i
                    posy = j
        if not jud:
            exit()
        f.close()
        draw.draw(n, m, gap / 2, np)
        running = True
        flag = 0
        pos = [posx, posy]
        while running:
            stddraw.show(60)
            if stddraw.hasNextKeyTyped():
                k = stddraw.nextKeyTyped()
                if k == 's':
                    flag = move.move(pos, -1, 0, np)
                if k == 'a':
                    flag = move.move(pos, 0, -1, np)
                if k == 'w':
                    flag = move.move(pos, 1, 0, np)
                if k == 'd':
                    flag = move.move(pos, 0, 1, np)
                if k == 'q' or flag == 1:
                    running = False
                if k == 'p':
                    f = open(filename, 'w')
                    store = ""
                    for i in range(n):
                        for j in range(n):
                            p = np.get_value(i,j)
                            print(str(int(p)))
                            store += str(int(p))
                    f.write(store)
                    f.flush()
                    f.close()
                draw.draw(n, m, gap / 2, np)
        if(flag == 1):
            print("Win!")
        else:
            print("Loss!")