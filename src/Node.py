import MethodCollection as mc

# Node Klasse.
# Bildet die Funktionalitaet von Knotenpunkten im Rahmen des Running Thief Problems ab.
class Node:

    # Erzeugt eine neue Knotenpunktinstanz unter Angabe von Name, Wert, Gewicht und Koordinaten.
    def __init__(self, name, value, weight, coordinates):
        self.name = name
        self.value = value
        self.weight = weight
        self.neighbours = {}
        self.distances = {}
        self.coordinates = coordinates

    # Setzt den Wert der an dem Knotenpunkt befindlichen Beute.
    def setValue(self, value):
        self.value = value

    # Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck.
    def getValue(self):
        return self.value

    # Setzte das Gewicht der an dem Knotenpunkt befinflichen Beute.
    def setWeight(self, weight):
        self.weight = weight

    # Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck.
    def getWeight(self):
        return self.weight

    # Fuegt zum Knotenpunkt einen Nachbarknoten hinzu und berechnet die Distanz zwischen beiden Punkten.
    def setNeighbour(self, node):
        self.neighbours[node.name] = node
        self.distances[node.name] = mc.calculateDistance(self.coordinates, (node.getCoordinates()))

    # Gibt die Distanz zu einem beleibigen Nachbarknoten zurueck.
    def getDistanceTo(self, node):
        return self.distances.get(node.name)

    # Gibt ein dictinory der Nachbarknoten zurueck.
    def getNeighbours(self):
        return self.neighbours.items()

    # Gibt einen Nachbarknoten unter Angabe des Namens zurueck.
    def getNeighbour(self, name):
        return self.neighbours.get(name)

    # Gibt die Koordinaten des Knotenpunktes zurueck.
    def getCoordinates(self):
        return self.coordinates
