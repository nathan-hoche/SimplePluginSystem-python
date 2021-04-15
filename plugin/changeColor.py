class changeColor:
    def __init__(self) -> None:
        self.wall = ""
        pass

    def edit(self, map = None):
        if (map == None):
            return None
        tmp = map.split('\n')
        y = 0 
        while (y != len(tmp)):
            x = 0
            while (x != len(tmp[y])):
                if (tmp[y][x] == '+'):
                    tmp[y] = tmp[y][:x] + '\033[91mo\033[00m' + tmp[y][x+1:]
                elif (tmp[y][x] == '|' or tmp[y][x] == '-'):
                    tmp[y] = tmp[y][:x] + '\033[92mo\033[00m' + tmp[y][x+1:]
                x += 1
            y += 1
        res = ""
        for line in tmp:
            res += "\n" + line
        return res

    def desc(self):
        pass

    def update(self, map=None):
        return map