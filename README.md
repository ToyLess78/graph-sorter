# Graph Sorter (Python)

This project implements a graph-based sorting algorithm to find the longest sequence of 6-digit numbers, where each number starts with the last two digits of the previous number. The script also measures execution time, CPU usage, and memory consumption during its execution.

---

## Features

- **Graph-based sorting**: Builds a graph to find the longest valid sequence.
- **Validation**: Ensures input file format and sequence validity.
- **Performance metrics**: Measures execution time, CPU time, and memory usage.
- **Output**: Saves the sorted sequence and final merged string to a file.

---

## Requirements

- Python 3.7+
- Required Python package: `psutil`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ToyLess78/graph-sorter-py.git
   cd graph-sorter
   ```
   
2. Install dependencies:
```bash
pip install psutil
````
## Usage
1. Place your input file (e.g., source.txt) in the project directory.

2. Run the script:

```bash
python graph_sorter.py
````
## Input File Format
The input file (source.txt) must contain 6-digit numbers, one per line.
Example:
   ```bash
   123456
   564738
   384950
```
## Output:

- The script validates the input file and calculates the longest valid sequence.
- Outputs the sorted sequence to sortedlist.txt.
- Displays performance metrics in the console:
  - Execution time 
  - CPU time used 
  - Memory used

## Troubleshooting
1. Missing psutil: If you encounter the error ModuleNotFoundError: No module named 'psutil', install the library:

```bash
pip install psutil
```

2. File Not Found: Ensure that the input file (source.txt) is in the same directory as the script and has the correct format.

## Performance Metrics
- Execution Time: Total time to process the file and compute the sequence.
- CPU Time: Time spent on CPU operations (user + system time).
- Memory Usage: Difference in memory usage before and after execution.


## Author
Bilenko Tetiana