from collections import deque

TOTAL_M = 3
TOTAL_C = 3

def is_valid(state):
    M_left, C_left, _ = state
    M_right = TOTAL_M - M_left
    C_right = TOTAL_C - C_left

    if not (0 <= M_left <= TOTAL_M and 0 <= C_left <= TOTAL_C):
        return False

    if M_left > 0 and M_left < C_left:
        return False
    if M_right > 0 and M_right < C_right:
        return False

    return True


def get_successors(state):
    M_left, C_left, boat = state
    successors = []

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m, c in moves:
        if boat == 0:  # left -> right
            new_state = (M_left - m, C_left - c, 1)
        else:          # right -> left
            new_state = (M_left + m, C_left + c, 0)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for succ in get_successors(state):
            queue.append((succ, path + [succ]))

    return None


def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for succ in get_successors(state):
            stack.append((succ, path + [succ]))

    return None


def depth_limited_dfs(start, goal, limit):
    stack = [(start, [start], 0)]

    while stack:
        state, path, depth = stack.pop()

        if state == goal:
            return path

        if depth < limit:
            for succ in get_successors(state):
                if succ not in path:  # avoid immediate cycles
                    stack.append((succ, path + [succ], depth + 1))

    return None


def iterative_deepening_dfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_dfs(start, goal, depth)
        if result is not None:
            return result
    return None


# -------------------- MAIN --------------------

print("Choose search method:")
print("1 - BFS")
print("2 - DFS")
print("3 - Depth-Limited DFS")
print("4 - Iterative Deepening DFS")

choice = input("Enter choice (1/2/3/4): ").strip()

start_state = (3, 3, 0)
goal_state = (0, 0, 1)

solution = None

if choice == "1":
    solution = bfs(start_state, goal_state)

elif choice == "2":
    solution = dfs(start_state, goal_state)

elif choice == "3":
    limit = int(input("Enter depth limit: "))
    solution = depth_limited_dfs(start_state, goal_state, limit)

elif choice == "4":
    max_depth = int(input("Enter maximum depth: "))
    solution = iterative_deepening_dfs(start_state, goal_state, max_depth)

else:
    print("Invalid choice.")
    exit()

if solution:
    print("\nSolution Path:")
    for s in solution:
        print(s)
else:
    print("\nNo solution found.")