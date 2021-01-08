from src.DiGraph import DiGraph

import matplotlib.pyplot as plt


def draw_graph(g: DiGraph):
    tupleee = []
    x = []
    y = []
    n = []

    for i in g.nodes.keys():
        n.append(i)

    for i in range(len(g.nodes)):
        tupleee.append(list(g.nodes[i]))

    print(tupleee)
    for i in range(len(tupleee)):
        x.append(tupleee[i][0])
        y.append(tupleee[i][1])

    ax = plt.axes()
    ax.scatter(x, y)
    plt.plot(x, y, "o")

    for i in g.nodes:
        for j in g.neighbors.get(i):
            src_x = g.nodes.get(i)[0]
            dst_x = g.nodes.get(j)[0]
            src_y = g.nodes.get(i)[1]
            dst_y = g.nodes.get(j)[1]
            ax.arrow(src_x, src_y, dst_x-src_x, dst_y-src_y, head_width=0.2, head_length=0.1, fc='k', ec='k')


    for i, txt in enumerate(n):
        ax.annotate(n[i], (x[i]-0.5, y[i]+0.5))  # , arrowprops=dict(arrowstyle="->"))

    plt.xlabel(" x --> ")
    plt.ylabel(" y --> ")
    plt.title("graph name")
    ax.set_facecolor('xkcd:mint green')

    plt.show()

if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(0, (1, 16, 0))
    graph.add_node(1, (6, 6, 0))
    graph.add_node(2, (9, 7, 0))
    graph.add_node(3, (9, 9, 0))
    graph.add_node(4, (2, 5, 0))
    graph.add_node(5, (5, 12, 0))
    graph.add_edge(0, 1, 1.0)
    graph.add_edge(1, 2, 1.0)
    graph.add_edge(2, 0, 1.0)
    graph.add_edge(0, 3, 1.0)
    graph.add_edge(0, 4, 1.0)
    graph.add_edge(0, 5, 1.0)
    graph.add_edge(5, 0, 1.0)


