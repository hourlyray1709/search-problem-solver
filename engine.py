class State: 
    def __init__(self, label, is_goal = False): 
        self.label = label
        self.is_goal = is_goal
        self.paths_to_start: list["Path"] = []

class Action: 
    def __init__(self, s: State, d: State, c: int | float): 
        self.source = s 
        self.dest = d 
        self.cost = c 

class ActionMap: 
    def __init__(self, AllActions: list[Action]): 
        # map is a dictionary holding key value pairs of (state , set[Action]) 
        self.map = {} 
        for action in AllActions: 
            if action.source in self.map.keys(): 
                if action not in self.map[action.source]: 
                    self.map[action.source].append(action) 
            else: 
                self.map[action.source] = [action]

    def get_actions(self, s: State) -> list[Action]: 
        return self.map[s]

class Path: 
    def __init__(self, start_state: State): 
        self.start_state = start_state
        self.path_list = [start_state]
        self.action_list = [] 
        
    def add(self, state: State, action: Action = None): 
        self.path_list.append(state) 

        if action: 
            self.action_list.append(action)

    def clone(self): 
        newPath = Path(self.start_state) 
        newPath.path_list = [i for i in self.path_list]
        newPath.action_list = [i for i in self.action_list]
        return newPath 

    def get(self): 
        labels = [i.label for i in self.path_list]
        return labels

    def get_cost(self): 
        return sum([action.cost for action in self.action_list])

class SearchProblem: 
    def __init__(self, initial_state: State, state_space: list[State], goal_states: list[State], possible_actions: ActionMap): 
        self.initial_state = initial_state 
        self.state_space = state_space 
        self.goal_states = goal_states 
        self.possible_actions = possible_actions 

    def naive_solver(self, suppress_log=True): 
        # solver set up 
        frontier = [self.initial_state] 
        explored = {i: False for i in self.state_space}
        self.initial_state.paths_to_start = [Path(self.initial_state)]

        while len(frontier) > 0: 
            # set up 
            current = frontier.pop(0) 
            if not suppress_log:
                print(f"naive_solver: currently evaluating node {current.label}")
            explored[current] = True 

            # find neighbours 
            possible_actions = self.possible_actions.get_actions(current) 
            neighbours = [action.dest for action in possible_actions]

            if not suppress_log:
                print(f"naive_solver: found neighbours {[state.label for state in neighbours]}")

            for neighbour_idx in range(len(neighbours)): 
                neighbour = neighbours[neighbour_idx]
                action = possible_actions[neighbour_idx]
                if not explored[neighbour]: 
                    frontier.append(neighbour)
                    for path in current.paths_to_start: 
                        _path = path.clone() 
                        _path.add(neighbour, action)
                        neighbour.paths_to_start.append(_path)

        if not suppress_log:
            print("naive_solver: Finished main loop")

        # find best path 
        paths = []
        min_cost = None 
        best_path = None 
        for state in self.goal_states: 
            for path in state.paths_to_start: 
                if not suppress_log:
                    print(f"naive_solver: possible path: {path.get()}")
                cost = path.get_cost()

                if min_cost == None: 
                    min_cost = cost 
                    best_path = path 
                elif cost < min_cost: 
                    min_cost = cost 
                    best_path = path 

                paths.append(path) 
        if not suppress_log:
            print(f"naive_solver: best path: {best_path.get()} cost: {min_cost}")
        return best_path.get() 

        

        
