import copy
import sys

sys.setrecursionlimit(10**6)

# ******** Operators
# ******** Τελεστές


def go_to_floor1(state):
    if state[-1]<8 and state[1]>0:
        if state[1]>10-state[-1]:
            new_state = [1] + [state[1] + state[-1] - 10] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[-1]]
        return new_state
    else:
        return None
    
def go_to_floor2(state):
    if state[-1]<8 and state[2]>0:
        if state[2]>10-state[-1]:
            new_state = [2] + [state[1]] + [state[2] + state[-1] - 10] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2] + [state[1]] + [0] + [state[3]] + [state[4]] + [state[2] + state[-1]]
        return new_state
    else:
        return None

def go_to_floor3(state):
    if state[-1]<8 and state[3]>0:
        if state[3]>10-state[-1]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3] + state[-1] - 10] + [state[4]] + [8]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[3] + state[-1]]
        return new_state
    else:
        return None

def go_to_floor4(state):
    if state[-1]<8 and state[4]>0:
        if state[4]>10-state[-1]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[-1] - 10] + [8]
        else:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[-1]]
        return new_state
    else:
        return None

def go_to_top(state):
    if(state[-1]>=8):
        state[-1]=0
        return state
    


'''
Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης
'''
def find_children(state):
    
    children=[]
    
       
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    
    floor2_state=copy.deepcopy(state)
    floor2_child=go_to_floor2(floor2_state)
    
    floor3_state=copy.deepcopy(state)
    floor3_child=go_to_floor3(floor3_state)
    
    floor4_state=copy.deepcopy(state)
    floor4_child=go_to_floor4(floor4_state)
    
    

    
    if floor1_child!=None: 
        children.append(floor1_child)
    if floor2_child!=None: 
        children.append(floor2_child)
    if floor3_child!=None: 
        children.append(floor3_child)
    if floor4_child!=None: 
        children.append(floor4_child)
        
    return children



""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
** check if front is empty
** Έλεγχος αν το μέτωπο είναι άδειο
"""

def front_is_empty(front):
    return front == []

""" ----------------------------------------------------------------------------
** add node to front
** Προσθήκη κόμβου στο μέτωπο
"""

def add_to_front(front, node):
    front.append(node)
    return front

""" ----------------------------------------------------------------------------
** remove node from front
** Αφαίρεση κόμβου από το μέτωπο
"""

def remove_from_front(front):
    return front.pop(0)

""" ----------------------------------------------------------------------------
**** QUEUE
**** Ουρά
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
** check if queue is empty
** Έλεγχος αν η ουρά είναι άδεια
"""

def queue_is_empty(queue):
    return queue == []

""" ----------------------------------------------------------------------------
** add node to queue
** Προσθήκη κόμβου στην ουρά
"""

def add_to_queue(queue, node):
    queue.append(node)
    return queue

""" ----------------------------------------------------------------------------
** remove node from queue
** Αφαίρεση κόμβου από την ουρά
"""

def remove_from_queue(queue):
    return queue.pop(0)

""" ----------------------------------------------------------------------------
**** SOLUTION
**** Λύση
"""

""" ----------------------------------------------------------------------------
** check if node is a solution
** Έλεγχος αν ο κόμβος είναι λύση
"""

def is_solution(node, goal):
    return node == goal

""" ----------------------------------------------------------------------------    
** find solution
** Εύρεση λύσης
"""

def find_solution(front, queue, path, goal, method):
    while not front_is_empty(front):
        node = remove_from_front(front)
        path.append(node)
        if is_solution(node, goal):
            print('Solution found')
            print(path)
            return
        else:
            children = find_children(node)
            for child in children:
                front = add_to_front(front, child)
            front = expand_front(front, method)
    print('No solution found')

""" ----------------------------------------------------------------------------
**** EXPAND FRONT
**** Επέκταση Μετώπου
"""

""" ----------------------------------------------------------------------------
** expand front
** Επέκταση Μετώπου
"""

def expand_front(front, method):
    if method=='BFS':
        return expand_front_BFS(front)
    elif method=='DFS':
        return expand_front_DFS(front)
    else: "other methods to be added"

""" ----------------------------------------------------------------------------
** expand front for BFS
** Επέκταση Μετώπου για BFS
"""

def expand_front_BFS(front):
    return front

""" ----------------------------------------------------------------------------
** expand front for DFS
** Επέκταση Μετώπου για DFS
"""

def expand_front_DFS(front):
    return front[::-1]

""" ----------------------------------------------------------------------------
**** EXPAND QUEUE
**** Επέκταση Ουράς
"""

""" ----------------------------------------------------------------------------
** expand queue
** Επέκταση Ουράς
"""

def expand_queue(queue, method):
    if method=='BFS':
        return expand_queue_BFS(queue)
    elif method=='DFS':
        return expand_queue_DFS(queue)
    else: "other methods to be added"

""" ----------------------------------------------------------------------------
** expand queue for BFS
** Επέκταση Ουράς για BFS
"""

def expand_queue_BFS(queue):
    return queue

""" ----------------------------------------------------------------------------
** expand queue for DFS
** Επέκταση Ουράς για DFS
"""

def expand_queue_DFS(queue):
    return queue[::-1]

""" ----------------------------------------------------------------------------
**** MAIN
**** Κύριο Πρόγραμμα
"""


def main():
    
    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]
    method=input('Choose search method (BFS, DFS): ')
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method)
    #find_solution(make_front(initial_state), make_queue(initial_state), [], method)
    
    
if __name__ == "__main__":
    main()



