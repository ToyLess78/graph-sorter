# Reload numbers from the newly uploaded file
file_path = './source.txt'

# Read the file and load numbers
with open(file_path, 'r') as file:
    numbers = file.read().splitlines()

# Improved graph-based approach
from collections import defaultdict

# Build a graph where each piece connects to others
def build_graph(pieces):
    graph = defaultdict(list)
    for piece1 in pieces:
        for piece2 in pieces:
            if piece1 != piece2:  # Avoid self-loops
                if piece1[-2:] == piece2[:2]:  # Match condition: last 2 chars of one = first 2 chars of another
                    graph[piece1].append(piece2)
    return graph

# DFS with memoization to find the longest path
def dfs(graph, current, visited, memo):
    if current in memo:
        return memo[current]

    max_path = []
    for neighbor in graph[current]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, visited | {neighbor}, memo)
            if len(path) > len(max_path):
                max_path = path

    result = [current] + max_path
    memo[current] = result
    return result

# Build the graph
graph = build_graph(numbers)

# Try DFS from each piece to ensure the best starting point
longest_path = []
memo = {}
for piece in numbers:
    path = dfs(graph, piece, {piece}, memo)
    if len(path) > len(longest_path):
        longest_path = path

# Output the results
print(f"Length of the longest path: {len(longest_path)}")
print(f"Longest path: {longest_path}")
