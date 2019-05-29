from collections import deque

def search(m,n,state, goal_state):
    """Breadth-first search"""
    queue = deque()

    current_node = Node(state)
    while not current_node.is_goal(goal_state):
        current_node.expand()
        queue.extendleft(current_node.children)
        current_node = queue.pop()

    output = []
    output.append(current_node.state)
    for parent in current_node.parents():
        output.append(parent.state)
    output.reverse()

    return output
