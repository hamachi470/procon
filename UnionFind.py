class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n)]
        self.size = [1]*n
        self.edge = [0]*n
        self.member = [[i] for i in range(n)]
        self.group = n

    def find(self, x):
        q = []
        while x != self.root[x]:
            q.append(x)
            x = self.root[x]
        for y in q:
            self.root[y] = x
        return x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            self.edge[x] += 1
            return
        if x > y:
            x, y = y, x
        self.root[y] = x
        self.size[x] += self.size[y]
        self.edge[x] += self.edge[y]+1
        self.member[x] += self.member[y]
        self.group -= 1
        return
