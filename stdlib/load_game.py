from . import stddraw, point2DMatrix, draw, move

class start_game:
    def __init__(self, n, m, filename, root, type_op):
        root.destroy()
        if type_op == "load":
            stddraw.setCanvasSize(800,800)
            stddraw.setXscale(-50,50)
            stddraw.setYscale(-50,50)
        np = point2DMatrix.point2DMatrix(0, 0, 100, 100, n, m)

        f = open(filename, 'r')
        start = f.read()
        posx = 0
        posy = 0
        
        for i in range(n):
            for j in range(n):
                np.set_value(i, j, int(start[i * n + j]))
                if(int(start[i * n + j]) == 2):
                    posx = i
                    posy = j
        draw.draw(n, np)
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
                draw.draw(n, np)
        if(flag == 1):
            print("Win!")
        else:
            print("Loss!")