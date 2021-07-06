from Node import Node as node


class FileManager:
    '''
    Einlesen der gegebene Datein aus src/data
    '''

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

            elif not fields[0] == "#EOF":  # Index + 1 = Knoten
                valueweight = eval(fields[2])
                n = node(eval(fields[0]), valueweight[1], valueweight[0], eval(fields[1]))
                self.items.append(n)
                try:
                    self.itemNeighbour.append(
                        eval(fields[3]))  # [(2, 4..), (8, 3..) ..] Wert 1 = Nachbar1... Wert 5 = Nachbar 5
                except IndexError:
                    self.itemNeighbour.append([])
        #         self.itemCoordinate.append(eval(fields[1]))  # [(1,1), (0,4) ..] Wert1 = x, Wert2 = y
        #
        #         self.items.append(eval(fields[2]))  # [(2,3), (4,6) ..] Wert1 = Gewicht, Wert2 = Wert

        #
        # # recompute ratios based on read values
        # self.ratioed_items = []
        # for i in range(len(self.items)):
        #     self.ratioed_items.append((self.items[i][1] / self.items[i][0], self.items[i][0], self.items[i][1], i))
        #
        # self.initialSol = len(self.items) * [-1]

        for i in range(len(self.itemNeighbour)):

            if not self.itemNeighbour[i]:
                for element in self.items:
                    if element != self.items[i]:
                        self.items[i].setNeighbour(element)

            for j in self.itemNeighbour[i]:
                self.items[i].setNeighbour(self.items[j - 1])

        return

    def __init__(self, filename):
        self.name = filename

        # maximal capacity of knapsack
        self.max_capacity = 18

        # list of Nodes
        self.items = []

        # compute ratio of value/weight for given instance, store together with index
        self.ratioed_items = []
        for i in range(len(self.items)):
            self.ratioed_items.append((self.items[i][1] / self.items[i][0], self.items[i][0], self.items[i][1], i))

        # initial solution as list of -1 values
        self.initialSol = len(self.items) * [-1]

        self.itemNeighbour = []

        self.itemCoordinate = []

        self.read()
