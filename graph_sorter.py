from collections import defaultdict, deque

# Build a graph where each piece connects to others
def build_graph(pieces):
    graph = defaultdict(list)
    for i, piece1 in enumerate(pieces):
        for j, piece2 in enumerate(pieces):
            if i != j:  # Avoid self-loops
                if piece1[-2:] == piece2[:2]:  # Match condition: last 2 of piece1 = first 2 of piece2
                    graph[piece1].append(piece2)
    return graph

# Find the longest path in the graph using BFS
def find_longest_path(graph, start_piece):
    queue = deque([(start_piece, [start_piece])])  # Queue stores (current_node, current_path)
    longest_path = []

    while queue:
        current, path = queue.popleft()

        # Update the longest path if the current path is longer
        if len(path) > len(longest_path):
            longest_path = path

        # Sort neighbors by the number of connections to prioritize most connected pieces
        for neighbor in sorted(graph[current], key=lambda x: len(graph[x]), reverse=True):
            if neighbor not in path and current[-2:] == neighbor[:2]:  # Ensure sequence matches
                queue.append((neighbor, path + [neighbor]))

    return longest_path

# Improve the sequence by including remaining elements with strict validation
def improve_with_remaining(pieces, main_sequence):
    # Find remaining pieces
    used = set(main_sequence)
    remaining = set(pieces) - used

    # Integrate remaining pieces into the sequence
    for piece in list(remaining):
        # Add to the end if it matches
        if main_sequence[-1][-2:] == piece[:2]:  # Match at the end
            main_sequence.append(piece)
            remaining.remove(piece)
        # Add to the start if it matches
        elif main_sequence[0][:2] == piece[-2:]:  # Match at the start
            main_sequence.insert(0, piece)
            remaining.remove(piece)

    # Exclude completely isolated pieces (they are not valid to add)
    if remaining:
        print(f"Excluded isolated pieces: {remaining}")

    return main_sequence

# Validate the final sequence
def validate_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i][-2:] != sequence[i + 1][:2]:
            return False, i  # Return False and the index where the error occurs
    return True, -1  # If valid, return True

# Save the sorted sequence to a file
def save_sequence_to_file(sequence, output_file_path):
    with open(output_file_path, 'w') as file:
        for item in sequence:
            file.write(f"{item}\n")
    print(f"Sorted sequence saved to {output_file_path}")

# Load the data from the file
file_path = './source.txt'  # Update with your file path
output_file_path = './sequence.txt'

with open(file_path, 'r') as file:
    numbers = file.read().splitlines()

# Build the graph
graph = build_graph(numbers)

# Determine a valid starting piece
start_piece = None
for piece, connections in graph.items():
    if len(connections) == 1:  # Start from a node with only one connection if possible
        start_piece = piece
        break
if not start_piece:
    start_piece = numbers[0]

# Find the longest path
longest_path = find_longest_path(graph, start_piece)

# Improve the sequence by including remaining elements
final_sequence = improve_with_remaining(numbers, longest_path)

# Validate the final sequence
is_valid, error_index = validate_sequence(final_sequence)

# Print the results
print(f"Total pieces: {len(final_sequence)}")
print(f"Sequence is valid: {is_valid}")
if not is_valid:
    print(f"Error at index {error_index}: {final_sequence[error_index]} -> {final_sequence[error_index + 1]}")
else:
    print("The sequence is fully valid.")

print(f"Final sequence: {final_sequence}")

# Save the final sequence to a file
if is_valid:
    save_sequence_to_file(final_sequence, output_file_path)
else:
    print("The sequence is invalid. Not saving to file.")
