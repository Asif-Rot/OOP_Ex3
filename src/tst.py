from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

if __name__ == '__main__' :
    graph1 = GraphInterface()
    graphAlgo = GraphAlgo()

    # file = '../data/A0'
    # print(graphAlgo.graph)
    # GraphAlgo.load_from_json(graphAlgo, file)
    # print(graphAlgo.graph)
    # print(graphAlgo.graph.e_size())
    # print(graphAlgo.graph.v_size())
    #
    # print(graphAlgo.save_to_json("C:/Users/97250/Desktop/savedgraph.json"))
    # graphhh = graphAlgo.load_from_json("C:/Users/97250/Desktop/savedgraph.json")
    # print(graphAlgo.load_from_json("C:/Users/97250/Desktop/savedgraph.json"))
    # print(graphAlgo.graph.all_out_edges_of_node(0))
    # print(graphAlgo.shortest_path(0, 10))

    graph = DiGraph()
    for i in range(5) :
        graph.add_node(i)
    graph.add_edge(0, 1, 1.0)
    graph.add_edge(0, 2, 1.1)
    graph.add_edge(2, 1, 1.0)
    graph.add_edge(1, 2, 1.0)
    # graph.add_edge(2, 0, 1.0)

    GraphAlgo.get_graph(graphAlgo)
    print(graphAlgo.connected_components())
    print(graphAlgo.connected_component(4))
    graphAlgo.plot_graph()
