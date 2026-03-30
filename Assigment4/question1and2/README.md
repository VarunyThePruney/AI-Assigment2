# Map Coloring CSP Assignment

## Overview

This project implements the **Map Coloring Problem using Constraint Satisfaction Problem (CSP)** in Python. The goal is to assign colors to regions on a map such that no two adjacent regions share the same color.

Two maps are solved in this assignment:

1. Australia Map (7 states and territories)
2. Telangana Map (33 districts)

The solution uses **backtracking search** to assign colors while satisfying adjacency constraints.

---

## Problem Statement

### Question 1

Implement the Map Coloring problem using CSP for the seven principal states and territories of Australia:

* WA
* NT
* Q
* SA
* NSW
* V
* T

Each state must be assigned a color such that neighboring states do not share the same color.

### Question 2

Apply the Map Coloring CSP to the 33 districts of Telangana and generate a colored map output.

---

## Approach

The solution follows these steps:

1. Represent the map as a graph
2. Each state/district is a node
3. Neighboring regions form edges
4. Define three colors: Red, Green, Blue
5. Use Backtracking CSP to assign colors
6. Check constraints using a safety function
7. Visualize results using Streamlit and NetworkX

---

## Files

```
Question2and3.py
README.md
venv/
```

---

## Requirements

Install dependencies:

```
pip install streamlit matplotlib networkx
```

---

## How to Run

Run Streamlit visualization:

```
streamlit run Question2and3.py
```

or

```
python3 -m streamlit run Question2and3.py
```

---

## Output

### Australia Map

* 7 states colored
* No adjacent states share the same color

### Telangana Map

* 33 districts colored
* CSP constraints satisfied
* Visual map displayed in Streamlit

---

## Algorithm Used

Backtracking CSP

Steps:

1. Select a region
2. Try assigning a color
3. Check if the color is safe
4. Move to next region
5. If conflict occurs, backtrack
6. Continue until all regions are colored

---

## Conclusion

The Map Coloring CSP was successfully implemented for both Australia and Telangana maps.
The backtracking algorithm ensures that all adjacency constraints are satisfied and produces valid color assignments for both maps.

---

## Author

Varun Golakoti
