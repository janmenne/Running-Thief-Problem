import math


def calculateDistance(v1, v2):
    if len(v1) == 2 and len(v2) == 2:
        x = math.pow(v1[0] - v2[0], 2)
        y = math.pow(v1[1] - v2[1], 2)

        return math.sqrt(x + y)
    else:
        raise ValueError("Vektoren muessen jeweils aus zwei Zahlen bestehen.")


def calculateWDG(wert, distance, gewicht):
    return wert / distance / gewicht
