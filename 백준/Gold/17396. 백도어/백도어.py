import sys

input = sys.stdin.readline

from heapq import heappop, heappush

INF = float('inf')


def djk(start):
    Q = []
    heappush(Q, (0, start))
    road[start] = 0

    while Q:
        node, now = heappop(Q)
        if node > road[now]:
            continue
        # 그래프에는 길이, 다음위치 순으로 저장되어 있음
        for i in g[now]:
            cost = i[0] + node
            if road[i[1]] > cost and w[i[1]] == 0:
                road[i[1]] = cost
                heappush(Q, (cost, i[1]))


n, m = map(int, input().split())

g = [[] for _ in range(n)]
w = list(map(int, input().split()))
road = [INF] * (n)
w[-1] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    # 거리, 다음위치
    g[a].append((c, b))
    g[b].append((c, a))
djk(0)
if road[n - 1] == INF:
    print(-1)
else:
    print(road[n - 1])
