from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph

import queue
import json
from typing import List
import matplotlib.pyplot as plt
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        """
        Init graph Algo
        """
        self.graph = g
        self.vis = {}

    def get_graph(self) -> GraphInterface:
        """
        @return the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        with open(file_name) as json_file:
            data = json.load(json_file)
            if data is not None:
                for node in data["Nodes"]:
                    key = node["id"]
                    if len(node) > 1:
                        pos = node["pos"]
                        self.graph.add_node(key, pos)
                    else:
                        self.graph.add_node(key)
                for edge in data["Edges"]:
                    self.graph.add_edge(edge["src"], edge["dest"], edge["w"])

                return True

        return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        with open(file_name, 'w') as file:
            try:
                graph = {"Nodes": [], "Edges": []}
                for i in self.graph.nodes.keys():
                    for j in self.graph.neighbors.get(i):
                        graph["Edges"].append({"src": i, "w": self.graph.neighbors[i][j], "dest": j})

                for key, pos in self.graph.nodes.items():
                    if key is not None:
                        graph["Nodes"].append({"pos": str(pos), "id": key})
                    else:
                        graph["Nodes"].append({"pos": None, "id": key})
                json.dump(graph, file)
                return True
            except ValueError as ve:
                print("Could not save to json: " + ve.__str__())
                return False
            finally:
                file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Example:
#        >>> from GraphAlgo import GraphAlgo
#        >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        if not {id1, id2} <= self.graph.nodes.keys():  # Checking if the keys exist
            return float('inf'), []

        if id1 == id2:
            return float('inf'), []

        # Dijkstra algorithm
        weights = {}
        daddy = {}
        for n in self.graph.nodes:
            weights[n] = float('inf')
            daddy[n] = None

        weights[id1] = 0.0
        q = queue.PriorityQueue()
        q.put(id1)

        while not q.empty():
            tmp = q.get()
            for e in self.graph.all_out_edges_of_node(tmp):
                cur_dis = weights.get(tmp)
                full_dis = cur_dis + self.graph.neighbors.get(tmp).get(e)
                dest_dis = weights.get(e)
                if full_dis < dest_dis:
                    weights[e] = full_dis
                    daddy[e] = tmp
                    q.put(e)

        if daddy.get(id2) is None:
            return float('inf'), []

        rev = queue.LifoQueue(maxsize=self.graph.v_size())
        p = id2
        rev.put(p)
        for i in range(1, len(daddy)):
            if daddy.get(p) is None:
                break
            rev.put(daddy.get(p))
            p = daddy.get(p)

        path = []
        while not rev.empty():
            tmp = rev.get()
            path.append(tmp)

        return weights.get(id2), path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        vis = {}
        q = queue.Queue()

        if id1 not in self.graph.nodes:
            return []
        if self.graph.v_size() == 1:
            return [id1]

        for i in self.graph.nodes:
            vis[i] = "not_vis"

        vis[id1] = "vis"
        q.put(id1)

        out_list = []
        while not q.empty():
            node = q.get()
            if vis[node] == "vis":
                for k in self.graph.all_out_edges_of_node(node):
                    if vis[k] == "not_vis":
                        q.put(k)
                        vis[k] = "vis"

            out_list.append(node)
            vis[node] = "complete"

        for i in self.graph.nodes:
            vis[i] = "not_vis"

        vis[id1] = "vis"
        q.put(id1)

        in_list = []
        while not q.empty():
            node = q.get()
            if vis[node] == "vis":
                for k in self.graph.all_in_edges_of_node(node):
                    if vis[k] == "not_vis":
                        q.put(k)
                        vis[k] = "vis"
                in_list.append(node)
                vis[node] = "complete"
        return list(set(out_list) & set(in_list))

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        if len(self.graph.nodes) == 0:
            return []
        vis = {}
        list_for_us = []
        for i in self.graph.nodes:
            if i not in vis:
                sure = self.connected_component(i)
                for j in sure:
                    vis[j] = j
                list_for_us.append(sure)
        return list_for_us

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        tupleee = []
        x = []
        y = []
        n = []

        for i in self.graph.nodes.keys():
            if i is not None:
                n.append(i)

        unused_values_x = []
        unused_values_y = []
        for i in range(len(self.graph.nodes)):
            unused_values_x.append(random.uniform(0.0, 10000.0))
            unused_values_y.append(random.uniform(0.0, 10000.0))

        for j in range(len(self.graph.nodes)):
            tmp = self.graph.nodes[j]
            if tmp is not None:
                tupleee.append(tmp.split(","))
            else:
                tupleee.append([unused_values_x.pop(), unused_values_y.pop(), 0.0])

        for k in range(len(tupleee)):
            x.append(float(tupleee[k][0]))
            y.append(float(tupleee[k][1]))

        ax = plt.axes()
        ax.scatter(x, y)
        for o, txt in enumerate(n):
            ax.annotate(n[o], (x[o], y[o] + 0.10))

        for h in self.graph.nodes:
            for p in self.graph.neighbors.get(h):
                src_x = float(tupleee[h][0])
                dst_x = float(tupleee[p][0])
                src_y = float(tupleee[h][1])
                dst_y = float(tupleee[p][1])
                plt.plot(src_x, src_y, dst_x, dst_y, marker='o')
                ax.annotate("",
                            xy=(src_x, src_y), xycoords='data',
                            xytext=(dst_x, dst_y), textcoords='data',
                            arrowprops=dict(arrowstyle="->",
                                            connectionstyle="arc3"),
                            )

        plt.xlabel(" x --> ")
        plt.ylabel(" y --> ")
        plt.title("Our graph!")

        plt.show()
