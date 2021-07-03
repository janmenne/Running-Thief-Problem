from src.Graph import Graph, shortest_path
from FileManager import FileManager
from Node import Node
from Loot import Loot


def best_path(filename):
    graph = Graph()
    graph.import_data(filename)
    nodes = graph.getNodes()

    print(nodes)


if __name__ == '__main__':
    best_path("data/rtp_0_5.txt")
