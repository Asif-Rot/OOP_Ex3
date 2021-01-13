import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for i in range(5):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1.0)
        self.graph.add_edge(0, 2, 1.1)
        self.graph.add_edge(1, 3, 1.2)
        self.graph.add_edge(1, 4, 1.3)
        self.graph.add_edge(2, 0, 1.4)
        self.graph.add_edge(2, 3, 1.5)
        self.graph.add_edge(3, 1, 1.5)
        self.graph.add_edge(3, 4, 1.6)
        self.graph.add_edge(4, 0, 1.7)
        self.graph.add_edge(4, 1, 1.8)
        self.graph.add_edge(4, 3, 1.9)

    def test_v_size(self):
        self.assertEqual(5, self.graph.v_size())
        self.assertTrue(self.graph.add_node(5))
        self.assertEqual(6, self.graph.v_size())
        self.assertFalse(self.graph.add_node(1))
        self.assertEqual(6, self.graph.v_size())
        self.assertTrue(self.graph.add_node(6))
        self.assertEqual(7, self.graph.v_size())

    def test_e_size(self):
        self.assertEqual(11, self.graph.e_size())
        self.assertFalse(self.graph.add_edge(4, 3, 51.12))
        self.assertEqual(11, self.graph.e_size())
        self.assertTrue(self.graph.remove_node(1))
        self.assertEqual(6, self.graph.e_size())

    def test_add_node(self):
        self.assertEqual(5, self.graph.v_size())
        self.assertTrue(self.graph.add_node(13))
        self.assertEqual(6, self.graph.v_size())
        self.assertEqual(17, self.graph.get_mc())
        self.assertFalse(self.graph.add_node(4))
        self.assertEqual(17, self.graph.get_mc())

    def test_remove_node(self):
        self.assertEqual(16, self.graph.get_mc())
        self.assertEqual(5, self.graph.v_size())
        self.assertTrue(self.graph.remove_node(1))
        self.assertEqual(4, self.graph.v_size())
        self.assertEqual(17, self.graph.get_mc())
        self.assertFalse(self.graph.remove_node(9))
        self.assertEqual(4, self.graph.v_size())
        self.assertEqual(17, self.graph.get_mc())

    def test_add_edge(self):
        self.assertEqual(11, self.graph.e_size())
        self.assertTrue(self.graph.add_edge(0, 3, 4.99))
        self.assertEqual(12, self.graph.e_size())
        self.assertEqual(17, self.graph.get_mc())
        self.assertFalse(self.graph.add_edge(1, 4, 3.99))
        self.assertFalse(self.graph.add_edge(4, 51, 1))
        self.assertFalse(self.graph.add_edge(51, 4, 1))
        self.assertFalse(self.graph.add_edge(51, 12, 13))
        self.assertEqual(12, self.graph.e_size())
        self.assertEqual(17, self.graph.get_mc())

    def test_remove_edge(self):
        self.assertEqual(11, self.graph.e_size())
        self.assertTrue(self.graph.remove_edge(4, 3))
        self.assertEqual(10, self.graph.e_size())
        self.assertEqual(17, self.graph.get_mc())
        self.assertFalse(self.graph.remove_edge(3, 2))
        self.assertEqual(10, self.graph.e_size())
        self.assertEqual(17, self.graph.get_mc())

    def test_all_in_edges_of_node(self):
        self.assertIsNot({}, self.graph.all_in_edges_of_node(1))
        self.assertIsNot({}, self.graph.all_in_edges_of_node(2))
        self.assertIsNot({}, self.graph.all_in_edges_of_node(3))
        self.assertIsNot({}, self.graph.all_in_edges_of_node(4))
        self.assertTrue(self.graph.remove_edge(0, 2))
        self.assertEqual({}, self.graph.all_in_edges_of_node(2))

    def test_all_out_edges_of_node(self):
        self.assertIsNotNone(self.graph.all_out_edges_of_node(1))
        self.assertIsNotNone(self.graph.all_out_edges_of_node(2))
        self.assertIsNotNone(self.graph.all_out_edges_of_node(3))
        self.assertIsNotNone(self.graph.all_out_edges_of_node(4))
        self.assertIsNone(self.graph.all_out_edges_of_node(10))
        self.assertIsNone(self.graph.all_out_edges_of_node(22))

    def test_get_mc(self):
        self.assertEqual(16, self.graph.get_mc())


if __name__ == '__main__' :
    unittest.main()
