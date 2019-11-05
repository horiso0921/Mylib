class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self.bit = [0 for _ in range(size)]
        self.size = size

    def add(self, i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def search(self, x):
    # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        i = 0
        s = 0
        step = 1 << self.size.bit_length() - 1
        while step:
            if i + step <= self.size and s + self.bit[i + step] < x:
                i += step
                s += self.bit[i]
            step >>= 1
        return i + 1

    def __len__(self):
        return self.size