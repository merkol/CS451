from importlib.resources import path
from turtle import distance
from Node import Node
import math
from PriorityQueue import PriorityQueue
from Algorithm import Algorithm

# Do not import anything else. Use only provided imports.


class AStar(Algorithm):
    """
        You should implement the solve method. You can also create new methods inside the class.
    """
    def __init__(self, number_of_nodes: int, start_node: Node, target_node: Node):
        super().__init__(number_of_nodes, start_node, target_node)

    def solve(self) -> list:
        """
            Implement A* algorithm here to solve the problem. You must return the complete path, not the cost.
            self.iteration must be equal number of iteration. Do not forget to update it!
        :return: The path which is a list of nodes.
        """
        # TODO: You should implement inside of this method!
        que = PriorityQueue()
        path = [self.start_node]
        node = self.start_node
        
        for i in node.connections:
            estimated = i.get_estimated_distance(self.target_node)
            distance = node.get_distance(i)
            final = estimated + distance
            que.enqueue(i,final)
            
            
   
        node = que.dequeue()
        path.append(node)
        self.iteration+=1
        for i in range(que.__len__()):
            que.dequeue()
        return path
