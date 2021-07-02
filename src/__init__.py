from src.Graph import Graph, shortest_path

if __name__ == '__main__':
    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 30)
    graph.add_edge('B', 'E', 50)
    graph.add_edge('D', 'E', 30)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print(shortest_path(graph, 'B', 'E'))  # output: (25, ['A', 'B', 'D'])
