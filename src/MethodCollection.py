import math


def calculate_distance(v1, v2):
    '''
    Berechnet die Distanz aus den Koordinaten zweier Knotenpunkte
    :param v1: Liste der Koordinaten von Knotenpunkt-1
    :param v2: Liste der Koordinaten von Knotenpunkt-2
    :return: Distanz zwischen uebergebenen Koordinaten
    '''
    if len(v1) == 2 and len(v2) == 2:
        x = math.pow(v1[0] - v2[0], 2)
        y = math.pow(v1[1] - v2[1], 2)

        return math.sqrt(x + y)
    else:
        raise ValueError("Vektoren muessen jeweils aus zwei Zahlen bestehen.")


def calculateWDG(wert, distance, gewicht):
    '''
    Berechnet den WDG-Wert als gewichtetes Entscheidungskriterium.
    :param wert: Wert der Beute
    :param distance: kuerzeste Distanz zum Endknoten (Distanz zum naechsten Knoten + Dijkstra)
    :param gewicht: Gewicht der Beute
    :return: gewichteter Wert
    '''
    if (distance > 0 and gewicht > 0):
        return wert / distance / gewicht
    else:
        raise ZeroDivisionError("Die Werte Distanz und Gewicht muessen > 0 sein!")
