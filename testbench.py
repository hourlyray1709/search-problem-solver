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
            except: 
                pass 

    def testcase_make_actions(self): 
        # make states
        state_space = []   
        for i in range(6): 
            _state = State("i")
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


a = TestSuite() 
a.run() 