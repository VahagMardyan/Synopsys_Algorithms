from collections import deque
from enum import Enum
import networkx as nx
import matplotlib.pyplot as plt
import heapq, random

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    def __init__(self, name: str):
        self.name: str = name
        self.color: Color = Color.WHITE
        self.d: float = float("inf") # distance
        self.p: Vertex = None        # predecessor
        self.f: float = 0            # Finish time
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __repr__(self):
        return self.name
    
class UnionFind:
    def __init__(self, vertices: list[Vertex]):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False
    
class Wall:
    def __init__(self, u: Vertex, v: Vertex):
        self.u = u
        self.v = v
        self.is_open = False

    def explode(self):
        self.is_open = True
        print(f"The wall between {self.u} and {self.v} has been exploded")

    def __repr__(self):
        return f"Wall({self.u}<->{self.v})"
    
def kruskal_maze(vertices: list[Vertex], walls: list[Wall]):
    dsu = UnionFind(vertices)
    random.shuffle(walls)
    maze_adj = {v: [] for v in vertices}

    for wall in walls:
        u, v = wall.u, wall.v
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            wall.explode()

            maze_adj[u].append((v, 1))
            maze_adj[v].append((u, 1))
        
    return Graph(maze_adj)

class Graph:
    def __init__(self, adj_list: dict):
        self.adj: dict = adj_list
        self.time: float = 0

    def BFS(self, s: Vertex):
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

            for neighbor_info in self.adj[u]:
                v = neighbor_info[0] if isinstance(neighbor_info, tuple) else neighbor_info
                if v.color == Color.WHITE:
                    v.color = Color.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.append(v)

            u.color = Color.BLACK

    def DFS(self):
        for u in self.adj:
            u.color = Color.WHITE
            u.p = None
        self.time = 0
        for u in self.adj:
            if u.color == Color.WHITE:
                self.__dfs_visit__(u)

    def __dfs_visit__(self, u: Vertex):
        self.time += 1
        u.d = self.time
        u.color = Color.GRAY
        
        for neighbor_info in self.adj[u]:
            v = neighbor_info[0] if isinstance(neighbor_info, tuple) else neighbor_info
            if v.color == Color.WHITE:
                v.p = u
                self.__dfs_visit__(v)
        u.color = Color.BLACK
        self.time += 1
        u.f = self.time

    def dijkstra(self, start: Vertex, target: Vertex):
        dist = {n: float('inf') for n in self.adj}
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            d, u = heapq.heappop(pq)
            
            if u == target:
                break
                
            if d > dist[u]:
                continue

            for v, w in self.adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    v.p = u
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist[target]
    
    def undirected_visualisation(self):
        G = nx.Graph()
        node_colors = []

        for u, neighbors in self.adj.items():
            G.add_node(u)
            for item in neighbors:
                v = item[0] if isinstance(item, tuple) else item
                G.add_edge(u, v)
        
        for node in G.nodes():
            if node.color == Color.WHITE:
                node_colors.append("white")
            elif node.color == Color.GRAY:
                node_colors.append("lightgray")
            elif node.color == Color.BLACK:
                node_colors.append("black")

        plt.figure(figsize=(8, 6))
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
        G = nx.DiGraph() 
        
        for u, neighbors in self.adj.items():
            G.add_node(u)
            for item in neighbors:
                v = item[0] if isinstance(item, tuple) else item
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

    def maze_visualisation(self):
        G = nx.Graph()
        pos = {}

        for u, neighbors in self.adj.items():
            G.add_node(u)
            
            coords = u.name.replace("(", "").replace(")", "").split(",")
            x = int(coords[0])
            y = -int(coords[1])
            pos[u] = (x, y)

            for item in neighbors:
                v = item[0] if isinstance(item, tuple) else item
                G.add_edge(u, v)

        plt.figure(figsize=(7, 7))
        nx.draw(G, pos,
                with_labels=True,
                node_color='lightgreen',
                node_size=1200,
                font_size=10,
                font_weight="bold",
                edge_color='black',
                width=3,
                edgecolors='black'
        )
        plt.title("Kruskal's Maze Grid")
        plt.axis('off')
        plt.show()