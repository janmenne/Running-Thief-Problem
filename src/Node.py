import MethodCollection as mc


class Node:
    '''
    Node Klasse.
    Bildet die Funktionalitaet von Knotenpunkten im Rahmen des Running Thief Problems ab.
    '''

    def __init__(self, name, value, weight, coordinates):
        '''
        Erzeugt eine neue Knotenpunktinstanz unter Angabe von Name, Wert, Gewicht und Koordinaten.
        :param name: Name des Knotenpunkts
        :param value: Wert der Beute
        :param weight: Gewicht der Beute
        :param coordinates: Koorinaten des Knotenpunktes.
        '''
        self.name = name
        self.value = value
        self.weight = weight
        self.neighbours = {}
        self.distances = {}
        self.coordinates = coordinates

    def setValue(self, value):
        '''
        Setzt den Wert der an dem Knotenpunkt befindlichen Beute.
        :param value: Neuer Wert der Beute
        :return:
        '''
        self.value = value

    def getValue(self):
        '''
        Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck.
        :return: Aktueller Wert der Beute
        '''
        return self.value

    def setWeight(self, weight):
        '''
        Setzte das Gewicht der an dem Knotenpunkt befinflichen Beute.
        :param weight: neues Gewicht.
        :return:
        '''
        self.weight = weight

    def getWeight(self):
        '''
        Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck.
        :return: Aktuelles Gewicht der Beute
        '''
        return self.weight

    def setNeighbour(self, node):
        '''
        Fuegt zum Knotenpunkt einen Nachbarknoten hinzu und berechnet die Distanz zwischen beiden Punkten.
        :param node: Node-Objekt, dass als Nachbar gesetzt werden soll.
        :return:
        '''
        self.neighbours[node.name] = node
        self.distances[node.name] = mc.calculate_distance(self.coordinates, (node.getCoordinates()))

    def getDistanceTo(self, node):
        '''
        Gibt die Distanz zu einem beliebigen Nachbarknoten zurueck.
        :param node: Node-Objekt, zu dem die Distanz bestimmt werden soll.
        :return: Distanz zu uebergebenem Node-Objekt.
        '''
        if (node.name in self.distances.keys()):
            return self.distances.get(node.name)
        else:
            raise KeyError("Der uebergebene Knotenpunkt ist kein Nachbarknoten!")

    def set_distance_to(self, node, distance):
        self.distances[node.name] = distance

    def getNeighbours(self):
        '''
        Gibt die bestehenden Nachbarknoten zurueck.
        :return: dictionary der existierenden Nachbarknoten
        '''
        return self.neighbours.items()

    def getNeighbour(self, name):
        '''
        Gibt einen Nachbarknoten unter Angabe des Namens zurueck.
        :param name: Name des Node-Objekts
        :return: Node mit entsprechendem Namen
        '''
        return self.neighbours.get(name)

    def getCoordinates(self):
        '''
        Gibt die Koordinaten des Knotenpunktes zurueck.
        :return: List mit Koordinaten.
        '''
        return self.coordinates
