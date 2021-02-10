# single source  shortest path problem

# BFS DJIKSTRA BELLMANFORD etc


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        # queue is created for maintaining path
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            

            for adjacent in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

