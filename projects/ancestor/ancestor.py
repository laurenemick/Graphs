class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # keys are all verts in the graph, values are sets of adj verts

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    # Instantiate your graph
    graph = Graph()

    for pair in ancestors:
        # if it doesn't exists, then add
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])

        # connect with edge from child (1) to parent (0)
        graph.add_edge(pair[1], pair[0])

    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    q = Queue()
    q.enqueue([starting_node])
	
    longest_path = []

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()

        # if path is longer than longest path
        if len(path) > len(longest_path):
            # set longest path to this path
            longest_path = path

        # If there is more than one ancestor tied for "earliest"
        if len(path) == len(longest_path):
            # return the one with the lowest numeric ID
            if path[-1] < longest_path[-1]:
                longest_path = path

        # Then add A PATH TO its neighbors to the back of the queue
        for neighbor in graph.get_neighbors(path[-1]):
            # COPY THE PATH
            path_copy = path.copy()
            # APPEND THE NEIGHOR TO THE BACK
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    # If the input individual has no parents
    if len(longest_path) <= 1:
        return -1
    else:
        # otherwise, return last value of longest path
        return longest_path[-1]


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1))