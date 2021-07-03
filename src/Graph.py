import math
from collections import defaultdict, deque
from FileManager import FileManager
import MethodCollection as mc
from Node import Node as node


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)
        self.distances = {}
        self.allNodes = set()

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)
        self.distances[(from_node, to_node)] = distance

    def import_data(self, filename):
        fm = FileManager(filename)

        self.allNodes = fm.items

        for node in self.allNodes:
            self.add_node(node.name)
            for neighbour in node.getNeighbours():
                self.add_edge(node.name, neighbour[1].name, node.getDistanceTo(neighbour[1]))

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
