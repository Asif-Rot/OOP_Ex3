# OOP_Ex3 - last ex for the OOP course.

**Authors: Asif Rot & Maoz Lev**

![](https://stock.wikimini.org/w/images/2/2c/Pok%C3%A9mon.gif)

File list
------------

GraphInterface.py - Interface

DiGraph.py - GraphInterface implementation

GraphAlgoInterface.py - Interface

GraphAlgo.py - GraphAlgoInterface implementation

Readme.txt - This file

In this file, we will explain:
- Why we chose the data structures we used in this project.
- How we implemented the interfaces.
- Which algorithms we used.


### _There are 3 parts for this excrecise:_

## Write a class to implement a directed weighted graph.

### DiGraph

_this class implements the simple actions that build our graph:_
    
    add node
    
    remove node
    
    add edge - *can't update weights*
    
    remove edge 
    
    get_all_v - returns all the nodes in the graph
    
    all_in_edges_of_node - returns all the nodes that are connected to the chosen node as destination. (return all src to the specific destination)
    
    all_out_edges_of_node - returns all the nodes that are connected to the chosen node as src. (return all destinations fron the specific src)

    Note: there is no need for node_data class.

   _The way we built the graph:_
   
   There are 2 dictionaries: 
   
   - nodes - {key, position}
   - neighbors - {key, {key, weight}} - Every single node keeps a list of his "out nodes" (as destination)
    
#### Test class : TestDiGraph

- In this class all the graph methods are being tested.
    

## Write a class to implement the algorithms for the directed weighted graph
    
### GraphAlgo

_this class implements the algorithms in the graph, and some other more methods:_
      
    load_from_json - Load a graph from a json file. If there is no position for some node it will be placed by a random position.
      
    save_to_json - Save the chosen graph to a json file. It will be saved on the project package.
      
    shortest_path - Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
                    Return: The distance of the path, a list of the nodes ids that the path goes through.
      
    connected_component - By using Tarjan Algorithm, we can find the Strongly Connected Component(SCC) that the chosen node is a part of.
                          Return: The list of nodes in the SCC.
      
    connected_components - By using Tarjan Algorithm, we can find all the Strongly Connected Component(SCC) in the graph.
                           Return: The list of nodes in the SCC.
      
    plot_graph - Plots the graph.
    
#### **Algorithms:**
    
1. Dijkstra's algorithm: an algorithm for finding the shortest paths between nodes in a graph. (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

![](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

    
2. Tarjan's strongly connected components algorithm is an algorithm for finding the strongly connected components (SCCs) of a directed graph.          
   (https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
   
![](https://upload.wikimedia.org/wikipedia/commons/6/60/Tarjan%27s_Algorithm_Animation.gif)
      
#### Test class : TestGraphAlgo

- In this test all the methodes are being test. 
                  

## Perform comparisons between this project, our last project (OOP_Ex2) and NetworkX package

In this part we ran the algorithms for comparisons:
- shortest_path
- connected_component
- connected_components
  
  _More info in the Wiki page:_
  
  [Click here](https://github.com/Asif-Rot/OOP_Ex3/wiki/Comparisons)
  
  
        
