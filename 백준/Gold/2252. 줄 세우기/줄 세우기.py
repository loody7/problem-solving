from collections import deque

def solve():
    result = []

    q = deque()

    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    for x in result:
        print(x, end=' ')
    return

if __name__ == "__main__":

    n, m = map(int, input().split())  
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    solve()