from src.Graph import Graph, shortest_path
from FileManager import FileManager

if __name__ == '__main__':
    graph = Graph()
    graph.import_data("rtp_0_5.txt")
    print(graph.shortest_path(graph, 0, 5))
