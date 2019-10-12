from heapq import heappush, heappop

def Dijkstra(num, start, vedge):
    """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
    """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
    """ dist[i] は start から i までの最短距離 """

    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in vedge[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist

