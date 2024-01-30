import copy
import sys 
sys.setrecursionlimit(10**6) 

""" ----------------------------------------------------------------------------
**** Operators
**** Τελεστές
"""
#Συνάρτηση για τον τελεστή go_to_floor1
def go_to_floor1(state):
    #ελεγχος αν το ασανσερ εχει λιγοτερους απο 8 ένοικους και αν οι ενοίκοι στον πρώτο όροφο είναι μεγαλύτεροι του 0
    if state[-1] < 8 and state[1] > 0:
        #ελεγχος αν οι ενοίκοι στον πρώτο όροφο είναι περισσότεροι των 8 μειον τον αριθμό των ενοίκων στο ασανσερ
        if state[1] > 8 - state[-1]:
            new_state = [1] + [state[1] + state[-1] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[-1]]
        return new_state
    
#Συνάρτηση για τον τελεστή go_to_floor2
def go_to_floor2(state):
      #ελεγχος αν το ασανσερ εχει λιγοτερους απο 8 ένοικους και αν οι ενοίκοι στον δεύτερο όροφο είναι μεγαλύτεροι του 0
      if state[-1] < 8 and state[2] > 0:
        #ελεγχος αν οι ενοίκοι στον δεύτερο όροφο είναι περισσότεροι των 8 μειον τον αριθμό των ενοίκων στο ασανσερ
        if state[2] > 8 - state[-1]:
            new_state = [2] + [state[1]] + [state[2] + state[-1] - 8] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2] + [state[1]] + [0] + [state[3]] + [state[4]] + [state[2] + state[-1]]
        return new_state
      
#Συνάρτηση για τον τελεστή go_to_floor3
def go_to_floor3(state):
    #ελεγχος αν το ασανσερ εχει λιγοτερους απο 8 ένοικους και αν οι ενοίκοι στον τρίτο όροφο είναι μεγαλύτεροι του 0
    if state[-1] < 8 and state[3] > 0:
        #ελεγχος αν οι ενοίκοι στον τρίτο όροφο είναι περισσότεροι των 8 μειον τον αριθμό των ενοίκων στο ασανσερ
        if state[3] > 8 - state[-1]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3] + state[-1] - 8] + [state[4]] + [8]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[3] + state[-1]]
        return new_state

#Συνάρτηση για τον τελεστή go_to_floor4 
def go_to_floor4(state):
    #ελεγχος αν το ασανσερ εχει λιγοτερους απο 8 ένοικους και αν οι ενοίκοι στον τέταρτο όροφο είναι μεγαλύτεροι του 0
    if state[-1] < 8 and state[4] > 0:
        #ελεγχος αν οι ενοίκοι στον τέταρτο όροφο είναι περισσότεροι των 8 μειον τον αριθμό των ενοίκων στο ασανσερ
        if state[4] > 8 - state[-1]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[-1] - 8] + [8]
        else:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[-1]]
        return new_state

#Συνάρτηση για τον τελεστή go_to_top
def go_to_top(state):
    #ελεγχος αν το ασανσερ εχει 8 ένοικους ή αν οι ενοίκοι σε κάθε όροφο ειναι 0
    if state[-1] == 8 or (state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == 0):
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
        return new_state

""" ----------------------------------------------------------------------------
**** Function to find children of current state
**** Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης
"""

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

    top_state=copy.deepcopy(state)
    top_child=go_to_top(top_state)
    
    if top_child != None:
        children.append(top_child)
    if floor4_child != None:
        children.append(floor4_child)
    if floor3_child != None:
        children.append(floor3_child)
    if floor2_child != None:
        children.append(floor2_child)
    if floor1_child != None: 
        children.append(floor1_child)
      
    return children



""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

"""
** Initialization of Front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]
    
"""
**** Expanding Front
**** Επέκταση Μετώπου    
"""

def expand_front(front, method):  

    # Αν το μέτωπο δεν είναι κενό τότε επέκτεινέ το αλλιώς επέστρεψε κενό
    if front:
        print("Front:")
        print(front)
        node=front.pop(0)
        children=find_children(node)
    else:
        return []

    if method=='DFS':        
        for child in children:     
            front.insert(0,child) # Τοποθέτησε τα παιδιά στην αρχή του μετώπου
    
    elif method=='BFS':
        for child in children:     
            front.append(child) # Τοποθέτησε τα παιδιά στο τέλος του μετώπου

    elif method=='BestFS':
        for child in children:     
            front.insert(0,child) # Τοποθέτησε τα παιδιά
        front.sort(key=lambda x: sum(x[1:5])) # Ταξινόμησε το μέτωπο με βάση το άθροισμα των ενοίκων 

    elif method=='HillC':
        best_child=None        # Αρχικοποίηση καλύτερου παιδιού
        best_cost=float('inf') # Αρχικοποίηση κόστους στο άπειρο
        for child in children:
            cost = sum(child[1:5]) # Υπολογισμός του κόστους με βάση το άθροισμα των ενοίκων του παιδιού
            if cost < best_cost:   # Αν το κόστος του τρέχοντος παιδιού είναι καλύτερο από του καλύτερου μέχρι στιγμής
                best_child = child
                best_cost = cost
            if best_child:
                front.insert(0, best_child) # Τοποθέτησε το καλύτερο παιδί στην αρχή του μετώπου (άρα κρατιέται το παιδί με το καλύτερο κόστος, τα άλλα κλαδεύονται)        
    
    return front


""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση Ουράς
"""

""" 
** Ιnitialization of queue
** Αρχικοποίηση Ουράς
"""

def make_queue(state):
    return [[state]]

""" 
**** Εxpanding Queue
**** Επέκταση Ουράς
"""

def extend_queue(queue, method):

    print("Queue:")
    # Εμφάνιση κάθε μονοπατιού του μετώπου
    for path in queue:
        print(path)
    node=queue.pop(0)
    queue_copy=copy.deepcopy(queue)
    children=find_children(node[-1])
    
    if method=='DFS':    
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)        # Πρόσθεσε το παιδί στο μονοπάτι
            queue_copy.insert(0,path) # Τοποθέτησε το μονοπάτι στην αρχή του μετώπου  

    elif method=='BFS':
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)      # Πρόσθεσε το παιδί στο μονοπάτι
            queue_copy.append(path) # Τοποθέτησε το μονοπάτι στο τέλος του μετώπου

    elif method=='BestFS':
        for child in children:
            path=copy.deepcopy(node)
            path.append(child) 
            queue_copy.insert(0,path) # Τοποθέτησε τα μονοπάτια 
        queue_copy.sort(key=lambda x: sum(x[-1][1:5])) # Ταξινόμησε το μέτωπο με βάση το άθροισμα των ενοίκων του τελευταίου παιδιού κάθε μονοπατιού

    elif method=='HillC':
        best_path=None         # Αρχικοποίηση καλύτερου μονοπατιού
        best_cost=float('inf') # Αρχικοποίηση κόστους στο άπειρο
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            cost=sum(child[1:5])    # Υπολογισμός του κόστους με βάση το άθροισμα των ενοίκων του παιδιού
            if cost < best_cost:    # Αν το κόστος του τρέχων παιδιού είναι καλύτερο απο του καλύτερου μέχρι στιγμής
                best_path=path
                best_cost=cost
        if best_path:
            queue_copy.insert(0, best_path) # Τοποθέτησε το καλύτερο παιδί στην αρχή του μετώπου (άρα κρατιέται το μονοπάτι με το καλύτερο κόστος, τα άλλα κλαδεύονται)
    return queue_copy

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solution(front, queue, closed, goal, method):
    
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
    
    elif front[0]==goal:
        print('_GOAL_FOUND_',end=' ')
        print(front[0])    # Εμφάνιση goal
        for state in queue[0]: # Εμφάνιση μονοπατιού που οδηγέι στο goal
            print(state)
        
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method) # Επέκταση μετώπου
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method) # Επέκταση ουράς
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)
           
def main():
    
    initial_state = [0, 9, 4, 12, 7, 0] # Αρχική κατάσταση
    goal = [5, 0, 0, 0, 0, 0] # Τελική κατάσταση
    while True: # επιλογή μεθόδου αναζήτησης
        method = input('Choose search method (BFS, DFS, BestFS, HillC): ')
        if method in ['BFS', 'DFS', 'BestFS', 'HillC']:
            break
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method)
    
if __name__ == "__main__":
    main()

""" ----------------------------------------------------------------------------
**** Examples of execution of search algorithms:
**** Παράδειγματα εκτέλεσης αλγορίθμων αναζήτησης:
** DFS:
    _GOAL_FOUND_ [5, 0, 0, 0, 0, 0]
    [0, 9, 4, 12, 7, 0]
    [1, 1, 4, 12, 7, 8]
    [5, 1, 4, 12, 7, 0]
    [1, 0, 4, 12, 7, 1]
    [2, 0, 0, 12, 7, 5]
    [3, 0, 0, 9, 7, 8]
    [5, 0, 0, 9, 7, 0]
    [3, 0, 0, 1, 7, 8]
    [5, 0, 0, 1, 7, 0]
    [3, 0, 0, 0, 7, 1]
    [4, 0, 0, 0, 0, 8]
    [5, 0, 0, 0, 0, 0]
** BFS:
    _GOAL_FOUND_ [5, 0, 0, 0, 0, 0]
    [0, 9, 4, 12, 7, 0]
    [4, 9, 4, 12, 0, 7]
    [1, 8, 4, 12, 0, 8]
    [5, 8, 4, 12, 0, 0]
    [3, 8, 4, 4, 0, 8]
    [5, 8, 4, 4, 0, 0]
    [3, 8, 4, 0, 0, 4]
    [2, 8, 0, 0, 0, 8]
    [5, 8, 0, 0, 0, 0]
    [1, 0, 0, 0, 0, 8]
    [5, 0, 0, 0, 0, 0]
** BestFS:
    _GOAL_FOUND_ [5, 0, 0, 0, 0, 0]
    [0, 9, 4, 12, 7, 0]
    [1, 1, 4, 12, 7, 8]
    [5, 1, 4, 12, 7, 0]
    [3, 1, 4, 4, 7, 8]
    [5, 1, 4, 4, 7, 0]
    [4, 1, 4, 4, 0, 7]
    [1, 0, 4, 4, 0, 8]
    [5, 0, 4, 4, 0, 0]
    [2, 0, 0, 4, 0, 4]
    [3, 0, 0, 0, 0, 8]
    [5, 0, 0, 0, 0, 0]
** HillC:
    _GOAL_FOUND_ [5, 0, 0, 0, 0, 0]
    [0, 9, 4, 12, 7, 0]
    [3, 9, 4, 4, 7, 8]
    [5, 9, 4, 4, 7, 0]
    [1, 1, 4, 4, 7, 8]
    [5, 1, 4, 4, 7, 0]
    [4, 1, 4, 4, 0, 7]
    [3, 1, 4, 3, 0, 8]
    [5, 1, 4, 3, 0, 0]
    [2, 1, 0, 3, 0, 4]
    [3, 1, 0, 0, 0, 7]
    [1, 0, 0, 0, 0, 8]
    [5, 0, 0, 0, 0, 0]
"""
