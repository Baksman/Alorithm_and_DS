
from collections import defaultdict

print(defaultdict(list))


class Graph:
    def __init__(self,):
        self.node = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.node.add(value)

    def addEdge(self, fromNode, toNode, distance):
        # edge will dict of with key fromNode and value as List toNode
        # distance wil be a map with key as tuple and vale as int {(from,to):2}
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def djikstra(graph: Graph, initialNode):
    visited = {initialNode: 0}
    path = defaultdict(list)

    nodes = set(graph.node)

    while nodes:
        minimum_node = None
        for node in nodes:
            if node in visited:
                if minimum_node == None:
                    minimum_node = node
                elif visited[node] < visited[minimum_node]:
                    minimum_node = node
        if minimum_node is None:
            break

        nodes.remove(minimum_node)
        currentWeight = visited[minimum_node]

        for edge in graph.edges[minimum_node]:
            weight = currentWeight + graph.distances[(minimum_node, edge)]
            if edge not in visited and weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minimum_node)

    return visited, path
