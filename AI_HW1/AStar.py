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
        node = self.start_node
        path = [node]
        
        for j in range(self.number_of_nodes):
            for i in node.connections:
                if i in path:
                    pass
                else: 
                    estimated = i.get_estimated_distance(self.target_node)
                    distance = node.get_distance(i)
                    final = estimated + distance
                    if i !='T':   
                        que.enqueue(i,final)
                    elif i=='T' and j == self.number_of_nodes-1:
                        que.enqueue(i,final)

            
            
            if len(que) != 0:
                node = que.dequeue()
                path.append(node)
                self.iteration+=1
            if len(que) != 0:
                for i in range(len(que)):
                    que.dequeue()
        return path
