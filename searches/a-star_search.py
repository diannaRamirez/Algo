"""
Priority Queue class, which removes elements from the queue based on the least cost+heuristic value.

"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        if data not in self.queue:
            self.queue.append(data)

    def getA(self):
        try:
            maxi = 0
            for i in range(len(self.queue)):
                if (self.queue[i][0] + self.queue[i][2]) < (
                    self.queue[maxi][0] + self.queue[maxi][2]
                ):
                    maxi = i
            item = self.queue[maxi]
            del self.queue[maxi]
            return item
        except IndexError:
            return


def A_star_Traversal(graph, heuristic, start, goal):
    l = []
    path = []
    visited = set()
    goal_paths = []
    path.append(start)

    if start not in range(len(graph)):
        return []
    if start in goal:
        return path

    frontierA = PriorityQueue()

    path_cost = 0
    frontierA.insert([path_cost, path, heuristic[start]])

    while not frontierA.isEmpty():

        current_node_val = frontierA.getA()

        path_cost_till_now = current_node_val[0]
        path_till_now = current_node_val[1]
        current_node = path_till_now[-1]

        visited.add(current_node)

        if current_node in goal:
            ele = [path_till_now, path_cost_till_now]
            if ele not in goal_paths:
                goal_paths.append(ele)

        children_of_current = graph[current_node]

        for child_node in range(0, len(children_of_current)):
            if child_node not in visited:

                if children_of_current[child_node] > 0:
                    path_to_child = path_till_now.copy()
                    path_to_child.append(child_node)
                    cost_of_child = (
                        node_cost(graph, current_node, child_node) + path_cost_till_now
                    )
                    new_element = [cost_of_child, path_to_child, heuristic[child_node]]
                    frontierA.insert(new_element)

    for i in range(len(goal_paths)):
        mini = 0
        if goal_paths[i][1] < goal_paths[mini][1]:
            mini = i
        item = goal_paths[mini]

        return item[0]


"""
Function tri_traversal - performs DA* traversal and returns the path for the traversal

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n], start_point, goals[m]

"""


def tri_traversal(cost, heuristic, start_point, goals):

    visited = set()
    t1 = A_star_Traversal(cost, heuristic, start_point, goals)

    l.append(t1)
    return l


"""

Sample Test case 

    size of cost matrix is 11x11
    0th row and 0th column is ALWAYS 0
    Number of nodes is 10
    size of heuristic list is 11
    0th index is always 0

    cost = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
        [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
        [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
        [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
        [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
        [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
        [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
    ]
    heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]

    try:
        if (tri_traversal(cost, heuristic, 1, [6, 7, 10]))[0] == [1, 5, 4, 7]:
            print("SAMPLE TEST CASE 3 FOR THE  A_star_TRAVERSAL PASSED")
        else:
            print("SAMPLE TEST CASE 3 FOR THE  A_star_TRAVERSAL FAILED")
    except:
        print("SAMPLE TEST CASE 3 FOR THE A_star_TRAVERSAL FAILED")

"""