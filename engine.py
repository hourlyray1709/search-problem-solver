class State: 
    def __init__(self, label, is_goal = False): 
        self.label = label
        self.is_goal = is_goal

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

    def get_actions(self, s: State): 
        return self.map[s]


class SearchProblem: 
    def __init__(self, initial_state: State, state_space: list[State], goal_states: list[State], possible_actions: ActionMap): 
        self.initial_state = initial_state 
        self.state_space = state_space 
        self.goal_states = goal_states 
        self.possible_actions = possible_actions 

    def naive_solver(self): 
        frontier = [] 
        explored = [] 

