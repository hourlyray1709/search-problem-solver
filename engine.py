class State: 
    def __init__(self, label, is_goal = False): 
        self.label = label
        self.is_goal = is_goal
        self.paths_to_start = []

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
                self.map[action.source].add(action) 
            else: 
                self.map[action.source] = {action} 

    def get_actions(self, s: State) -> set[Action]: 
        return self.map[s]

class Path: 
    def __init__(self, start_state: State): 
        self.start_state = start_state
        self.path_list = [start_state]
        self.action_list = [] 
        
    def add(self, state: State): 
        self.path_list.append(state) 

    def clone(self): 
        newPath = Path(self.start_state) 
        newPath.path_list = [i for i in self.path_list]
        newPath.action_list = [i for i in self.action_list]
        return newPath 

    def show(self): 
        labels = [i.label for i in self.path_list]
        print(labels)


class SearchProblem: 
    def __init__(self, initial_state: State, state_space: list[State], goal_states: list[State], possible_actions: ActionMap): 
        self.initial_state = initial_state 
        self.state_space = state_space 
        self.goal_states = goal_states 
        self.possible_actions = possible_actions 

    def naive_solver(self): 
        # naive approach pseudocode 
        # add the start state to the frontier 
        # add the start state to its path_to_start list 
        # while the frontier is not empty, 
            # remove the first item from the frontier 
            # mark it as explored 
            # for each neighbour, 
                # if it is not explored, 
                    # add it to the frontier 
                    # for each possible path in the current node's paths_to_start list, 
                        # make a copy of this path 
                        # add the neighbour to this path 
                        # find the action responsible for this connection
                        # add it to the path 
                        # add the path to the neighbour's list 

        # solver set up 
        frontier = [self.initial_state] 
        explored = {i: False for i in self.state_space}
        self.initial_state.paths_to_start = [Path(self.initial_state)]

        while len(frontier) > 0: 
            # set up 
            current = frontier.pop(0) 
            print(f"naive_solver: currently evaluating node {current.label}")
            explored[current] = True 

            # find neighbours 
            possible_actions = self.possible_actions.get_actions(current) 
            neighbours = [action.dest for action in possible_actions]
            print(f"naive_solver: found neighbours {[state.label for state in neighbours]}")

            for neighbour in neighbours: 
