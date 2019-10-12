def Gauss_Partial_pivot_selection(n, a, y):
    """
    n = 解の数(x_n)
    a = 係数のlist
    y = 方程式の右辺
    """
    for k in range(n-1):
        bf = -float("INF")
        for i in range(k,n):
            if bf < abs(a[i][k]):
                mi = i
                bf = a[i][k]
        if mi != k:
            for i in range(k,n):
                a[k][i],a[mi][i] = a[mi][i],a[k][i]
            y[k],y[mi] = y[mi],y[k]
        for i in range(k+1,n):
            alpa = a[i][k]/a[k][k]
            for j in range(k+1,n):
                a[i][j] = a[i][j] - alpa*a[k][j]
            y[i] = y[i] - alpa*y[k]
    x = [0 for i in range(n)]
    x[n-1] = y[n-1]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        A = 0.0
        for k in range(i,n):
            A += float(a[i][k])*float(x[k])
        x[i] = (y[i]-A)/a[i][i]
    return x
