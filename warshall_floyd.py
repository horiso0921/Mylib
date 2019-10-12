def Warshall_Floyd(n, vedge, d):
    """ vedge は dict. 辺がない場合は lambda:inf 等でinfをあらかじめ入れること """
    """ d[i][j] は i → j の最短距離 """

    # 初期化
    for i in range(n):
        for j in range(n):
            d[i][j] = vedge[(i, j)]
    
    # 本計算
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
