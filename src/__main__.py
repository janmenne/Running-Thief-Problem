'''

Loesungsansatz fuer das Running Thief Problem.

1. Dijkstra Algorithmus um die besten Wege von jedem Knoten zum Endknoten zu berechnen.
2. Optimale Route aufstellen ueber WDG Wert
    - WDG berechnet sich aus Wert / Distanz (Nachbarknoten+Dijkstra) / Gewicht
3. Optimale Route nach Wert/Gewicht sortieren und Rucksack vollpacken. :)

'''
from queue import PriorityQueue
import math
import sys

# list to store final solutions (store triple:(O,U,solution), sorted ascending)
final_solutions = []

### The following values are only first test values, in case readInstance
### is not used

# maximal capacity of knapsack
max_capacity = 18

# list of tuples that denote (item weight, item value) each
items = [(1, 3), (2, 1), (2, 4), (3, 3), (2, 2), (3, 6), (1, 1), (3, 4), (2, 3), (4, 3)]

# compute ratio of value/weight for given instance, store together with index
ratioed_items = []
for i in range(len(items)):
    ratioed_items.append((items[i][1] / items[i][0], items[i][0], items[i][1], i))

# initial solution as list of -1 values
initialSol = len(items) * [-1]


def readInstance(filename):
    """import an instance from file and overwrite the default global data.
    This method only reads the necessary nodes information on weights and
    utility of objects as well as the maximum capacity of the knapsack (k)."""
    global items
    global max_capacity
    global ratioed_items
    global initialSol

    value_mode = False

    file = open(filename)

    for line in file:
        fields = line.strip().split()
        if not value_mode and not fields[0] == "#EOF":
            if fields[0] == "k":
                max_capacity = int(fields[2])
            elif fields[0] == "#NODES":
                value_mode = True
                items = []

        elif not fields[0] == "#EOF":
            items.append(eval(fields[2]))

    # recompute ratios based on read values
    ratioed_items = []
    for i in range(len(items)):
        ratioed_items.append((items[i][1] / items[i][0], items[i][0], items[i][1], i))

    initialSol = len(items) * [-1]

    print(filename)

    return


######### MAIN #############
if __name__ == '__main__':
    print("Read Instance: ")
    readInstance("rtp_0_5.txt")
    print
