# Reload numbers from the newly uploaded file
file_path = './source.txt'

with open(file_path, 'r') as file:
    numbers = file.read().splitlines()

# Improved graph-based approach
from collections import defaultdict, deque

# Build a graph where each piece connects to others
def build_graph(pieces):
    graph = defaultdict(list)
    for i, piece1 in enumerate(pieces):
        for j, piece2 in enumerate(pieces):
            if i != j:  # Avoid self-loops
                if piece1[-2:] == piece2[:2] or piece1[:2] == piece2[-2:]:
                    graph[piece1].append(piece2)
    return graph

def find_longest_path(graph, start_piece):
    visited = set()
    queue = deque([start_piece])
    sorted_puzzle = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            sorted_puzzle.append(current)
            visited.add(current)
            # Sort neighbors by the number of connections to prioritize most connected pieces
            neighbors = sorted(graph[current], key=lambda x: len(graph[x]), reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return sorted_puzzle

# Build the graph
graph = build_graph(numbers)

# Find a starting piece (a piece with only one connection, if exists)
start_piece = None
for piece, connections in graph.items():
    if len(connections) == 1:
        start_piece = piece
        break
if not start_piece:
    # If no single-connection piece, take any as start
    start_piece = numbers[0]

# Find the longest path using the improved graph-based approach
longest_path = find_longest_path(graph, start_piece)

len(longest_path), longest_path
