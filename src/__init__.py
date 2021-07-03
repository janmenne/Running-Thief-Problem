from src.Graph import Graph, shortest_path
from FileManager import FileManager
from Node import Node
from Loot import Loot

if __name__ == '__main__':
    graph = Graph()
    graph.import_data("rtp_0_5.txt")
    print(shortest_path(graph, 1, 5))
