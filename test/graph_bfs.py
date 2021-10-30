class Graph(object):

    def __init__(self):

        self.g = {}

    def add_edge(self, u, v):

        if u in self.g:
            self.g[u].append(v)
        else:
            self.g[u] = [v]

    def dfs_recur(self, v, visited, path):

        visited.add(v)
        path.append(v)

        adj_nodes = self.g[v]

        for node in adj_nodes:
            if node in visited:
                continue
            else:
                self.dfs_recur(node, visited, path)
        return

    def dfs(self, u):

        path = []
        visited = set()
        for u in self.g.keys():
            if u not in visited:
                self.dfs_recur(u, visited, path)
        return path

    def bfs(self, u, visited, path):

        node_q = []
        node_q.append(u)
        visited.add(u)

        while len(node_q) > 0:
            print(node_q)
            n = node_q.pop(0)
            path.append(n)

            for node in self.g[n]:
                if node not in visited:
                    node_q.append(node)
                    visited.add(node)




g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.dfs(3))

path = []

g.bfs(0, set(), path)

print(path)

