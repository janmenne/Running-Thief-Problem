from collections import defaultdict, deque

from FileManager import FileManager


class Graph(object):
    '''
    Graph welcher unser Problem darstellt, abspeichert und verarbeitet
    '''

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)
        self.distances = {}
        self.allNodes = set()

    def add_node(self, value):
        '''
        Fuegt einen neuen Knotenpunkt zum Graphen hinzu.
        :param value: Node-Objekt
        :return: None
        '''
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        '''
        Fuegt eine neue Kante zwischen zwei Knotenpunkten zum Graphen hinzu.
        :param from_node: Knotenpunkt-1
        :param to_node: Knotenpunkt-2
        :param distance: Distanz zwischen den beiden Knotenpunkten.
        :return: None
        '''
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)
        self.distances[(from_node, to_node)] = distance

    def import_data(self, filename):
        '''
        Import einen Datensatz und fuegt anhand dessen Knotenpunkte und Kanten zum Graphen hinzu.
        :param filename: Dateipfad zum Datensatz
        :return: None
        '''
        fm = FileManager(filename)

        self.allNodes = fm.items
        self.max_capacity = fm.max_capacity

        for node in self.allNodes:
            self.add_node(node.name)
            for neighbour in node.getNeighbours():
                self.add_edge(node.name, neighbour[1].name, node.getDistanceTo(neighbour[1]))


def dijkstra(graph, initial):
    '''
    Interne Implementation des Dijkstra-Algorithmus zur weiteren Verwendung in 'shortest_path'
    :param graph: gefuellte Instanz eines Graph-Objekts
    :param initial: Initialer Wert standartmaeßig 0.
    :return: besuchte Knoten, Pfad
    '''
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
    '''
    Berechnet den kuerzesten Pfad von einem Start- zu einem Endknoten.
    :param graph: gefuellte Instanz eines Graph-Objekts
    :param origin: Startknoten
    :param destination: Zielknoten
    :return: Liste aus besuchten Knoten bzw. vollstaendigem, kuerzesten Pfad.
    '''
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
