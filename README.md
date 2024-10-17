# Kosaraju's Algorithm for Strongly Connected Components (SCC)

This project implements **Kosaraju's Algorithm** to find the strongly connected components of a directed graph. The algorithm efficiently computes the SCCs using two depth-first searches on the graph and its transpose.

## Algorithm Steps

1. **First Pass (DFS on Transposed Graph)**: 
   - Process all nodes in reverse order to assign "finishing times."

2. **Second Pass (DFS on Original Graph)**:
   - Process nodes in decreasing order of finishing times to discover SCCs.

## Files

- **kosaraju_scc.py**: The main Python file implementing the Kosaraju SCC algorithm.
- **input.txt**: Input file containing the directed graph, with each line representing an edge (tail and head).

### Large File Notice: `input.txt`

The file `input.txt` is tracked using **Git Large File Storage (LFS)** due to its large size. As a result, it cannot be displayed directly in the GitHub web interface.

- **To view or download the file**:
  - You can **download it locally** by clicking the **"View raw"** link on the file in the GitHub repository.
  - Alternatively, if you have **Git LFS** installed, you can clone the repository and Git LFS will automatically download the file:
    ```bash
    git lfs install
    git clone https://github.com/ArnavSingh314/kosaraju-scc-algorithm.git
    ```

## Input Format

- Each line in the `input.txt` file represents an edge in the graph.
  ```text
  tail_node head_node
