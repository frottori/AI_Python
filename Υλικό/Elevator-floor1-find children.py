import copy
    
def go_to_floor1(state):
    if state[5]<8 and state[1]>0:
        if state[1]>8-state[5]:
            new_state = [1] + [state[1] + state[5] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[5]]
        return new_state

def find_children(state):
    
    children=[]
    
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    
    if floor1_child!=None: 
        children.append(floor1_child)
        
    return children

state= [0, 9, 11, 6, 14, 0]  
""" ----------------------------------------------------------------------------
**** [όροφος ασανσέρ, ένοικοι 1ου, ένοικοι 2ου, ένοικοι 3ου, ένοικοι 4ου, άτομα στο ασανσέρ]
"""
new_state=go_to_floor1(state)
print(new_state)

children=find_children(state)
print(children)
