class FenwickTree:
    def __init__(self, N, mod=None):
        self.N = N
        self.tree = [0]*(N+1)
        self.mod = mod
        self.depth = N.bit_length()

    def add(self, i, x=1):
        while i <= self.N:
            self.tree[i] += x
            if self.mod:
                self.tree[i] %= self.mod
            i += i&(-i)

    def fold(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            if self.mod:
                s %= self.mod
            i -= i&(-i)
        return s

    def get_range(self, l, r):
        #閉区間[l, r]の合計を取得
        res = self.fold(r) - self.fold(l-1)
        if self.mod:
            res %= self.mod
        return res

    def bisect(self, x):
        #fold(p) >= x となる最小のpと、その直前までの累積和
        pos, s = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos+(1<<i)
            if k <= self.N and s + self.tree[k] < x:
                s += self.tree[k]
                pos += 1<<i
        return pos+1, s

def inversion(arr):
    #配列arrの転倒数を求める(座標圧縮)
    S = sorted(list(set(arr)))
    Z = {s: i for i, s in enumerate(S, 1)}
    FT = FenwickTree(len(Z))
    inv = 0
    for i, a in enumerate(arr):
        z = Z[a]
        inv += i-FT.fold(z)
        FT.add(z, 1)
    return inv
