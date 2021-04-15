class player:
    def __init__(self) -> None:
        self.linex = 0
        self.liney = 29
        pass

    def edit(self, map=None):
        if (map == None):
            return None
        tmp = map.split('\n')
        l0 = list(tmp[self.liney])
        l0[self.linex] = 'P'
        lr = "".join(l0)
        y = 1
        res = tmp[0]
        while (y != len(tmp)):
            if (y == self.liney):
                res += '\n' + lr
            else:
                res += '\n' + tmp[y]
            y += 1
        return res

    def desc(self):
        print("P -> player")
        pass

    def update(self, map=None):
        if (map == None):
            return None
        map = map.replace('P', ' ')
        if (self.linex < 50):
            self.linex += 1
        return self.edit(map)