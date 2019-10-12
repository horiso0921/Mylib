class Value_UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.differ_weight = [0] * n
        self.rank = [0] * n

    def root(self,x):
        if x == self.par[x]:
            return x
        r = self.root(self.par[x])
        self.differ_weight[x] += self.differ_weight[self.par[x]]
        self.par[x] = r
        return r

    def weight(self, x):
        self.root(x)
        return self.differ_weight[x]

    def unit(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: x, y, w = y, x, -w
        if self.rank[x] == self.rank[y]: self.rank[x] += 1
        self.par[y] = x
        self.differ_weight[y] = w
        return True

    def differ(self, x, y):
        return self.weight(y) - self.weight(x)
