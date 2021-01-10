from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.MC = 0
        self.edgeSize = 0
        self.nodes = {}
        self.neighbors = {}

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        id1_in = {}
        for k in self.nodes:
            new_ni = self.neighbors.get(k)
            if id1 in new_ni.keys():
                id1_in[k] = new_ni[id1]

        if id1_in == {}:
            return {}
        return id1_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.neighbors.get(id1)

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
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
        if node_id in self.nodes.keys():
            return False
        self.nodes[node_id] = pos
        self.neighbors[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
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
