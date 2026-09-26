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
        return self.map.get(s, [])

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
        # preconditions 
        if self.initial_state == None: 
            return [""]

        # solver set up 
        frontier = [Path(self.initial_state)]
        solutions: list[Path] = [] 
        

        while len(frontier) > 0: 
            current_path = frontier.pop(0) 
            current_node = current_path.path_list[-1] 

            actions = self.possible_actions.get_actions(current_node) 
            for action in actions: 
                neighbour = action.dest 

                if neighbour not in current_path.path_list: 
                    _path = current_path.clone()
                    _path.add(neighbour, action) 

                    if neighbour in self.goal_states: 
                        solutions.append(_path) 

                    frontier.append(_path) 
        min_cost = None 
        best_path = None 
        for path in solutions: 
            if not suppress_log:
                print(path.get(),"cost:", path.get_cost())

            cost = path.get_cost()

            if min_cost == None: 
                min_cost = cost 
                best_path = path 
            elif cost < min_cost: 
                min_cost = cost 
                best_path = path 

        return best_path.get()
            



        

        
