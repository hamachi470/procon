class SegTree:
    def __init__(self, n, segfunc, unit):
        # n:要素数, segfunc:関数, unit:単位元
        self.depth = (n-1).bit_length()
        self.num = 1 << self.depth
        self.segfunc = segfunc
        self.unit = unit
        self.tree = [self.unit] * (self.num << 1)

    def build(self, arr):
        # 既存の配列arrからセグ木を生成(arrの要素数はnであること)
        for i in range(len(arr)):
            self.tree[i+self.num] = arr[i]
        for i in range(self.num-1, 0, -1):
            l_ch = i << 1 # left child
            self.tree[i] = self.segfunc(self.tree[l_ch], self.tree[l_ch+1])

    def update(self, i, x):
        # i番目の値をxに更新
        i += self.num
        self.tree[i] = x
        while i > 1:
            i >>= 1
            l_ch = i << 1
            self.tree[i] = self.segfunc(self.tree[l_ch], self.tree[l_ch+1])

    def get(self, i):
        # i番目の値を取得
        return self.tree[i+self.num]

    def fold(self, l, r):
        # 半開区間[l, r)の値を取得
        left = self.unit; right = self.unit
        l += self.num; r += self.num
        while l < r:
            if l & 1:
                left = self.segfunc(left, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                right = self.segfunc(self.tree[r], right)
            l >>= 1; r >>= 1
        return self.segfunc(left, right)
