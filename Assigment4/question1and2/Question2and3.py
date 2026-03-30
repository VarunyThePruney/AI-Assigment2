import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(graph, colors, assignment, nodes, index):
    if index == len(nodes):
        return assignment

    node = nodes[index]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = backtracking(graph, colors, assignment, nodes, index + 1)
            if result:
                return result
            del assignment[node]

    return None

def solve_map(graph, colors):
    nodes = list(graph.keys())
    return backtracking(graph, colors, {}, nodes, 0)

def draw_graph(graph, solution, pos, title):
    G = nx.Graph()

    for node in graph:
        G.add_node(node)

    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    color_map = [solution[node] for node in G.nodes()]

    plt.figure(figsize=(14,10))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=1200,
        font_size=7,
        edge_color="black"
    )

    plt.title(title)
    st.pyplot(plt, use_container_width=True)
    plt.clf()

def main():

    st.title("Map Coloring CSP")

    australia_graph = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }

    australia_pos = {
        "WA": (0,2),
        "NT": (1,2),
        "SA": (1,1),
        "Q": (2,2),
        "NSW": (2,1),
        "V": (2,0),
        "T": (2,-1)
    }

    telangana_graph = {
        "Adilabad": ["Komaram Bheem", "Nirmal"],
        "Komaram Bheem": ["Adilabad", "Mancherial"],
        "Mancherial": ["Komaram Bheem", "Peddapalli"],
        "Nirmal": ["Adilabad", "Nizamabad"],
        "Nizamabad": ["Nirmal", "Kamareddy"],
        "Kamareddy": ["Nizamabad", "Medak"],
        "Medak": ["Kamareddy", "Sangareddy"],
        "Sangareddy": ["Medak", "Vikarabad", "Hyderabad"],
        "Vikarabad": ["Sangareddy", "Rangareddy"],
        "Hyderabad": ["Sangareddy", "Rangareddy", "Medchal"],
        "Medchal": ["Hyderabad", "Yadadri"],
        "Yadadri": ["Medchal", "Nalgonda"],
        "Nalgonda": ["Yadadri", "Suryapet", "Nagarkurnool"],
        "Suryapet": ["Nalgonda", "Khammam"],
        "Khammam": ["Suryapet", "Bhadradri"],
        "Bhadradri": ["Khammam", "Mulugu"],
        "Mulugu": ["Bhadradri", "Warangal"],
        "Warangal": ["Mulugu", "Jangaon"],
        "Jangaon": ["Warangal", "Siddipet"],
        "Siddipet": ["Jangaon", "Karimnagar"],
        "Karimnagar": ["Siddipet", "Peddapalli"],
        "Peddapalli": ["Karimnagar", "Mancherial"],
        "Nagarkurnool": ["Nalgonda", "Wanaparthy"],
        "Wanaparthy": ["Nagarkurnool", "Mahabubnagar"],
        "Mahabubnagar": ["Wanaparthy", "Narayanpet"],
        "Narayanpet": ["Mahabubnagar", "Jogulamba"],
        "Jogulamba": ["Narayanpet"],
        "Rangareddy": ["Hyderabad", "Vikarabad"],
        "Rajanna": ["Karimnagar"],
        "Jagitial": ["Karimnagar"],
        "Hanamkonda": ["Warangal"],
        "Jayashankar": ["Mulugu"],
        "Medchal-Malkajgiri": ["Hyderabad"]
    }

    telangana_pos = {
    "Adilabad": (0,5),
    "Komaram Bheem": (1,5),
    "Mancherial": (2,5),
    "Peddapalli": (3,5),
    "Karimnagar": (3,4),
    "Jagitial": (2,4),
    "Rajanna": (4,4),
    "Nirmal": (0,4),
    "Nizamabad": (1,4),
    "Kamareddy": (2,4.5),
    "Medak": (3,3.5),
    "Sangareddy": (2,3),
    "Vikarabad": (1,3),
    "Rangareddy": (2,2),
    "Hyderabad": (3,2),
    "Medchal": (4,2),
    "Medchal-Malkajgiri": (4,2.2),
    "Yadadri": (5,2),
    "Nalgonda": (5,1),
    "Suryapet": (6,1),
    "Khammam": (7,1),
    "Bhadradri": (8,1),
    "Mulugu": (7,2),
    "Warangal": (6,2),
    "Hanamkonda": (6,2.5),
    "Jayashankar": (8,2),
    "Jangaon": (5,3),
    "Siddipet": (4,3),
    "Nagarkurnool": (5,0),
    "Wanaparthy": (6,0),
    "Mahabubnagar": (7,0),
    "Narayanpet": (8,0),
    "Jogulamba": (9,0)
}

    colors = ["red", "green", "blue"]

    australia_solution = solve_map(australia_graph, colors)
    telangana_solution = solve_map(telangana_graph, colors)

    st.subheader("Australia Map")
    draw_graph(australia_graph, australia_solution, australia_pos, "Australia Map Coloring")

    st.subheader("Telangana Map")
    draw_graph(telangana_graph, telangana_solution, telangana_pos, "Telangana Map Coloring")

if __name__ == "__main__":
    main()