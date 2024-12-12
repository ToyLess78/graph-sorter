import os
import time
import psutil  # To get information about CPU usage
from collections import defaultdict, deque


# Validate the input file
def validate_file(file_path):
    if not file_path.endswith('.txt'):
        raise ValueError("Invalid file format. The file must be a .txt file.")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        if not line.isdigit() or len(line) != 6:
            raise ValueError(f"Invalid line in file: '{line}'. Each line must be a 6-digit number.")
    print("File validation successful.")
    return lines


# Build a graph where each piece connects to others
def build_graph(pieces):
    graph = defaultdict(list)
    for i, piece1 in enumerate(pieces):
        for j, piece2 in enumerate(pieces):
            if i != j and piece1[-2:] == piece2[:2]:
                graph[piece1].append(piece2)
    return graph


# Find the longest path in the graph using BFS
def find_longest_path(graph, start_piece):
    queue = deque([(start_piece, [start_piece])])
    longest_path = []

    while queue:
        current, path = queue.popleft()
        if len(path) > len(longest_path):
            longest_path = path
        for neighbor in sorted(graph[current], key=lambda x: (len(graph[x]), x), reverse=True):
            if neighbor not in path and current[-2:] == neighbor[:2]:
                queue.append((neighbor, path + [neighbor]))

    return longest_path


# Improve the sequence by including remaining elements with strict validation
def improve_with_remaining(pieces, main_sequence):
    used = set(main_sequence)
    remaining = sorted(set(pieces) - used)

    for piece in list(remaining):
        if main_sequence[-1][-2:] == piece[:2]:
            main_sequence.append(piece)
            remaining.remove(piece)
        elif main_sequence[0][:2] == piece[-2:]:
            main_sequence.insert(0, piece)
            remaining.remove(piece)

    return main_sequence


# Validate the final sequence
def validate_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i][-2:] != sequence[i + 1][:2]:
            return False, i
    return True, -1


# Merge the sequence into a single number string
def merge_sequence(sequence):
    if not sequence:
        return ""
    merged = sequence[0]
    for i in range(1, len(sequence)):
        merged += sequence[i][2:]
    return merged


# Save the sorted sequence to a file
def save_sequence_to_file(sequence, output_file_path):
    with open(output_file_path, 'w') as file:
        for item in sequence:
            file.write(f"{item}\n")
    print(f"Sorted sequence saved to {output_file_path}")


# File paths
file_path = './source.txt'
output_file_path = './sortedlist.txt'

try:
    start_time = time.time()  # Start time
    process = psutil.Process(os.getpid())  # Get current process

    cpu_before = process.cpu_times()  # CPU times before execution
    memory_before = process.memory_info().rss / (1024 ** 2)  # Memory in MB before execution

    numbers = validate_file(file_path)

    graph = build_graph(numbers)

    start_piece = min((piece for piece, connections in graph.items() if len(connections) == 1), default=numbers[0])

    longest_path = find_longest_path(graph, start_piece)

    final_sequence = improve_with_remaining(numbers, longest_path)

    is_valid, error_index = validate_sequence(final_sequence)

    merged_sequence = merge_sequence(final_sequence)

    cpu_after = process.cpu_times()  # CPU times after execution
    memory_after = process.memory_info().rss / (1024 ** 2)  # Memory in MB after execution
    end_time = time.time()  # End time

    # CPU time calculations
    user_cpu_time = cpu_after.user - cpu_before.user
    system_cpu_time = cpu_after.system - cpu_before.system
    total_cpu_time = user_cpu_time + system_cpu_time

    # Print results
    print(f"Total pieces: {len(final_sequence)}")
    print(f"Sequence is valid: {is_valid}")
    if not is_valid:
        print(f"Error at index {error_index}: {final_sequence[error_index]} -> {final_sequence[error_index + 1]}")
    else:
        print("The sequence is fully valid.")
    print(f"Final sequence: {merged_sequence}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print(f"CPU time used: {total_cpu_time:.2f} seconds")
    print(f"Memory used: {memory_after - memory_before:.2f} MB")

    # Save the final sequence to a file
    if is_valid:
        save_sequence_to_file(final_sequence, output_file_path)
    else:
        print("The sequence is invalid. Not saving to file.")

except (ValueError, FileNotFoundError) as e:
    print(e)
