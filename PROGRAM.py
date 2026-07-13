import heapq

# ---------- Dijkstra Algorithm ----------
def dijkstra(graph, source):
    n = len(graph)

    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


# ---------- Reconstruct Path ----------
def reconstruct_path(prev, source, target):
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []
