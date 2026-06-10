from graphs import *

# a = Vertex("A")
# b = Vertex("B")
# c = Vertex("C")
# d = Vertex("D")
# e = Vertex("E")
# f = Vertex("F")
# h = Vertex("H")
# x = Vertex("X")

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

# adj_map = {
#     a: [b,c],
#     b: [a],
#     c: [a,f,h],
#     d: [e,f],
#     e: [d],
#     f: [c,d],
#     h: [c],
#     x: [a],
# }

# g = Graph(adj_map)
# g.DFS()

# g.dijkstra(adj_map[a], adj_map[x])
# g.directed_visualisation()
# g.undirected_visualisation()
# print(e.d)

# a = Vertex("A")
# b = Vertex("B")
# c = Vertex("C")

# adj_with_weights = {
#     a: [(b,4), (c,2)],
#     b: [(c,1)],
#     c: [(b,2)]
# }

# g = Graph(adj_with_weights)

# shortest_distance = g.dijkstra(start=a, target=b)
# print(f"Shortest distance from A to B: {shortest_distance}")

def draw_real_maze(walls: list[Wall], grid_size: int):
    plt.figure(figsize=(6, 6))
    
    # Նկարում ենք արտաքին սահմանները (եզրագծերը)
    plt.plot([0, grid_size, grid_size, 0, 0], [0, 0, grid_size, grid_size, 0], color="black", linewidth=5)

    for wall in walls:
        if not wall.is_open:  # Եթե պատը դեռ կա (չի պայթել)
            # Ստանում ենք երկու վանդակների կոորդինատները
            c1 = wall.u.name.replace("(", "").replace(")", "").split(",")
            c2 = wall.v.name.replace("(", "").replace(")", "").split(",")
            x1, y1 = int(c1[0]), int(c1[1])
            x2, y2 = int(c2[0]), int(c2[1])

            # Հաշվում ենք պատի գծի կոորդինատները
            if x1 == x2:  # Հորիզոնական պատ հարևանների միջև (ուղղահայաց գիծ)
                wall_x = [x1 + 1, x1 + 1]
                wall_y = [max(y1, y2), max(y1, y2) + 1]
            else:  # Ուղղահայաց հարևաններ (հորիզոնական գիծ)
                wall_x = [max(x1, x2), max(x1, x2) + 1]
                wall_y = [y1 + 1, y1 + 1]

            plt.plot(wall_x, wall_y, color="black", linewidth=4)

    plt.xlim(-0.5, grid_size + 0.5)
    plt.ylim(grid_size + 0.5, -0.5) # Շրջում ենք Y-ը, որ վերևից սկսվի
    plt.axis('off')
    plt.title("Generated Labirinth (True Walls)")
    plt.show()

GRID_SIZE = 5
vertices_grid = {}
all_vertices = []
all_walls = []

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        v = Vertex(f"({x},{y})")
        vertices_grid[(x,y)] = v
        all_vertices.append(v)

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        if x + 1 < GRID_SIZE:
            all_walls.append(Wall(vertices_grid[(x,y)], vertices_grid[(x + 1,y)]))
        if y + 1 < GRID_SIZE:
            all_walls.append(Wall(vertices_grid[(x, y)], vertices_grid[(x, y + 1)]))

print("--- Generating a Complex 5x5 Maze ---")
maze_graph = kruskal_maze(all_vertices, all_walls)

start_node = vertices_grid[(0, 0)]
target_node = vertices_grid[(0, 2)]

print("\n--- Searching the Shortest Path with Dijkstra ---")
shortest_path_len = maze_graph.dijkstra(start_node, target_node)
print(f"\nShortest path length from {start_node} to {target_node} is: {shortest_path_len} steps.")

print("\n--- Visualizing Maze ---")
maze_graph.maze_visualisation()