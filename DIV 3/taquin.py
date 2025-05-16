# ce travail est élaboré par Med Taher Ben Slama et Helmi BenFraj TD 2 TP 1 
# importation
import heapq
import math
import time

def rbfs(state, goal, f_limit, h_func):
    def recursive_best_first_search(state, f_limit):
        if is_goal_state(state, goal):
            return state, 0
        neighbors = generate_neighbors_states(state)
        if not neighbors:
            return None, math.inf

        successors = []
        for neighbor in neighbors:
            g = calculate_cost(state, neighbor)
            h = h_func(neighbor, goal)
            f = max(g + h, f_limit)
            successors.append((f, neighbor))

        while True:
            successors.sort()  # Sort based on the cost
            best_f, best_successor = successors[0]
            if best_f > f_limit:
                return None, best_f

            alternative = successors[1][0] if len(successors) > 1 else math.inf
            result, best_f = recursive_best_first_search(best_successor, min(f_limit, alternative))
            successors[0] = (best_f, best_successor)
            if result is not None:
                return result, best_f
    return recursive_best_first_search(state, f_limit=0)

def sma_star(start, goal, max_memory, h_func):
    open_list = [(calculate_cost(start), start)]
    while open_list:
        open_list.sort()
        f, state = open_list.pop(0)
        
        if is_goal_state(state, goal):
            return state
        
        if len(open_list) > max_memory:
            open_list.pop()  
            
        neighbors = generate_neighbors_states(state)
        for neighbor in neighbors:
            f = calculate_cost(start) + h_func(neighbor, goal)
            open_list.append((f, neighbor))

    
def ida_star(start, goal, h_func):
    bound = h_func(start, goal)
    
    while True:
        t = search(start, goal, 0, bound, h_func)
        if t == "FOUND":
            return start
        if t == math.inf:
            return None
        bound = t

def search(state, goal, g, bound, h_func):
    f = g + h_func(state, goal)
    if f > bound:
        return f
    if is_goal_state(state, goal):
        return "FOUND"
    
    min_cost = math.inf
    for neighbor in generate_neighbors_states(state):
        t = search(neighbor, goal, g + calculate_cost(state, neighbor), bound, h_func)
        if t == "FOUND":
            return "FOUND"
        if t < min_cost:
            min_cost = t
    return min_cost

def wait_for_start():
    print("Hello, the game is starting now. Please press Enter to start...")
    input()

def print_matrix(matrix):
    print("\nCurrent State:")
    for row in matrix:
        print(" | ".join(f"{tile:>2}" for tile in row))
        print("-" * (len(matrix[0]) * 5 - 1))

def empty_space_position(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == "#":
                return (i, j)

def generate_neighbors_states(state):
    empty_pos = empty_space_position(state)
    if empty_pos is None:
        return []

    i, j = empty_pos
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < len(state) and 0 <= new_j < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(new_state)

    return neighbors

def is_goal_state(state, goal_state):
    return state == goal_state

# el zouz grids
goal = [["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", "#"]]
start = [["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "#", "15"]]

#  choisir l algo
def choose_algorithm():
    print("Choose an algorithm:")
    print("1. Recursive Best First Search (RBFS)")
    print("2. Simplified Memory-Bounded A* (SMA*)")
    print("3. Iterative Deepening A* (IDA*)")
    
    choice = input("Enter the number of the algorithm you want to use: ")
    if choice == "1":
        return rbfs
    elif choice == "2":
        return sma_star
    elif choice == "3":
        return ida_star
    else:
        print("Invalid choice. Defaulting to IDA*.")
        return ida_star

# al3b
wait_for_start()
print("Game started!")

player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")
current_player = player1

# timer 
algorithm = choose_algorithm()
start_time = time.time()

current_state = start
while True:
    print_matrix(current_state)
    neighbors = generate_neighbors_states(current_state)

    if not neighbors:
        print("No valid moves left. The game is a draw!")
        break

    print(f"{current_player}, you have the following options:")
    for idx, neighbor in enumerate(neighbors):
        print(f"Move {idx + 1}:")
        print_matrix(neighbor)

    move_choice = int(input(f"Choose your move (1-{len(neighbors)}): ")) - 1
    if 0 <= move_choice < len(neighbors):
        current_state = neighbors[move_choice]
    else:
        print("Invalid move! Please try again.")
        continue

    if is_goal_state(current_state, goal):
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Player {current_player} has won!!!")
        print(f"Time taken: {time_taken:.2f} seconds")
        break

    current_player = player2 if current_player == player1 else player1
