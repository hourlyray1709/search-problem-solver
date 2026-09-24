from engine import * 

class TestSuite: 
    def __init__(self): 
        self.cases = [
            getattr(self, attr) for attr in dir(self) if callable(getattr(self, attr)) and attr.startswith("testcase")
        ]

    def run(self): 
        for case in self.cases: 
            try: 
                case() 
            except Exception as e: 
                print(e)

    def testcase_make_actions(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State(str(i))
            state_space.append(_state)

        # make actions 
        actions = [] 
        for i in range(6): 
            _action = Action(state_space[i], state_space[(i+1) % 6], 1)
            actions.append(_action) 

        action_map = ActionMap(actions) 

        # assertion 
        for state in state_space: 
            if len(action_map.get_actions(state)) != 1: 
                print(f"testcase_make_actions: [DEBUG]: {action_map}")
                raise Exception("testcase_make_actions: Failed - More actions than expected")
        print("testcase_make_actions: OK")

    def testcase_basic_paths(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State(str(i))
            state_space.append(_state)

        path1 = Path(state_space[0])
        path1.add(state_space[5])
        path1.add(state_space[3]) 

        # assert length is equal to 3 
        if len(path1.path_list) != 3: 
            print(f"testcase_basic_paths: [DEBUG]: {path1.path_list}")
            raise Exception("testcase_basic_paths: Failed - Wrong numbr of nodes in path")
        print("testcase_basic_paths: OK")

    def testcase_clone_paths(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State(str(i))
            state_space.append(_state)

        path1 = Path(state_space[0])
        path2 = path1.clone() 
        path2.add(state_space[5])

        # assert path 1 has length 1 and path 2 has length 2 
        if len(path1.path_list) != 1 or len(path2.path_list) != 2: 
            print(f"testcase_clone_paths: [DEBUG]: {path1.path_list}")
            print(f"testcase_clone_paths: [DEBUG]: {path2.path_list}")
            raise Exception("testcase_clone_paths: Failed - Wrong number of nodes in path")
        print("testcase_clone_paths: OK")

    def testcase_simple_solution(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State(str(i))
            state_space.append(_state)

        # make actions 
        actions = [] 
        for i in range(6): 
            _action = Action(state_space[i], state_space[(i+1) % 6], 1)
            actions.append(_action) 

        action_map = ActionMap(actions) 

        # initiate design under test 
        solver = SearchProblem(state_space[0], state_space, [state_space[5]], action_map)
        solution = solver.naive_solver()

        # assertion
        if solution != [str(i) for i in range(6)]: 
            raise Exception("testcase_simple_solution: Failed - wrong solution")
        print("testcase_simple_solution: OK")

    def testcase_harder_solution(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State(str(i))
            state_space.append(_state)

        # make actions 
        actions = [] 
        for i in range(6): 
            _action = Action(state_space[i], state_space[(i+1) % 6], 1)
            actions.append(_action) 

        _action = Action(state_space[0], state_space[5], 1)
        actions.append(_action)
        _action = Action(state_space[3], state_space[4], 1)
        actions.append(_action)
        _action = Action(state_space[1], state_space[5], 1)
        actions.append(_action)


        action_map = ActionMap(actions) 

        # initiate design under test 
        solver = SearchProblem(state_space[0], state_space, [state_space[5]], action_map)
        path = solver.naive_solver()

        # assertion 
        if path != ["0", "5"]: 
            raise Exception(f"testcase_harder_solution: Failed - incorrect solution, got {path} expected ['0', '5']")
        print("testcase_harder_solution: OK")

a = TestSuite() 
a.run() 