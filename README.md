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
    
    add node - Adding a node to the graph
    
    remove node - Removing a node from the graph
    
    add edge - Adding edge between two nodes (*can't update weights*)
    
    remove edge - Remove edge between two nodes 
    
    get_all_v - returns all the nodes in the graph
    
    all_in_edges_of_node - returns all the nodes that are connected to the chosen node as destination. (return all src to the specific destination)
    
    all_out_edges_of_node - returns all the nodes that are connected to the chosen node as src. (return all destinations fron the specific src)

    Note: there was no need for node_data class.

   _The way we built the graph:_
   
   There are 2 dictionaries: 
   
   - nodes - {key, position}
   - neighbors - {key, {key, weight}} - Every single node keeps a list of his "out nodes" (as destination)
    
#### Test class : TestDiGraph

- In this class all the DiGraph methods are being tested.
    

## Write a class to implement the algorithms for the directed weighted graph
    
### GraphAlgo

_this class implements the algorithms in the graph, and some other more methods:_
      
    load_from_json - Load a graph from a json file. If there is no position for some node it will be placed by a random position.
      
    save_to_json - Save the chosen graph to a json file. It will be saved on the project package.
      
    shortest_path - Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
                    Return: The distance of the path, a list of the nodes ids that the path goes through.
      
    connected_component - By using Kosaraju's algorithm, we can find the Strongly Connected Component(SCC) that the chosen node is a part of.
                          Return: The list of nodes in the SCC that the chosen node is a part of.
      
    connected_components - By using Kosaraju's algorithm, we can find all the Strongly Connected Components(SCC) in the graph.
                           Return: A list of lists of nodes in their SCCs.
      
    plot_graph - Plots the graph.
    
#### **Algorithms:**
    
1. Dijkstra's algorithm: an algorithm for finding the shortest paths between nodes in a graph.
	At first, we initialize all the vertices distance to infinity.
	In the algorithm loop - as long as there are vertices in the queue:
  
	- Each neighbor of that node, will be updated to the minimal value of dist.
    
	- Adding the node which has the shortest distance to the queue.

_For more info:_ (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

![](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

    
2. Kosaraju's strongly connected components algorithm is an algorithm for finding the strongly connected components (SCCs) of a directed graph.
    
	- The key point of the algorithm is that during the first traversal of the graph edges,
	vertices are prepended to the list 'List' in post-order DFS relative to the graph being explored.
	- Second, the algorithm do a post-order DFS on 'tmp_list' in order to pop the root vertices from 'List' and mark the SCCs to a list.
	- Finally, we take this list and turn it into a list of lists where every list is a SCC.
    
_For more info:_ (https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)
   
![](https://miro.medium.com/max/1666/1*mW2CO2dhTkvgsJK7oSrFJg.gif)
      
#### Test class : TestGraphAlgo

- In this class all the GraphAlgo methods are being tested.
                  

## Perform comparisons between this project, our last project (OOP_Ex2) and NetworkX package

In this part we ran the algorithms for comparisons:
- shortest_path
- connected_component
- connected_components
  
  _More info in the Wiki page:_
  
  [Click here](https://github.com/Asif-Rot/OOP_Ex3/wiki)
  
  
        
