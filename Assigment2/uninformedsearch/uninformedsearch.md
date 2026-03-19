# Uninformed Search – BFS, DFS and Variants

## 1. Problem Overview

The Missionaries and Cannibals problem is modeled as a state-space search problem.

State: (M_left, C_left, Boat)

* M_left → Missionaries on left bank
* C_left → Cannibals on left bank
* Boat → 0 (left), 1 (right)

Start: (3,3,0)
Goal: (0,0,1)

Valid states ensure missionaries are never outnumbered by cannibals on either bank.

---

# 2. High-Level Architecture

The system follows a modular state-space search architecture:

1. State Representation

   * Encodes problem as tuples
   * Defines start and goal states

2. Validity Checker (is_valid)

   * Ensures constraints are satisfied
   * Prevents illegal states

3. Successor Function (get_successors)

   * Generates possible moves
   * Filters them using validity rules

4. Search Strategy Module

   * Implements BFS, DFS, Depth-Limited DFS, and Iterative Deepening DFS

5. Path Tracking

   * Maintains sequence of states
   * Returns full solution when goal is found

---

# 3. Breadth-First Search (BFS)

* Uses a Queue (FIFO)
* Explores level by level
* Finds shortest solution

Properties:

* Complete: Yes
* Optimal: Yes
* Time & Space: O(b^d)

BFS guarantees the minimum number of boat moves but uses more memory.

---

# 4. Depth-First Search (DFS)

* Uses a Stack (LIFO)
* Explores deepest nodes first
* Backtracks on dead ends

Properties:

* Complete: Not always
* Optimal: No
* Time: O(b^m)
* Space: O(bm)

DFS uses less memory but may not find the shortest solution.

---

# 5. Depth-Limited DFS (DLS)

* DFS with a fixed depth limit
* Prevents infinite exploration

Complete only if limit ≥ solution depth.

---

# 6. Iterative Deepening DFS (IDDFS)

* Repeatedly applies DLS with increasing depth
* Combines BFS optimality with DFS memory efficiency

Properties:

* Complete: Yes
* Optimal: Yes
* Time: O(b^d)
* Space: O(bd)

---

# 7. Performance Comparison

| Algorithm | Complete    | Optimal | Memory Usage |
| --------- | ----------- | ------- | ------------ |
| BFS       | Yes         | Yes     | High         |
| DFS       | No          | No      | Low          |
| DLS       | Conditional | No      | Low          |
| IDDFS     | Yes         | Yes     | Medium       |
