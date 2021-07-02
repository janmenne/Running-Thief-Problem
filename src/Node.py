import MethodCollection as mc


class Node:

    def __init__(self, name, value, weight, coordinates):
        self.name = name
        self.value = value
        self.weight = weight
        self.neighbours = {}
        self.distances = {}
        self.coordinates = coordinates

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setNeighbour(self, node):
        self.neighbours[node.name] = node
        self.distances[node.name] = mc.calculateDistance(self.coordinates, (node.getCoordinates()))

    def getDistanceTo(self, node):
        return self.distances.get(node.name)

    def getNeighbours(self):
        return self.neighbours.items()

    def getNeighbour(self, name):
        return self.neighbours.get(name)

    def getCoordinates(self):
        return self.coordinates
