from bit import BinaryIndexedTree
def count_inversions(array, Max=None):
    """
    リストから転倒数 (array[i] > array[j] (i < j) となる (i, j) の組み合わせ数) を返す
    バブルソートするときに反転する必要がある数。
    :param list of int array:
            すべての要素が 0 以上の int である配列。
    :param int max: array の最大値。指定はわかる場合
    :rtype int:
    """
    if not Max:
        Max = max(array)
    bit = BinaryIndexedTree(Max + 1)
    res = 0
    for i in range(len(array)):
        res += i - bit.sum(array[i])
        bit.add(array[i], 1)
    return res