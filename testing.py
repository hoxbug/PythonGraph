from graph import Graph

def test_graph():
    graph_string = """\
    U 6
    1 2
    1 3
    2 4
    2 3
    3 5
    4 5
    """

    my_graph = Graph(graph_string)
    my_graph.print_graph()

if __name__ == "__main__":
    test_graph()
