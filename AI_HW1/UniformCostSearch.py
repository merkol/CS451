from Node import Node
import math
from PriorityQueue import PriorityQueue
from Algorithm import Algorithm

# Do not import anything else. Use only provided imports.


class UniformCostSearch(Algorithm):
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
        
        que.enqueue([0,node,[node]],0)
        while que:
            cost,node,path = que.dequeue()

            
            
            if path[0] == self.start_node and path[-1] == self.target_node and len(path) == self.number_of_nodes:
                break
            for i in node.connections:
                if i not in path:
                    total_cost = cost + node.get_distance(i)
                    que.enqueue([total_cost,i,path+[i]],total_cost)
            self.iteration+=1
        
        return path
