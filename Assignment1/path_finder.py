import math

class Node:
    def __init__(self, x, y, value, f = 0, g = 0, h = 0, parent = 0):
        self.x = x # row
        self.y = y # column
        self.value = value # 1 for unblocked, 0 for blocked
        self.f = f # path cost + heuristic
        self.g = g # path cost
        self.h = h # heuristic
        self.parent = parent
    def update_f(self):
        self.f = self.g + self.h
    def location(self):
        return self.x, self.y
########################################################################################
### global variables
########################################################################################
START_NODE
GOAL_NODE
WEIGHT = 1
ZERO_HEURISTICS = 1
numExpansions = 0
numSteps = 0

def generateNeighbors(map, origin_node):
    """
        Args:
            map: 2D Array of 0 and 1 values indicating blocked (0) and unblocked (1) cells
            origin_node: Node from which to derive its neighbors
        Returns:
            List of Nodes which are neighbors (UP, DOWN, LEFT, and RIGHT) of the origin_node
    """

    neighbors = []
    x, y = origin_node.location()
    if(x - 1 < 0):
        pass
    else:
        if(map[x-1][y] == 1):#getting UP
            neighbors.append(Node(x-1,y,1))
    if(x + 1 >= len(map)):
        pass
    else:
        if(map[x+1][y] == 1):# getting DOWN
            neighbors.append(Node(x+1,y,1))
           
    if(y - 1 < 0):
        pass
    else:
        if(map[x][y-1] == 1):#getting LEFT
            neighbors.append(Node(x,y-1,1))
    if(y + 1 >= len(map[x])):
        pass
    else:
        if(map[x][y+1] == 1):# getting RIGHT
            neighbors.append(Node(x,y+1,1))
    return neighbors
def h(origin_node, goal_node): 
    """ function will compute the heuristic. It will compute the manhattan distance if zero_heuristic variable is one and
    and the zero heuristic if zero is zero """
    return ZERO_HEURISTIC * round( math.sqrt(((goal_node.x - origin_node.x)**2)+((goal_node.y - origin_node.y)**2)), 2)

def g(origin_node, node):
    """ returns cost from the origin node to any node """
    return round( math.sqrt(((node.x - origin_node.x)**2)+((node.y - origin_node.y)**2)), 2)
def PathFinder(map, initial_x, initial_y, goal_x, goal_y):
    """
        Args:
            map: 2D Array of 0 and 1 values indicating blocked (0) and unblocked (1) cells
            initial_x: integer value denoting the starting row
            initial_y: integer value denoting the starting column
            goal_x: integer value denoting the goal row
            goal_y: integer value denoting the goal column
        Returns:
            List of 2-tuples indicating a path from the starting state to the goal state
                i.e. path from (0,0) -> (2,2): ((0,0), (0,1), (1,1), (1,2), (2,2))
    """

    pathExists = True # boolean flag for whether or not path exists, assumed True until determined False

    open_list = []
    open_list.append(Node(initial_x, initial_y, map[initial_x][initial_y]))
    closed_list = []

    while(len(open_list) != 0):
        q = open_list[0]
        for node in open_list: # determine lowest f score in open_list
            if(node.f < q.f):
                q = node
            else:
                continue
        if(q.x == goal_x and q.y == goal_y):
            closed_list.append((q.x, q.y))
            return closed_list
        else:
            closed_list.append((q.x, q.y))
            # create a generateNeighbors(Node) function
