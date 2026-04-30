from collections import deque
from enum import Enum
import networkx as nx
import matplotlib.pyplot as plt

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    def __init__(self, name:str):
        self.name:str = name
        self.color:Color = Color.WHITE
        self.d:float = float("inf") # # distance
        self.p:Vertex = None # # predecessor
        self.f:float = 0 # # Finish time
    
    def __repr__(self):
        return self.name

class Graph:
    def __init__(self, adj_list:dict):
        self.adj:dict = adj_list
        self.time:float = 0

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

    def undirected_visualisation(self):
        """
            Undirected graph visualisation
        """
        G = nx.Graph()
        node_colors = []

        for u, neighbors in self.adj.items():
            G.add_node(u)
            for v in neighbors:
                G.add_edge(u,v)
        
        for node in G.nodes():
            if node.color == Color.WHITE:
                node_colors.append("white")
            elif node.color == Color.GRAY:
                node_colors.append("lightgray")
            elif node.color == Color.BLACK:
                node_colors.append("black")

        plt.figure(figsize=(8,6))
        nx.draw(G,
                with_labels=True,
                node_color=node_colors,
                node_size=2000,
                font_size=16,
                font_weight="bold",
                edge_color='gray',
                edgecolors='black',
                font_color='orange'
            )
        plt.title("Graph Visualisation (Current State)")
        plt.show()

    def directed_visualisation(self, title_suffix=""):
        """
            Directed graph visualisation
        """
        G = nx.DiGraph() 
        
        for u, neighbors in self.adj.items():
            G.add_node(u)
            for v in neighbors:
                G.add_edge(u, v)

        node_colors = []
        for node in G.nodes():
            if node.color == Color.WHITE:
                node_colors.append('white')
            elif node.color == Color.GRAY:
                node_colors.append('lightgray')
            elif node.color == Color.BLACK:
                node_colors.append('black')

        plt.figure(figsize=(10, 8))
        
        pos = nx.spring_layout(G)

        nx.draw(G, pos,
                with_labels=True,
                node_color=node_colors,
                node_size=2000,
                font_size=16,
                font_weight='bold',
                edge_color='gray',
                edgecolors='black',
                font_color='orange',
                arrows=True,
                arrowsize=30,
                connectionstyle='arc3,rad=0.1'
        )

        plt.title(f"Directed Graph Visualization {title_suffix}")
        plt.show()

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
# g.DFS()
g.directed_visualisation()
# g.undirected_visualisation()
# print(e.d)

