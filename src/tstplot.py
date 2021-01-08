from src.DiGraph import DiGraph
# https://colab.research.google.com/github/makeabilitylab/signals/blob/master/Tutorials/IntroToMatplotlib.ipynb#scrollTo=DZBaqyORpHIS

import matplotlib.pyplot as plt

if __name__ == '__main__':

    graph = DiGraph()
    graph.add_node(0, (4, 8, 0))
    graph.add_node(1, (2, 9, 0))
    graph.add_node(2, (12.3, 3, 0))
    graph.add_edge(0, 1, 1.0)
    graph.add_edge(0, 2, 1.1)
    graph.add_edge(2, 1, 1.0)
    graph.add_edge(1, 2, 1.0)
    graph.add_edge(2, 0, 1.0)



    tupleee = []
    x = []
    y = []
    for i in range(len(graph.nodes)):
        tupleee.append(list(graph.nodes[i]))

    print(tupleee)
    for i in range(len(tupleee)):
        x.append(tupleee[i][0])
        y.append(tupleee[i][1])

    print(x)
    print(y)


# x_vals = [1,2,3,4]
# y_vals = [1,4,9,16]
# plt.plot(x_vals,y_vals,label = "My firs plot :)")
# plt.xlabel("x axis ")
# plt.ylabel("y axis ")
# plt.title("The title of the graph")
# plt.legend()
# plt.show()
#
# x = np.arange(0,10,0.1)
# plt.figure(figsize=(20, 10))
# y = np.sin(x)
    n = [0, 1, 2]
    # plt.plot(x,y,"D-")
    # plt.plot(x, y, "ro-")

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i, txt in enumerate(n):
        ax.annotate(n[i], (x[i]+0.005, y[i]+0.005))#, arrowprops=dict(arrowstyle="->"))
    plt.show()
