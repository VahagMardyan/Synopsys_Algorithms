from collections import deque
from enum import Enum

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    # # Colors: 0->white, 1->gray, 2->black
    def __init__(self, name):
        self.name = name
        self.color = Color.WHITE
        self.d = float("inf") # # distance
        self.p = None # # predecessor
        self.f = 0 # # Finish time

class Graph:
    def __init__(self, adj_list):
        self.adj = adj_list
        self.time = 0

    def BFS(self, s:Vertex):
        """
            Breadth-First-Search
        """
        for u in self.adj:
            if u != s:
                u.color = Color.WHITE
                u.d = float("inf")
                u.p = None
        
        s.color = Color.GRAY
        s.d = 0
        s.p = None
        
        Q = deque([s])
        while Q:
            u = Q.popleft()

            for v in self.adj[u]:
                if v.color == Color.WHITE:
                    v.color = Color.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.append(v)

            u.color = Color.BLACK

    def DFS(self):
        """
            Depth-First-Search
        """
        for u in self.adj:
            u.color = Color.WHITE
            u.p = None
        self.time = 0
        for u in self.adj:
            if u.color == Color.WHITE:
                self.__dfs_visit__(u)

    def __dfs_visit__(self, u:Vertex):
        self.time += 1
        u.d = self.time
        u.color = Color.GRAY
        for v in self.adj[u]:
            if v.color == Color.WHITE:
                v.p = u
                self.__dfs_visit__(v)
        u.color = Color.BLACK
        self.time += 1
        u.f = self.time

a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
h = Vertex("H")
x = Vertex("X")

""" Adjacency Matrix
    A|B|C|D|E|F|H|X|
A   0|1|1|0|0|0|0|0|
B   1|0|0|0|0|0|0|0|
C   1|0|0|0|0|1|1|0|
D   0|0|0|0|1|1|0|0|
E   0|0|0|1|0|0|0|0|
F   0|0|1|1|0|0|0|0|
H   0|0|1|0|0|0|0|0|
X   1|0|0|0|0|0|0|0|
"""

adj_map = {
    a: [b,c],
    b: [a],
    c: [a,f,h],
    d: [e,f],
    e: [d],
    f: [c,d],
    h: [c],
    x: [a],
}

g = Graph(adj_map)
g.BFS(c)
print(e.d)
