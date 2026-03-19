import streamlit as st
import numpy as np
import heapq
import matplotlib.pyplot as plt
import time
import io
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

GRID_SIZE = 70
START = (0, 0)
GOAL = (69, 69)
IMG_PX = 600 

DENSITY_MAP = {"Low": 0.1, "Medium": 0.25, "High": 0.4}

def create_grid(density):
    grid = (np.random.rand(GRID_SIZE, GRID_SIZE) < density).astype(int)
    grid[START] = 0
    grid[GOAL] = 0
    return grid

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {start: 0}
    while open_set:
        _, cur = heapq.heappop(open_set)
        if cur == goal:
            break
        r, c = cur
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nb = (r+dr, c+dc)
            if 0 <= nb[0] < GRID_SIZE and 0 <= nb[1] < GRID_SIZE and grid[nb] == 0:
                ng = g[cur] + 1
                if ng < g.get(nb, float('inf')):
                    g[nb] = ng
                    heapq.heappush(open_set, (ng + abs(nb[0]-goal[0]) + abs(nb[1]-goal[1]), nb))
                    came_from[nb] = cur
    path, node = [], goal
    while node in came_from:
        path.append(node)
        node = came_from[node]
    return list(reversed(path)) if path else []

def render(grid, path, ugv):
    dpi = 100
    size = IMG_PX / dpi  

    fig = plt.figure(figsize=(size, size), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])

    ax.imshow(grid, cmap="gray_r", vmin=0, vmax=1,
              extent=[0, GRID_SIZE, GRID_SIZE, 0],  
              interpolation="nearest")

    if path:
        ax.plot([p[1]+0.5 for p in path], [p[0]+0.5 for p in path],
                color="dodgerblue", lw=1.5)

    ax.scatter(ugv[1]+0.5,  ugv[0]+0.5,  color="green", s=60, zorder=3)
    ax.scatter(GOAL[1]+0.5, GOAL[0]+0.5, color="red",   s=60, zorder=3)

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(GRID_SIZE, 0)
    ax.axis("off")

    buf = io.BytesIO()
    fig.savefig(buf, format="PNG", dpi=dpi, pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).copy()

def click_to_cell(click, img):
    """Convert a pixel click to a (row, col) grid cell."""
    col = int(click["x"] / img.width  * GRID_SIZE)
    row = int(click["y"] / img.height * GRID_SIZE)
    return row, col

def main():
    density = DENSITY_MAP[st.selectbox("Obstacle Density", list(DENSITY_MAP))]

    if "grid" not in st.session_state or st.button("Reset Grid"):
        st.session_state.grid = create_grid(density)
        st.session_state.ugv = START
        st.session_state.last_click = None

    path = astar(st.session_state.grid, st.session_state.ugv, GOAL)
    img  = render(st.session_state.grid, path, st.session_state.ugv)

    st.title("UGV Navigation")
    st.caption("Click the grid to toggle obstacles.")

    click = streamlit_image_coordinates(img, key="grid_canvas")

    if isinstance(click, dict):
        row, col = click_to_cell(click, img)
        cell = (row, col)
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            if cell not in (st.session_state.ugv, GOAL) and cell != st.session_state.last_click:
                st.session_state.grid[cell] ^= 1
                st.session_state.last_click = cell
                st.rerun()

    if path:
        st.write(f"Path length: **{len(path)}** steps")
        time.sleep(1)
        st.session_state.ugv = path[0]
        if st.session_state.ugv == GOAL:
            st.success("Goal reached!")
            st.session_state.ugv = START
        st.rerun()
    else:
        st.error("No path found, remove some obstacles.")

    st.caption(f"UGV: {st.session_state.ugv}  |  Goal: {GOAL}")
    
if __name__ == "__main__":
    main()