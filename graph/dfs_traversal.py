

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            # Note we used pop(0) which makes it look like queeu {remove first} known as dqueue
            deVertex = queue.pop(0)
            print(deVertex)

            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def defs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            # Note we used pop() which makes it look like stack {remove last}
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e"],
    "e": ["c", "d", "f", "b", ],
    "f": ["d", "e"]

}

graph = Graph(customDict)


graph.bfs("a")
