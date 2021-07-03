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

    route.sort(key=take_second, reverse=True)
    getPerfectRoute(route, graph.max_capacity)


def getPerfectRoute(route, max_capacity):
    weight = 0
    for r in route:
        if weight + r[2] <= max_capacity:
            weight += r[2]
            r[3] = True
    route.insert(0, ["Knoten", "WDG", "Wert/Gewicht", "Mitnehmen?"])
    print(*route, sep='\n')


def take_second(element):
    return element[2]


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
        value = node.neighbours[neighbour].getValue()
        distance = node.getDistanceTo(node.neighbours[neighbour]) + \
                   shortest_path(graph, node.neighbours[neighbour].name, last_element)[0]
        weight = node.neighbours[neighbour].getWeight()
        neighbour_wdg = MC.calculateWDG(value, distance, weight)
        if best_wdg < neighbour_wdg:
            best_wdg = neighbour_wdg
            best_neighbour = node.neighbours[neighbour]

    route.append([best_neighbour.name, best_wdg, best_neighbour.getValue() / best_neighbour.getWeight(), False])

    # Nachbarn übergeben!
    getRoute(graph, route, last_element)


if __name__ == '__main__':
    best_path("data/rtp_1_10.txt")
