# search-problem-solver
A general search problem can be defined as the following: 
- The state space: A set of states that you can go to (in this repo we only allow finite state space)
- The goal state: Where you want to be
- Actions(s): given state s, this returns the set of possible actions we can take.
- Transition model: Given state s and action a, return a state s' that we reach via this action.
- Cost function: Given s and action a, return the cost of applying this action.

This repo takes in a general search problem (with some limitations) and tries to solve it. 
