class clipsPoint:
    def __init__(self) -> None:
        self.point = [[29, 18], [29, 36], [29, 42], [29, 57]]
        pass

    def edit(self, map = None):
        if (map == None):
            return None
        tmp = map.split('\n')
        for pt in self.point:
            tmp[pt[0]] = tmp[pt[0]][:pt[1]] + 'x' + tmp[pt[0]][pt[1]+1:]
        res = ""
        for line in tmp:
            res += "\n" + line
        return res

    def desc(self):
        print("x -> broken wall")

    def update(self, map=None):
        return map