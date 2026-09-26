from engine import * 
import random 

class Generator: 
    def __init__(self, cost_min=1, cost_max=50): 
        self.cost_min = cost_min 
        self.cost_max = cost_max

    def get_graph(self, n, min_additional_factor=1, max_additional_factor=5) -> SearchProblem:
        # this generates a main path from 0->1->...->n before adding random paths between nodes 
        # the main path is not necessarily the best path. 

        state_space = [State(str(i)) for i in range(n)]
        start_state = state_space[0]
        goal_state = state_space[n-1]
        action_list = [] 

        # core path generation
        for i in range(n-1): 
            action = Action(state_space[i], state_space[i+1], random.randint(self.cost_min, self.cost_max))
            action_list.append(action)

        # sub path generation 
        connections = {i:[i+1] if i < n-1 else [] for i in range(n) } 
        path_count = int(n * random.uniform(min_additional_factor, max_additional_factor))

        # in a k complete graph we can only have 0.5 n (n-1) edges in total and we used up n-1 edges in the core path 
        path_limit = int((0.5 * n * (n-1)) - (n-1))
        if path_count > path_limit: 
            path_count = path_limit 

        for i in range(path_count): 
            source = random.randint(0, n-1) 
            dest = random.randint(0, n-1)

            if source == dest: 
                continue 

            if dest in connections[source]: 
                continue 

            connections[source].append(dest)
            s = state_space[source]
            d = state_space[dest]


            action = Action(s, d, random.randint(self.cost_min, self.cost_max))
            action_list.append(action) 

        action_map = ActionMap(action_list)
        problem = SearchProblem(start_state, state_space, [goal_state], action_map)

        return problem 



