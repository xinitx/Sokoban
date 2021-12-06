from . import point2DMatrix
def move(pos, dx, dy, np):
    posx = (int)(pos / np.n())
    posy = (int)(pos % np.n())
    n = (int)(np.n())
    m = (int)(np.m())
    #print(posx, posy, dx, dy)
    #print(np.get_values())
    if  posx + dx < 0 or posx + dx > m - 1 or posy + dy < 0 or posy + dy > n - 1:
        return 0
    if  np.get_value(posx + dx, posy + dy) == 0:        #如果移动目标点是空地
                np.set_value(posx, posy, 0)
                np.set_value(posx + dx, posy + dy, 2)
                                                        #如果移动目标点是箱子，箱子后边是空地
    elif np.get_value(posx + dx, posy + dy) == 3: 
        if posx + dx * 2 < 0 or posx + dx * 2 > m - 1 or posy + dy * 2 < 0 or posy + dy * 2 > n - 1:
            return 0
        if np.get_value(posx + dx * 2, posy + dy * 2) == 0:
            np.set_value(posx, posy, 0)
            np.set_value(posx + dx, posy + dy, 2)
            np.set_value(posx + dx * 2, posy + dy * 2, 3)
                                                             #如果移动目标点是箱子，箱子后边是终点
        elif np.get_value(posx + dx * 2, posy + dy * 2) == 4:
            return 1
    return 0