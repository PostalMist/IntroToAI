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
    def update_f():
        self.f = self.g + self.h
    def location():
        return self.x, self.y

def path_cost(origin_node):
    """
        Args:
            origin_node: Node from which to derive its path cost
        Returns:
            Nothing, sets the origin_node's g value
    """

    if(origin_node.value == 1):
        origin_node.g = 0
        return
    elif(origin_node.value == 0):
        origin_node.g = math.Inf
        return

def generateNeighbors(maze_map, origin_node):
    """
        Args:
            maze_map: 2D Array of 0 and 1 values indicating blocked (0) and unblocked (1) cells
            origin_node: Node from which to derive its neighbors
        Returns:
            List of Nodes which are neighbors (UP, DOWN, LEFT, and RIGHT) of the origin_node
    """

    neighbors = []
    x, y = origin_node.location()

    if(x == 0): # top left corner or top right corner
        if(y == 0): # top left
            right = Node(x + 1, y, maze_map[x + 1][y])
            path_cost(right)
            right.update_f()

            down = Node(x, y + 1, maze_map[x][y + 1])
            path_cost(down)
            down.update_f()

            neighbors.append(right)
            neighbors.append(down)
        elif(y == len(maze_map[x]) - 1): # top right
            left = Node(x - 1, y, maze_map[x - 1][y])
            path_cost(left)
            left.update_f()

            down = Node(x, y + 1, maze_map[x][y + 1])
            path_cost(down)
            down.update_f()

            neighbors.append(left)
            neighbors.append(down)
        else: # top border
            right = Node(x + 1, y, maze_map[x + 1][y])
            path_cost(right)
            right.update_f()

            left = Node(x - 1, y, maze_map[x - 1][y])
            path_cost(left)
            left.update_f()

            down = Node(x, y + 1, maze_map[x][y + 1])
            path_cost(down)
            down.update_f()

            neighbors.append(right)
            neighbors.append(left)
            neighbors.append(down)

def PathFinder(maze_map, initial_x, initial_y, goal_x, goal_y):
    """
        Args:
            maze_map: 2D Array of 0 and 1 values indicating blocked (0) and unblocked (1) cells
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
    open_list.append(Node(initial_x, initial_y, maze_map[initial_x][initial_y]))
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
