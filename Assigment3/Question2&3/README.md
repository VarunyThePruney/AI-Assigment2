# UGV Path Planning using A* Algorithm (Streamlit Apps)

## Overview

This project contains two Streamlit applications that simulate UGV (Unmanned Ground Vehicle) path planning using the A* (A-Star) algorithm on a grid with obstacles.

Both apps generate a battlefield grid and compute the shortest path from a start position to a goal while avoiding obstacles.

---

## ▶️ How to Run

### App 1: Basic Battlefield Generator + Path Finder

Run:

pip install streamlit numpy matplotlib pillow streamlit-image-coordinates

&&

streamlit run script_name.py

or

python -m streamlit run script_name.py

Steps:

1. Select obstacle density (Low / Medium / High)
2. Enter start coordinates (X, Y)
3. Enter goal coordinates (X, Y)
4. Click "Generate Battlefield & Find Path"

---

### App 2: Interactive UGV Navigation (Advanced)

Install dependency:
pip install streamlit-image-coordinates

Run:
streamlit run your_second_script.py

Steps:

1. Select obstacle density
2. Click "Reset Grid" (optional)
3. Click on the grid to add/remove obstacles
4. Watch the UGV automatically move toward the goal

---

## ⚙️ What These Programs Do

### Common Features

* Use A* Algorithm for shortest path finding
* Work on a 70 × 70 grid
* Support different obstacle densities
* Avoid obstacles while navigating to the goal

---

### App 1 (Basic Version)

* Generates a random battlefield grid
* Takes manual input for start and goal positions
* Displays:

  * Path visualization
  * Path length
  * Number of nodes explored

Best for:

* Understanding A* algorithm performance
* Observing the effect of obstacle density

---

### App 2 (Interactive Version)

* Allows real-time obstacle placement by clicking
* Maintains UGV position across steps (continuous movement)
* Automatically recomputes path after each change
* Shows:

  * Live UGV movement
  * Dynamic path updates
  * Error if no path exists

Best for:

* Interactive simulation
* Real-time path planning
* Visualization of dynamic environments

---

## 🛠 Requirements

* Python 3.x
* Streamlit
* NumPy
* Matplotlib
* Pillow
* heapq (built-in)

Install all dependencies:
pip install streamlit numpy matplotlib pillow streamlit-image-coordinates

---

## ⚠️ Notes

* Grid size is fixed at 70x70 (can be adjustable with the initial global variables)
* Start and goal positions are always kept obstacle-free
* If no valid path exists, the app will notify the user
* App 2 is more advanced and supports interactive obstacle editing


