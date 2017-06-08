# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    import sys
    stateSet = []

    stateStack = util.Stack() 
    actionStack = util.Stack()
    startState  = problem.getStartState()
    stateStack.push(startState)
    actionStack.push([])

    while not stateStack.isEmpty():
        popState = stateStack.pop()
        stateSet.append(popState)
        if problem.isGoalState(popState):
            return actionStack.pop()
        else:
            routeHistory = actionStack.pop()
            successorStates = problem.getSuccessors(popState)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if state not in stateSet:
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        stateStack.push(state)
                        actionStack.push(currentRoute)
    print "Unable to find a route"
    sys.exit(1)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    import sys
    from sets import Set
    stateSet = []

    stateQueue = util.Queue()
    actionQueue = util.Queue()
    startState = problem.getStartState()
    stateQueue.push(startState)
    actionQueue.push([])

    while not stateQueue.isEmpty():
        popState = stateQueue.pop()
        stateSet.append(popState)
        if problem.isGoalState(popState):
            return actionQueue.pop()
        else:
            routeHistory = actionQueue.pop()
            successorStates = problem.getSuccessors(popState)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if (state not in stateSet) and (state not in stateQueue.list):
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        stateQueue.push(state)
                        actionQueue.push(currentRoute)
    print "Unable to find a route"
    sys.exit(1)

'''
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    import sys
    from sets import Set
    stateSet = Set([])

    stateQueue = util.Queue()
    actionQueue = util.Queue()
    startState = problem.getStartState()
    stateSet.add(startState)
    stateQueue.push(startState)
    actionQueue.push([])

    while not stateQueue.isEmpty():
        popState = stateQueue.pop()
        if problem.isGoalState(popState):
            return actionQueue.pop()
        else:
            routeHistory = actionQueue.pop()
            successorStates = problem.getSuccessors(popState)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if state not in stateSet:
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        stateQueue.push(state)
                        actionQueue.push(currentRoute)
                        stateSet.add(state)
    print "Unable to find a route"
    sys.exit(1)
'''

'''
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    import sys

    stateSet = []
    stateQueue = util.PriorityQueue()
    actionQueue = util.PriorityQueue()
    costQueue = util.PriorityQueue()

    startState = problem.getStartState()
    stateQueue.push(startState,0)
    actionQueue.push([],0)
    costQueue.push(0,0)

    while not stateQueue.isEmpty():
        popState = stateQueue.pop()
        stateSet.append(popState)
        if problem.isGoalState(popState):
            return actionQueue.pop()
        else:
            costHistory = costQueue.pop()
            routeHistory = actionQueue.pop()
            successorStates = problem.getSuccessors(popState)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if (state not in stateSet):
                        print "adding state",state
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        currentCost = costHistory + cost
                        
                        stateQueue.push(state,currentCost)
                        actionQueue.push(currentRoute,currentCost)
                        costQueue.push(currentCost,currentCost)

    print "Unable to find a route"
    sys.exit(1)
'''

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    import sys

    class Node:
        def __init__(self,state,action,cost):
            self.state = state
            self.action = action
            self.cost = cost



    stateSet = []
    stateQueue = util.PriorityQueue()

    startState = problem.getStartState()
    node = Node(startState,[],0)
    stateQueue.push(node,0)

    while not stateQueue.isEmpty():
        popState = stateQueue.pop()
        if popState.state in stateSet:
            continue
        stateSet.append(popState.state)
        if problem.isGoalState(popState.state):
            return popState.action 
        else:
            costHistory = popState.cost
            routeHistory = popState.action 
            successorStates = problem.getSuccessors(popState.state)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if (state not in stateSet):
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        currentCost = costHistory + cost
                        
                        stateQueue.push(Node(state,currentRoute,currentCost),currentCost)

    print "Unable to find a route"
    sys.exit(1)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    import sys

    stateSet = []
    stateQueue = util.PriorityQueue()
    actionQueue = util.PriorityQueue()
    costQueue = util.PriorityQueue()

    startState = problem.getStartState()
    stateQueue.push(startState,0)
    actionQueue.push([],0)
    costQueue.push(0,0)

    while not stateQueue.isEmpty():
        popState = stateQueue.pop()
        stateSet.append(popState)
        if problem.isGoalState(popState):
            return actionQueue.pop()
        else:
            routeHistory = actionQueue.pop()
            costHistory = costQueue.pop()
            successorStates = problem.getSuccessors(popState)
            if successorStates:
                for (state,action,cost) in successorStates:
                    if state not in stateSet:
                        currentRoute = routeHistory[:]
                        currentRoute.append(action)
                        currentCost = costHistory + cost
                        currentCostHeur = currentCost + heuristic(state,problem)
                        
                        stateQueue.push(state,currentCostHeur)
                        actionQueue.push(currentRoute,currentCostHeur)
                        costQueue.push(currentCost,currentCostHeur)

    print "Unable to find a route"
    sys.exit(1)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
