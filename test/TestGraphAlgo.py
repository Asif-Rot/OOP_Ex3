import unittest
from numpy import inf

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for i in range(10):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1.0)
        self.graph.add_edge(0, 2, 3.1)
        self.graph.add_edge(2, 0, 2.4)
        self.graph.add_edge(1, 3, 4.2)
        self.graph.add_edge(1, 4, 3.2)
        self.graph.add_edge(2, 3, 1.5)
        self.graph.add_edge(3, 1, 3.5)
        self.graph.add_edge(3, 4, 5.6)
        self.graph.add_edge(4, 0, 2.7)
        self.graph.add_edge(4, 1, 4.8)
        self.graph.add_edge(4, 3, 1.9)
        self.graph.add_edge(5, 4, 7.2)
        self.graph.add_edge(6, 5, 2.2)
        self.graph.add_edge(6, 4, 5.2)
        self.graph.add_edge(4, 6, 1.2)
        self.graph.add_edge(7, 5, 4.1)
        self.graph.add_edge(6, 7, 2.8)
        self.graph.add_edge(8, 0, 9.2)
        self.graph.add_edge(0, 8, 5.2)
        self.graph.add_edge(9, 8, 2.6)
        self.graph.add_edge(8, 9, 7.4)
        self._g = GraphAlgo(self.graph)

    def test_get_graph(self):
        self.assertIsNotNone(self._g.get_graph())
        self.g = DiGraph()
        self._g1 = GraphAlgo(self.g)
        self.assertEqual(0, self._g1.get_graph().v_size())
        self.assertEqual(0, self._g1.get_graph().e_size())
        self.assertEqual(0, self._g1.get_graph().get_mc())
        self.g.add_node(1)
        self.assertEqual(1, self._g1.get_graph().v_size())

    def test_load_and_save(self):
        file = '../data/Legendary_graph.json'
        self._g.save_to_json(file)
        self.gg = DiGraph()
        self._g2 = GraphAlgo(self.gg)
        self.assertTrue(self._g2.load_from_json(file))
        print(self._g2.get_graph())
        self.ggg = DiGraph()
        self._g3 = GraphAlgo(self.ggg)
        self.assertTrue(self._g3.load_from_json('../data/A5'))
        print(self._g3.get_graph())

    def test_shortest_path(self):
        self.assertEqual((1.0, [0, 1]), self._g.shortest_path(0, 1))
        self.assertEqual((12.600000000000001, [0, 8, 9]), self._g.shortest_path(0, 9))
        self.assertEqual((16.799999999999997, [8, 0, 1, 4, 6, 5]), self._g.shortest_path(8, 5))
        self.graph.remove_edge(0, 8)
        self.assertEqual((inf, []), self._g.shortest_path(0, 9))
        self.assertEqual((inf, []), self._g.shortest_path(0, -1))
        self.assertEqual((inf, []), self._g.shortest_path(1232, 51))
        self.assertEqual((inf, []), self._g.shortest_path(-2, 9))
        self.graph.add_edge(5, 6, 0.5)
        self.assertEqual((5.7, [5, 6, 4]), self._g.shortest_path(5, 4))  # Checking if goes through the weightless nodes
        self.graph.add_edge(8, 6, 3.0)
        self.graph.add_edge(6, 9, 1.0)
        self.assertEqual((4.0, [8, 6, 9]), self._g.shortest_path(8, 9))  # Checking if goes through the weightless nodes

    def test_connected_component(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], self._g.connected_component(0))
        self.graph.remove_edge(8, 9)
        self.graph.remove_edge(6, 9)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], self._g.connected_component(0))
        self.graph.add_edge(9, 6, 0.5)
        self.graph.add_edge(6, 9, 1.5)
        self.graph.remove_edge(6, 4)
        self.graph.remove_edge(6, 5)
        self.graph.remove_edge(6, 7)
        self.graph.remove_edge(6, 8)
        self.graph.remove_edge(9, 8)
        self.assertEqual([6, 9], self._g.connected_component(9))
        self.assertEqual([7], self._g.connected_component(7))
        self.assertEqual([5], self._g.connected_component(5))

    def test_connected_components(self):
        self.assertEqual([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], self._g.connected_components())
        self.graph.remove_edge(6, 4)
        self.graph.remove_edge(6, 5)
        self.graph.remove_edge(6, 8)
        self.graph.remove_edge(9, 8)
        self.assertEqual([[0, 1, 2, 3, 4, 5, 6, 7, 8], [9]], self._g.connected_components())
        self.assertEqual(2, len(self._g.connected_components()))
        self.graph.remove_edge(6, 7)
        self.assertEqual([[0, 1, 2, 3, 4, 8], [5], [6], [7], [9]], self._g.connected_components())
        self.assertEqual(5, len(self._g.connected_components()))
        self.graph.add_edge(5, 6, 0.5)
        self.graph.remove_edge(4, 6)
        self.graph.add_edge(6, 5, 6.5)
        self.assertEqual([[0, 1, 2, 3, 4, 8], [5, 6], [7], [9]], self._g.connected_components())
        self.assertEqual(4, len(self._g.connected_components()))

    def test_plot_graph(self):
        # random positions
        self._g.plot_graph()
        # known positions
        self.g5 = DiGraph()
        self._g2 = GraphAlgo(self.g5)
        self._g2.load_from_json('../data/A1')
        self._g2.plot_graph()


if __name__ == '__main__' :
    unittest.main()
