from queue import PriorityQueue
import math
import sys


class FileManager:

    def read(self):
        """import an instance from file and overwrite the default global data.
        This method only reads the necessary nodes information on weights and
        utility of objects as well as the maximum capacity of the knapsack (k)."""

        value_mode = False

        file = open(self.name)

        for line in file:
            fields = line.strip().split()
            if not value_mode and not fields[0] == "#EOF":
                if fields[0] == "k":
                    self.max_capacity = int(fields[2])
                elif fields[0] == "#NODES":
                    value_mode = True
                    self.items = []

            elif not fields[0] == "#EOF":
                self.items.append(eval(fields[2]))

        # recompute ratios based on read values
        self.ratioed_items = []
        for i in range(len(self.items)):
            self.ratioed_items.append((self.items[i][1] / self.items[i][0], self.items[i][0], self.items[i][1], i))

        self.initialSol = len(self.items) * [-1]

        return

    def __init__(self, filename):
        self.name = filename

        # maximal capacity of knapsack
        self.max_capacity = 18

        # list of tuples that denote (item weight, item value) each
        self.items = [(1, 3), (2, 1), (2, 4), (3, 3), (2, 2), (3, 6), (1, 1), (3, 4), (2, 3), (4, 3)]

        # compute ratio of value/weight for given instance, store together with index
        self.ratioed_items = []
        for i in range(len(self.items)):
            self.ratioed_items.append((self.items[i][1] / self.items[i][0], self.items[i][0], self.items[i][1], i))

        # initial solution as list of -1 values
        self.initialSol = len(self.items) * [-1]

        self.read()

        print(filename + " wurde eingelesen mit den Attributen:")
        print(self.items)
        print("\nMaximale Kapazitaet:")
        print(self.max_capacity)
        print("\nWert durch Gewicht fuer jeden Knoten:")
        print(self.ratioed_items)
