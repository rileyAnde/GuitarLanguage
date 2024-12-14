'''
RILEY ANDERSON
EECS 510 FINAL PROJECT
'''

#function to read in the automata from memory
def read_automata():
    #store important data
    valid_characters = []
    transitions = {}
    start_state = ''
    accepting_state = ''
    data_structure = open("datastructure.txt", 'r')
    #counter to get specific line numbers
    count = 0
    for i in data_structure:
        #create the dict with empty lists for every state
        if count == 0:
            for x in i.strip().split():
                transitions[x] = []
        #save alphabet
        if count == 1:
            valid_characters = (i.strip().split(' '))
        #save start state
        if count == 2:
            start_state = i.strip()
        #save accept state
        if count == 3:
            accepting_state = i.strip()
        #append transitions into dict, with read character and next state at next index
        if count > 3:
            isfrom, read, to = i.strip().split()
            transitions[isfrom] += [read, to]
        count += 1
    #return the data structure
    return [transitions, valid_characters, start_state, accepting_state]



def accept(A, w):
    #define properties
    valid_characters = A[1]
    transitions = A[0]
    start_state = A[2]
    accepting_state = A[3]
    #split the string so we can iterate
    string = list(w)
    cur_state = start_state
    
    #read every character and check for a transition
    for i in string:
        #if a character isnt in the alphabet, the string cant be in the language
        if i not in valid_characters:
            print("Not in language. Invalid Characters. String rejected")
            return
        #if there is no transition, we are in an implied jail state
        elif i not in transitions[cur_state]:
            print(f"No transition exists from current state {cur_state} with character {i}. Implicit jail state. String rejected")
            return
        #otherwise, find the correct index
        else:
            next_state_idx = transitions[cur_state].index(i)+1
            cur_state_pointer = transitions[cur_state][next_state_idx]
            #print where we're coming from, reading, and going to
            print(f'From {cur_state}, read {i}, go to {cur_state_pointer}')
            #update pointer
            cur_state = cur_state_pointer
    #print success or failure
    if cur_state == accepting_state:
        print("String accepted.")
    else:
        print("Did not reach accept state. String rejected.")


#test with a string in the language
accept(read_automata(), '(022000)(022100)(002210)(x32010)(x02220)(320003)(xx0232)(xx0231)(020100)(xx0212)(x02020)(x32310)')

#and not in the language
accept(read_automata(), '(022010)')