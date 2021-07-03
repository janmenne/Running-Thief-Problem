from src.Graph import Graph, shortest_path
from FileManager import FileManager
from Node import Node
import MethodCollection as MC


def best_path(filename):
    '''
    berechnet den besten Pfad von einem gegebenen Startpunkt zu einem Endpunkt.
    :param filename: Name der .txt Vorlage
    :return: Liste mit Reihenfolge der besuchten Knoten + Beute (True/False)
    '''
    graph = Graph()
    graph.import_data(filename)

    last_element = list(graph.allNodes)[-1].name
    route = []
    getRoute(graph, route, last_element)

    print(route)


def getRoute(graph, route, last_element):
    if not graph.allNodes:
        return

    best_wdg = 0
    best_neighbour = None

    node = graph.allNodes.pop(0)

    if node == last_element:
        return

    for neighbour in node.neighbours:
        if neighbour == last_element:
            break
        print(neighbour)
        value = node.neighbours[neighbour].getValue()
        distance = node.getDistanceTo(node.neighbours[neighbour]) + \
                   shortest_path(graph, node.neighbours[neighbour].name, last_element)[0]
        weight = node.neighbours[neighbour].getWeight()
        print(value, distance, weight)
        neighbour_wdg = MC.calculateWDG(value, distance, weight)
        if best_wdg < neighbour_wdg:
            best_wdg = neighbour_wdg
            best_neighbour = node.neighbours[neighbour]

    route.append([best_neighbour.name, best_wdg, best_neighbour.getValue() / best_neighbour.getWeight()])

    getRoute(graph, route, last_element)


if __name__ == '__main__':
    best_path("data/rtp_0_5.txt")
