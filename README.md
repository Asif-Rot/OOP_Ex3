# OOP_Ex3 - last ex for the OOP course.

3 parts of this excrecise:

## 1. write two classes to implement an directional weighed graph.

  ### a. DiGraph. this class implements the simple actions to build the graph:
    
    add node
    
    remove node
    
    add edge - cant update weights
    
    remove edge 
    
    get_all_v - return all the nodes on the graph
    
    all_in_edges_of_node returns all the nodes are connected to the chosen node as dest. (return all src to the specific dest)
    
    all_out_edges_of_node returns all the nodes are connected to the chosen node as src. (return all dest to the specific src)

    Note: there is no class for node_data.

   The way we built the graph:
    There are 2 dictionaries: one for nodes and one for there neighbors. every single node keeps a list of his "out nodes" (as dest)
    
  ### b. GraphAlgo. this class implements the algorithms on the graph, and some more methodes:
      
    load_from_json: load a graph from a json file. If there is no position for some node it will be placed by a random position.
      
    save_to_json: save the chosen graph to a json file. it will be saved on the project package.
      
    shortest_path: Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
                     Return: The distance of the path, a list of the nodes ids that the path goes through.
      
    connected_component: By using Tarjan Algorithm finds the Strongly Connected Component(SCC) that the chosen node is a part of.
                           Return: The list of nodes in the SCC.
      
    connected_components: By using Tarjan Algorithm Finds all the Strongly Connected Component(SCC) in the graph.
      
    plot_graph: Plots the graph.
      
2. 
      
        
