"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

		# Init:
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)   # "Visit" the node
                visited.add(v)
                
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        # Init:
        s.push(starting_vertex)

		# While queue isn't empty
        while s.size() > 0:
            v = s.pop()
            
            if v not in visited:
                print(v)   # "Visit" the node
                visited.add(v)
                
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set([starting_vertex])
        
        for each in self.get_neighbors(starting_vertex):
            if each not in visited:
                visited.add(each)
                self.dft_recursive(each, visited)
                
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()

		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            last_v = path[-1]

			# If that vertex has not been visited...
            if last_v not in visited:
				# CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
				    # IF SO, RETURN PATH
                    return path

				# Mark it as visited...
                print(last_v)   # "Visit" the node
                visited.add(last_v)
                
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_v):
				    # COPY THE PATH
                    path_copy = path.copy()
				    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)

                    # CHECK IF IT'S THE TARGET
                    if neighbor == destination_vertex:
                        # IF SO, RETURN PATH
                        return path_copy
                    # add to queue
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()

		# While the queue is not empty...
        while s.size() > 0:
			# Pop the first PATH
            path = s.pop()
			# Grab the last vertex from the PATH
            last_v = path[-1]

			# If that vertex has not been visited...
            if last_v not in visited:
				# CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
				    # IF SO, RETURN PATH
                    return path

				# Mark it as visited...
                print(last_v)   # "Visit" the node
                visited.add(last_v)
                
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_v):
				    # COPY THE PATH
                    path_copy = path.copy()
				    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)

                    # CHECK IF IT'S THE TARGET
                    if neighbor == destination_vertex:
                        # IF SO, RETURN PATH
                        return path_copy
                    # add to stack
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set([starting_vertex])

        path += [starting_vertex]
        
        for each in self.get_neighbors(starting_vertex):
            if each not in path:
                visited.add(each)
                self.dfs_recursive(each, destination_vertex, visited, path)
                
        return visited


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# print(graph.vertices)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print()
    print("bft:")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print()
    print("dft:")
    graph.dft(1)

    print()
    print("dft_recursive:")
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print()
    print("bfs:")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print()
    print("dfs:")
    print(graph.dfs(1, 6))

    print()
    print("dfs_resursive:")
    print(graph.dfs_recursive(1, 6))
