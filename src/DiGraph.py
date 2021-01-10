from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        """
        Init the graph
        """
        self.MC = 0
        self.edgeSize = 0
        self.nodes = {}
        self.neighbors = {}

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edgeSize

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        id1_in = {}
        for k in self.nodes:
            new_ni = self.neighbors.get(k)
            if id1 in new_ni.keys():
                id1_in[k] = new_ni[id1]

        if id1_in == {}:
            return {}
        return id1_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.neighbors.get(id1)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 == id2:
            return False

        if not {id1, id2} <= self.nodes.keys():
            return False
        try:
            tmp = self.neighbors[id1][id2]
            return False
        except KeyError:
            self.neighbors[id1][id2] = weight
            self.edgeSize += 1
            self.MC += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id in self.nodes.keys():
            return False
        self.nodes[node_id] = pos
        self.neighbors[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.nodes.keys():
            for k in self.neighbors.keys():
                if node_id in self.neighbors.get(k):
                    del self.neighbors[k][node_id]
                    self.edgeSize -= 1
                    self.MC += 1

                if k in self.neighbors.get(node_id):
                    del self.neighbors[node_id][k]
                    self.edgeSize -= 1
                    self.MC += 1

            del self.nodes[node_id]
            self.MC += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if not {node_id1, node_id2} <= self.nodes.keys():
            return False
        if node_id1 == node_id2:
            return False
        if node_id2 in self.neighbors.get(node_id1):
            del self.neighbors[node_id1][node_id2]
            self.edgeSize -= 1
            self.MC += 1
            return True
        return False

    def __str__(self):
        """
        Prints the graph
        """
        Nodes = {}

        for i in self.nodes:
            Nodes[i] = {
                "id": i,
                "pos": self.nodes.get(i)
            }

        Edges = {}
        for i in self.nodes:
            for k in self.neighbors.get(i):
                Edges[i] = {
                    "src": i, "dest": k, "w": self.neighbors[i][k]}    # Edges = {0, 1, 1.2}

        return "Edges "+format(Edges)+", Nodes "+format(Nodes)

