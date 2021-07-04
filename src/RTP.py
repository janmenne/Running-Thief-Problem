from src.Graph import Graph, shortest_path
import MethodCollection as Mc
import os.path
from os import path


def best_path(filename):
    '''
    berechnet den besten Pfad von einem gegebenen Startpunkt zu einem Endpunkt.
    :param filename: Name der .txt Vorlage
    :return: Liste mit Reihenfolge der besuchten Knoten + Beute (True/False)
    '''
    graph = Graph()
    graph.import_data(filename)

    visited = []
    last_element = list(graph.allNodes)[-1].name
    route = []
    node = graph.allNodes.pop(0)
    getRoute(graph, node, route, last_element, visited)

    route.sort(key=sortV_W, reverse=True)
    getPerfectRoute(route, graph.max_capacity)


def getPerfectRoute(route, max_capacity):
    weight = 0
    value = 0
    for r in route:
        if weight + r[4] <= max_capacity:
            weight += r[4]
            r[5] = True
            value += r[3]
    route.sort(key=sortNode)
    route.insert(0, ["Knoten", "Nachbar", "WDG", "Wert", "Gewicht", "Mitnehmen?"])
    route.append("Mitgenommenes Gewicht: " + str(weight))
    route.append("Maximales Gewicht: " + str(max_capacity))
    route.append("Wert der Beute: " + str(value))
    print(*route, sep='\n')


def sortV_W(element):
    return element[3] / element[4]


def sortNode(element):
    return element[0]


def getRoute(graph, node, route, last_element, visited):
    if node.name == last_element:
        route.append([node.name, node.name, 0.000, node.getValue(), node.getWeight(), False])
        return

    best_wdg = 0
    best_neighbour = None

    for neighbour in node.neighbours:
        if neighbour in visited:
            continue
        if neighbour == last_element:
            distance = node.getDistanceTo(node.neighbours[neighbour])
        else:
            distance = node.getDistanceTo(node.neighbours[neighbour]) + \
                       shortest_path(graph, node.neighbours[neighbour].name, last_element)[0]
        value = node.neighbours[neighbour].getValue()
        weight = node.neighbours[neighbour].getWeight()
        neighbour_wdg = Mc.calculateWDG(value, distance, weight)
        if best_wdg < neighbour_wdg:
            best_wdg = neighbour_wdg
            best_neighbour = node.neighbours[neighbour]

    route.append([node.name, best_neighbour.name, round(best_wdg, 3), node.getValue(), node.getWeight(), False])
    visited.append(node.name)
    getRoute(graph, best_neighbour, route, last_element, visited)


if __name__ == '__main__':
    print("######### OR-Projekt 1: SS21 WWU Muenster #########")
    print("Autoren: Jan Menne, Julian Luetke-Lengerich, Nick Salfeld")
    print("Github: https://github.com/janmenne/Running-Thief-Problem")
    print("######################################################\n\n")

    files = os.listdir('data/')

    print("###Dateien die zur verfügung stehen:\n")
    for f in files:
        print(f)
    print("\n")
    p = input("Welche Datei aus /data/.. soll benutzt werden?\n")
    while not path.exists("data/" + p):
        print("Die angegebene Datei konnte nicht gefunden werden.")
        p = input("Welche Datei aus /data/.. soll benutzt werden?\n")
    print("\n\n")
    best_path("data/" + p)
    print("\n\n")
    input("Press key to end programm...")
